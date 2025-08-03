# Odd Product Identity

This project explores a mathematical identity involving the sum of consecutive odd integers and its relationship to integer products.

## Core Identity

For positive integers \( p \) and \( q \), the product \( pq \) can be expressed as the sum of \( p \) consecutive odd numbers centered around \( q \), under certain conditions. This leads to the identity:

\[
pq = \sum_{k = -\frac{p-1}{2}}^{\frac{p-1}{2}} (2q + 2k - 1)
\]

## What’s Included

- `odd_product_identity.py`: A Python script to find decompositions for a single number \( N \).
- `plot_multiple_N.py`: A Python script that plots all valid decompositions for many values of \( N \).
- `main.tex`: A LaTeX paper draft including definitions, theorems, and introduction.

## How to Use

Install matplotlib:

```bash
pip install matplotlib
```

Then run the Python scripts:

```bash
python3 odd_product_identity.py
python3 plot_multiple_N.py
```

## Status

Work in progress — contributions welcome!
