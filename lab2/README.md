# Lab 2: Evolutionary Set Covering

## Task

Given a number $N$ and some lists of integers $P = (L_0, L_1, L_2, ..., L_n)$,
determine, if possible, $S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n})$
such that each number between $0$ and $N-1$ appears in at least one list

$$\forall n \in [0, N-1] \ \exists i : n \in L_{s_i}$$

and that the total numbers of elements in all $L_{s_i}$ is minimum.

---

## Some results

using:

```python
POP_SIZE = 100
GEN = 500
OFFSPRING_SIZE = 100
SEED = 42
MUTATION_RATE = 0.5
```

| N    | w    | num_gen | bloat |
| ---- | ---- | ------- | ----- |
| 5    | 7    | 141     | 40%   |
| 10   | 21   | 194     | 110%  |
| 20   | 41   | 165     | 105%  |
| 100  | 330  | 336     | 230%  |
| 500  | 2028 | 450     | 305%  |
| 1000 | 4839 | 405     | 383%  |
