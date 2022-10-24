# Lab 1: Set Covering

## Task

Given a number $N$ and some lists of integers $P = (L_0, L_1, L_2, ..., L_n)$,
determine, if possible, $S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n})$
such that each number between $0$ and $N-1$ appears in at least one list

$$\forall n \in [0, N-1] \ \exists i : n \in L_{s_i}$$

and that the total numbers of elements in all $L_{s_i}$ is minimum.

---

## My implementation

To solve this problem I've choosen A\* with

- `priority_function = lambda state: state_cost[state] + h(state)`
- `h(state) = (N - len(state))`
- `unit_cost = lambda state, action: len(state & action)`

---

## Optimizations

The next possible action is selected from the set of possible moves by checking if the proposed list contains one (or more) number not already present in the current state:

```python
def possible_actions(state):
    return (State(set(m)) for m in MOVES if check_opt(state, m))

def check_opt(state, m):
    return not (list(m) <= list(state._data))
```

---

## Some results

(Using unit `cost = 1`)

| N    | steps | visited |
| ---- | ----- | ------- |
| 5    | 3     | 19      |
| 10   | 3     | 63      |
| 20   | 4     | 73      |
| 100  | 5     | 1.573    |
| 500  | 7     | 10.758   |
| 1000 | 9     | 18.961   |
