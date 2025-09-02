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
