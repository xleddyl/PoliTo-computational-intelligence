# Lab 3: Policy Search

## 3.1 - Fixed rules

The **Fixed rules agent** consists of the following two parts:

### 1. Main strategy

A simple approach to the game that consider only two possible states:

- Number of _remaining rows is even_

  - In this case the agent takes only `1` item from the row with the highest number of items

- Number of _remaining rows is odd_
  - In this case the agent takes all the item from the row with the highest number of items

### 2. Endgame strategy

When the board has only `3` rows left, the _endgame strategy_ is adopted.

This strategy consists in counting how many rows containing `1` item are left and, if there is only one, clear it by removing the last item. This prevents that the strategy of removing all the items from the row with the highest number of items, leaves the board in a state that will favor the opponent.

Example:

```text
 |
| |  agent wipes max row  ->   |
| |                           | |
the opponent can now take 1 item from the row
with 2 items, making the agent loose ❌

 |
| |  endgame strategy  ->  | |
| |                        | |
the opponent is now in a state in which every
move he does will result in him loosing ✅
```

## 3.2 - Evolved rules

⚠️ **TBD** ⚠️

## 3.3 - MinMax

Basic MinMax strategy with _alpha-beta_ pruning and `MAX_DEPTH` bound

## 3.4 - Reinforcement learning

RL agent trained agains a selected `TEACHER` during _n_ `EPOCHS` with parameters `ALPHA` and `RANDOM_FACTOR`

---

## Benchmarks

Winrates evaluated with the following parameters:

```py
# Evaluation
NIM_SIZE = 5
K = None
NUM_MATCHES = 100

# evolved
...

# minmax
MAX_DEPTH = 5

# rl
EPOCHS = 500
ALPHA = 0.1
RANDOM_FACTOR = 0.2
TEACHER = optimal_strategy
```

|                      | optimal_strategy | random_strategy | fixed_strategy | evolved_strategy | minmax_strategy | rl_strategy |
| -------------------- | :--------------: | :-------------: | :------------: | :--------------: | :-------------: | :---------: |
| **optimal_strategy** |        -         |   100% (0.1s)   |  100% (0.1s)   |                  |   100% (8.7s)   |  100% (2m)  |
| **random_strategy**  |       _0%_       |        -        |   9% (0.1s)    |                  |   2% (14.9s)    |  23% (3m)   |
| **fixed_strategy**   |       _0%_       |      _91%_      |       -        |                  |   52%(13.8s)    |  23% (2m)   |
| **evolved_strategy** |                  |                 |                |        -         |                 |             |
| **minmax_strategy**  |       _0%_       |      _98%_      |     _48%_      |                  |        -        |  63% (4m)   |
| **rl_strategy**      |       _0%_       |      _77%_      |     _77%_      |                  |      _37%_      |      -      |

Observation: with _minmax_strategy_ and _rl_strategy_ we could have achieved far better results raising `MAX_DEPTH` and `EPOCHS` respectively, at the cost of more execution time
