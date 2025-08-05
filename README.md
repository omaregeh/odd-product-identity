# Odd Product Identity

This project explores mathematical identities involving the sum of consecutive odd integers and their relationship to integer products.

## Core Identity

For positive integers \( p \) and \( q \), the product \( pq \) can be expressed as the sum of \( p \) consecutive odd numbers centered around \( q \), under certain conditions. This leads to the identity:

\[
pq = \sum_{k = -\frac{p-1}{2}}^{\frac{p-1}{2}} (2q + 2k - 1)
\]

## Symmetric Odd Number Tree Visualization

A new interactive visualization showing how odd numbers can be arranged in symmetric patterns around a center value (15), with each row expanding outward.

### 🌳 [View Interactive Tree Visualization](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree.html)

### Pattern Properties:
- **Row n**: Contains (1 + 2n) odd numbers, symmetric around 15
- **Numbers**: Start from (15 - 2n) and increment by 2  
- **Sum**: Always equals 15 × (number of terms in row)
- **Growth**: Each row adds one number to each side

### Example Output:
```
  15  =  15
  45  =  13 + 15 + 17
  75  =  11 + 13 + 15 + 17 + 19
 105  =  9 + 11 + 13 + 15 + 17 + 19 + 21
 135  =  7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23
```

### Mathematical Insight:
The sum of n consecutive odd numbers centered around k is always k × n, which connects to the broader odd product identity explored in this repository.

## What's Included

- `odd_product_identity.py`: A Python script to find decompositions for a single number \( N \).
- `plot_multiple_N.py`: A Python script that plots all valid decompositions for many values of \( N \).
- `generate_tree.py`: Python script to generate the symmetric odd number tree pattern.
- `symmetric-odd-tree.html`: Interactive visualization of the tree pattern.
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
python3 generate_tree.py
```

## Status

Work in progress — contributions welcome!
