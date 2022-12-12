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

TBD

## 3.3 - MinMax

Basic MinMax strategy with _alpha-beta_ pruning and `MAX_DEPTH`

## 3.4 - Reinforcement learning

TBD

---

## Benchmarks

TBD
