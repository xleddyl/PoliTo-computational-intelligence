# ♟️ Quarto! with MinMax

Quarto is a two-player strategy game where the goal is to place pieces on a 4x4 board in such a way that all pieces in a row share a common attribute (such as color or shape).

This repository contains a Python-based implementation of the game with an AI player that implements the MinMax algorithm, which evaluates all possible moves and countermoves to determine the optimal move for the current player.

## 🎮 How to run

By running [main.py](./main.py) a new game is started. All the relevant info about the current board state are printed alongside with the choices made by the players.

```cli
python3 main.py
```

- `-m`: allows to specify the number of matches to run _(for `m>1` the board states are not printed, default `m=1`)_

  - ```cli
    python3 main.py -m 10
    ```

The board states are represented by a `4ⅹ4` grid containg numbers from 0 to 15 to represent the different pieces

```txt
0   →  [0, 0, 0, 0]  →  [small, black, solid , round]
1   →  [0, 0, 0, 1]  →  [small, black, solid , square]
2   →  [0, 0, 1, 0]  →  [small, black, hollow, round]
3   →  [0, 0, 1, 1]  →  [small, black, hollow, square]
4   →  [0, 1, 0, 0]  →  [small, white, solid , round]
5   →  [0, 1, 0, 1]  →  [small, white, solid , square]
6   →  [0, 1, 1, 0]  →  [small, white, hollow, round]
7   →  [0, 1, 1, 1]  →  [small, white, hollow, square]
8   →  [1, 0, 0, 0]  →  [tall , black, solid , round]
9   →  [1, 0, 0, 1]  →  [tall , black, solid , square]
10  →  [1, 0, 1, 0]  →  [tall , black, hollow, round]
11  →  [1, 0, 1, 1]  →  [tall , black, hollow, square]
12  →  [1, 1, 0, 0]  →  [tall , white, solid , round]
13  →  [1, 1, 0, 1]  →  [tall , white, solid , square]
14  →  [1, 1, 1, 0]  →  [tall , white, hollow, round]
15  →  [1, 1, 1, 1]  →  [tall , white, hollow, square]
```

## 💡 How the MinMax Agent works

`AgentXleddyl` implements a MinMax algorithm that works in the following way:

- The initial move is randomly determined, as experiments from ([1](#-references)) has shown that the selection and placement of the first piece have no significant impact
- From the second move on, the MinMax algorithm is employed

### Depth

A dynamic depth adjustment is adopted, increasing the depth to +∞ as soon as the board reaches a state that is ideal for exploration. According to ([1](#-references)), the initial size of the search space is a staggering `(16!)^2 = 4.4e26` states, which would take approximately `44 million` years to process on a 1GHz machine. To overcome this limitation, the depth is set to increase to +∞ when there are 7 moves remaining, which results in a much more manageable `(7!)^2 = 2.54e7` states that will only take `2.54 seconds` to process on a 1GHz machine (note that 7 is an upper limit for speed, as 8 moves would require 24 minutes to process).

### Score

When the maximum depth is reached (4 during the early stages of the game), a score is assigned to the current state of the board. The score is determined by considering the number of matching features between each element in a row (also column and diagonal) and the total number of elements.\
Then the scores of all the rows, columns, and diagonals are added together to obtain the final score.

For example, consider the following row:

- `[0, 1, 2, -1]`
  - the number of common features is `2`
  - the number of elements is `3`
  - the score assigned to the row is `3*2 = 6`

Finally, a score of `90` is assigned if the MinMax algorithm discovers a winning state, and a score of `45` is assigned in case of a draw.

## 🧪 Results

The results from 100 matches between `AgentXleddyl` and `AgentRandom` are the following:

```cli
AgentXleddyl win rate against AgentRandom: 99.0%
  -  AgentXleddyl      99
  -  AgentRandom       0
  -  ties              1

(avg match time: 14.44s)
```

## 🗂️ Folder structure

- [📁 players](./players/)  _folder containing the players_
  - [📄 AgentRandom.py](./players/AgentRandom.py) → _player making random moves_
  - [📄 AgentXleddyl.py](./players/AgentXleddyl.py) → _player implementing MinMax_
- [📁 quarto](./quarto/) → _folder containing Quarto!'s classes_
  - [📄 objects.py](./quarto/objects.py) → _quarto game provided by prof_
  - [📄 objects2.py](./quarto/objects2.py) → _quarto game provided by prof_
  - [📄 objects3.py](./quarto/objects3.py) → _quarto game provided by prof, modified for better printing of the board state_
- [📄 main.py](./main.py) → _start the game_

## 📚 References

- <http://web.archive.org/web/20041012023358/http://ssel.vub.ac.be/Members/LucGoossens/quarto/quartotext.htm>
- <https://stmorse.github.io/journal/quarto-part1.html>

---
