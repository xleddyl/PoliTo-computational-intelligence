from quarto import Quarto, Player
from copy import deepcopy
import numpy as np
import random
import math

class AgentXleddyl(Player):

    def __init__(self, quarto: Quarto, starting_depth: int = 4, affordable_moves: int = 7) -> None:
        super().__init__(quarto)
        self.__default_move = (-1, (-1, -1))
        self.__win_score = 9 * 10 # max point (3 pieces * 3 features = 9, 9 * all winning positions)
        self.__tie_score = self.__win_score / 2 # ci si accontenta
        self.__affordable_complexity = math.factorial(affordable_moves if affordable_moves <= 16 else 16) ** 2 # math.factorial(16) ** 2 max complexity
        self.__starting_depth = starting_depth
        self.__depth = self.__starting_depth # increased autonomously based on self.__affordable_complexity

    def choose_piece(self) -> int:
        pieces = self.__get_remaining_pieces(self.get_game())
        if len(pieces) == 16:
            self.__depth = self.__starting_depth
            return random.choice(pieces)
        return self.__minmax('choose')

    def place_piece(self) -> tuple[int, int]:
        moves = self.__get_possible_moves(self.get_game())
        if len(moves) == 16:
            self.__depth = self.__starting_depth
            return random.choice(moves)
        return self.__minmax('place')

    def __minmax(self, action: str) -> int | tuple[int, int]:
        def increase_depth(game: Quarto) -> int:
            remaining_moves = len(self.__get_remaining_pieces(game))
            complexity = math.factorial(remaining_moves) ** 2
            return self.__depth if complexity >= self.__affordable_complexity else math.inf

        def fallback_score(game: Quarto) -> int:
            minmax_turn = game.get_current_player()
            real_turn = self.get_game().get_current_player()
            board = game.get_board_status()

            count_prop_eq = lambda i: 1 if i.count(1) == len(i) or i.count(0) == len(i) else 0
            map_to_bin = lambda i: (len(i), [game.get_piece_charachteristics(j).binary for j in i])
            map_to_eq = lambda i: (i[0], sum([count_prop_eq(prop) for prop in zip(*i[1])]) if len(i[1]) > 1 else 1)

            rows = [[j for j in i.tolist() if j != -1] for i in board]
            cols = [[j for j in i.tolist() if j != -1] for i in board.T]
            diags = [[i for i in board.diagonal().tolist() if i != -1], [i for i in np.fliplr(board).diagonal().tolist() if i != -1]]
            rows_bin = [map_to_bin(row) for row in rows if len(row) > 0]
            cols_bin = [map_to_bin(col) for col in cols if len(col) > 0]
            diags_bin = [map_to_bin(diag) for diag in diags if len(diag) > 0]
            rows_eq = [map_to_eq(row) for row in rows_bin]
            cols_eq = [map_to_eq(col) for col in cols_bin]
            diags_eq = [map_to_eq(diag) for diag in diags_bin]

            rows_score = sum([row[1] * row[0] for row in rows_eq])
            cols_score = sum([col[1] * col[0] for col in cols_eq])
            diags_score = sum([diag[1] * diag[0] for diag in diags_eq])
            return (rows_score + cols_score + diags_score) * (-1 if minmax_turn == real_turn else 1)

        def alpha_beta(my_turn: bool, score, alpha, beta):
            if my_turn:
                if score <= alpha:
                    return True, alpha, beta
                return False, alpha, min(beta, score)
            else:
                if score >= beta:
                    return True, alpha, beta
                return False, max(alpha, score), beta

        def win_scores(winner: int, minmax_turn: int) -> float:
            real_turn = self.get_game().get_current_player()
            my_turn = minmax_turn == real_turn
            if winner == -1: return self.__tie_score * (-1 if my_turn else 1)
            else: return self.__win_score * (-1 if winner == real_turn else 1)

        def minmax_fn(game: Quarto, action: str, depth: int = 0, alpha = (-math.inf, self.__default_move), beta = (math.inf, self.__default_move)) -> tuple[float, tuple[tuple[int, int], int]]:
            minmax_turn = game.get_current_player()
            real_turn = self.get_game().get_current_player()
            score = math.inf * (1 if minmax_turn == real_turn else -1), self.__default_move

            winner = game.check_winner()
            finished = game.check_finished()

            moves = self.__get_possible_moves(game)
            remaining_pieces = self.__get_remaining_pieces(game)

            if depth >= self.__depth:
                return fallback_score(game), self.__default_move
            elif len(moves) == 1:
                return fallback_score(game), (remaining_pieces[0], moves[0])
            elif finished or winner != -1:
                return win_scores(winner, minmax_turn), self.__default_move

            if action == 'place':
                for move in moves:
                    _game = deepcopy(game)
                    _game.place(*move)
                    val, _ = minmax_fn(_game, 'choose', depth + 1, alpha, beta)
                    score = (min if minmax_turn == real_turn else max)(score, (val, (self.__default_move[0], move)))
                    res, alpha, beta = alpha_beta(minmax_turn == real_turn, score, alpha, beta)
                    if res:
                        break
                return score
            elif action == 'choose':
                for piece in remaining_pieces:
                    _game = deepcopy(game)
                    _game.select(piece)
                    _game._current_player = 1 - _game._current_player
                    val, _ = minmax_fn(_game, 'place', depth + 1, alpha, beta)
                    score = (min if minmax_turn == real_turn else max)(score, (val, (piece, self.__default_move[1])))
                    res, alpha, beta = alpha_beta(minmax_turn == real_turn, score, alpha, beta)
                    if res:
                        break
                return score

        self.__depth = increase_depth(self.get_game())
        score, (piece, move) = minmax_fn(self.get_game(), action)
        return piece if action == 'choose' else move

    def __get_possible_moves(self, game: Quarto) -> list[tuple[int, int]]:
        # moves in the format (y, x)
        return [(j, i) for i in range(0, game.BOARD_SIDE) for j in range(0, game.BOARD_SIDE) if game.get_board_status()[i, j] == -1]

    def __get_remaining_pieces(self, game: Quarto) -> list[int]:
        board = game.get_board_status()
        placed = [board[i, j] for i in range(0, game.BOARD_SIDE) for j in range(0, game.BOARD_SIDE) if i != -1 and j != -1]
        return [i for i in range(0, 16) if placed.count(i) == 0]
