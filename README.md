# Odd Product Identity

This project explores mathematical identities involving the sum of consecutive odd integers and their relationship to integer products.

## Core Identity

For positive integers \( p \) and \( q \), the product \( pq \) can be expressed as the sum of \( p \) consecutive odd numbers centered around \( q \), under certain conditions. This leads to the identity:

\[
pq = \sum_{k = -\frac{p-1}{2}}^{\frac{p-1}{2}} (2q + 2k - 1)
\]

## Symmetric Odd Number Tree Visualization

Interactive visualizations showing how odd numbers can be arranged in symmetric patterns around different center values, with each row expanding outward.

### 🌳 Interactive Tree Visualizations:
- **[Center: 3](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center3.html)** - Smaller numbers, includes negatives
- **[Center: 15](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center15.html)** - Larger numbers, all positive

### Pattern Properties:
- **Row n**: Contains (1 + 2n) odd numbers, symmetric around center value
- **Numbers**: Start from (center - 2n) and increment by 2  
- **Sum**: Always equals center × (number of terms in row)
- **Growth**: Each row adds one number to each side

### Example Output (Center: 3):
3  =  3

9  =  1 + 3 + 5

15  =  -1 + 1 + 3 + 5 + 7

21  =  -3 + -1 + 1 + 3 + 5 + 7 + 9

27  =  -5 + -3 + -1 + 1 + 3 + 5 + 7 + 9 + 11

### Example Output (Center: 15):
15  =  15

45  =  13 + 15 + 17

75  =  11 + 13 + 15 + 17 + 19

105  =  9 + 11 + 13 + 15 + 17 + 19 + 21

135  =  7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23

### Mathematical Insight:
The sum of n consecutive odd numbers centered around k is always k × n, which connects to the broader odd product identity explored in this repository.

## What's Included

- `odd_product_identity.py`: A Python script to find decompositions for a single number \( N \).
- `plot_multiple_N.py`: A Python script that plots all valid decompositions for many values of \( N \).
- `generate_tree.py`: Python script to generate the symmetric odd number tree pattern.
- `symmetric-odd-tree-center3.html`: Interactive visualization centered on 3.
- `symmetric-odd-tree-center15.html`: Interactive visualization centered on 15.
- `main.tex`: A LaTeX paper draft including definitions, theorems, and introduction.

## How to Use

Install matplotlib:
```bash
pip install matplotlib
Then run the Python scripts:
bashpython3 odd_product_identity.py
python3 plot_multiple_N.py
python3 generate_tree.py


### STATUS:
Work in progress 
