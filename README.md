# Odd Product Identity

This project explores a known arithmetic idea through a visual tree.

The identity itself is not new. For example:

```text
3 × n = (n - 2) + n + (n + 2)
```

This works because the `-2` and `+2` balance each other:

```text
(n - 2) + n + (n + 2) = 3n
```

What this project focuses on is **visualizing** that idea as a growing pattern of odd numbers.

## Main idea

Multiplication is usually introduced as repeated addition:

```text
3 × 7 = 3 + 3 + 3 + 3 + 3 + 3 + 3
```

But the same product can also be shown as a short strip of odd numbers:

```text
3 × 7 = 5 + 7 + 9
```

The middle number of the strip is the multiplier.

So instead of seeing `3 × 7` only as seven 3s, we can also see it as three consecutive odd numbers centered on 7.

## Example

```text
3 × 3 = 1 + 3 + 5

3 × 5 = 3 + 5 + 7

3 × 7 = 5 + 7 + 9

3 × 9 = 7 + 9 + 11

3 × 11 = 9 + 11 + 13
```

Each row is a different way to represent multiplication using balanced odd-number addition.

## How the tree shows it

The full tree starts with rows of consecutive odd numbers centered around a chosen odd number.

For center `3`, one row looks like this:

```text
3 × 7 = -3 + -1 + 1 + 3 + 5 + 7 + 9
```

Some terms cancel:

```text
-3 + 3 = 0
-1 + 1 = 0
```

After cancellation, the same row becomes:

```text
3 × 7 = 5 + 7 + 9
```

So the tree shows two things at the same time:

```text
3 × 7 = seven 3s
```

and

```text
3 × 7 = three odd numbers centered on 7
```

## General pattern

For multiplying by 3:

```text
3 × n = (n - 2) + n + (n + 2)
```

For multiplying by 5:

```text
5 × n = (n - 4) + (n - 2) + n + (n + 2) + (n + 4)
```

For any odd center number, the product can be visualized as a balanced strip of odd numbers centered on the multiplier.

## Interactive Visualizations

- [Odd Addition Multiplication Tree](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center3.html)
- [Center = 15 — Larger Tree](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center15.html)

## Files

- `symmetric-odd-tree-center3.html` — main interactive odd-number tree
- `symmetric-odd-tree-center15.html` — older larger center example
- `generate_tree.py` — Python generation file
- `odd_product_identity.py` — Python identity exploration
- `plot_multiple_N.py` — plotting file
- `main.tex` — LaTeX write-up

---

![](sierpinski-tree-readme.png)
