# Lab 1: Set Covering

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
