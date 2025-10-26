# Odd Product Identity — Pascal & Sierpiński Tree

<p align="center">
  <img src="sierpinski-tree-readme.png" width="820" alt="Sierpiński Pascal Tree on symmetric odd-number lattice">
</p>

A visualization of the **symmetric odd-number tree** centered at 3, where each level represents a ±2 random walk.  
Pascal multiplicities are overlaid to reveal modular and fractal structures such as the **Sierpiński triangle**.

---

## 🔭 Live Interactive Version

👉 **[View the interactive Pascal & Sierpiński Tree](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center3-pascal.html)**

You can adjust:
- **Depth (n):** Number of steps in the ±2 random walk  
- **Value coloring:** `(3 + 2k) mod m` for any modulus  
- **Multiplicity mask:** `C(n, (n+k)/2) mod p` to visualize Pascal fractals  
- **Sierpiński mode:** Set `p = 2` and dim zeros to see the classic pattern emerge

---

## 🧮 Mathematical Background

Each row at depth **n** represents all possible sums of n independent ±2 steps starting at 3.  
The value at position **k** is \( x = 3 + 2k \), with multiplicity:

\[
M(n, k) = C\!\left(n, \frac{n + k}{2}\right)
\]
(defined only when \( n + k \) is even)

### Key identities

\[
\sum_k (3 + 2k)\,C\!\left(n,\frac{n+k}{2}\right) = 3 \cdot 2^n
\]

\[
\sum_k (3 + 2k)^2\,C\!\left(n,\frac{n+k}{2}\right) = (9 + 4n)\,2^n
\]

This means:
- The **average value** per row is always **3**.  
- The **variance** grows linearly with n — characteristic of a diffusion process.  
- Modular coloring (mod 2, 3, 5, 7, …) reveals **Sierpiński** and **Lucas-theorem** fractals.

---

## 🌈 Visual Modes

| Mode | Description |
|------|--------------|
| **Pascal Multiplicities** | Shows binomial counts \( C(n,(n+k)/2) \) as badges |
| **Size by Multiplicity** | Scales each node by its multiplicity |
| **Modular Coloring** | Colors by value `(3+2k) mod m` |
| **Mod-p Masking** | Dims or highlights nodes by multiplicity mod p (Sierpiński and beyond) |
| **Show Meta Info** | Displays (n, k) coordinates and parity |

---

## 🧩 Mathematical Connections

- **Combinatorics of restricted walks:** each row is a binomial layer of a ±2 random walk  
- **Catalan and Ballot numbers:** appear when restricting to \( k \ge 0 \)  
- **Modular arithmetic:** Sierpiński fractal for p = 2; Lucas-theorem patterns for other primes  
- **Moments and invariants:** mean = 3, variance = 4n  
- **Visual pedagogy:** connects Pascal’s triangle, random walks, and parity into one structure  

---

## 🖼️ Image Credits

The image above was generated using the mod-2 mask (Sierpiński pattern) at depth 9.  
You can reproduce it directly from the interactive page by exporting as PNG.

---

## 🧠 Future Directions

| Theme | Idea | Why it matters |
|-------|------|----------------|
| **Mod-p fractals** | Explore p = 3, 5, 7 | Visualize Lucas’ theorem |
| **Catalan subsets** | Restrict to k ≥ 0 | Reveals Dyck paths |
| **Generating functions** | \( \sum_k C(n,(n+k)/2)x^k \) | Links to Chebyshev & Hermite polynomials |
| **Prime highlighting** | Mark where (3+2k) is prime | Studies prime density |
| **3-D surface** | Height = multiplicity | Builds a “Pascal mountain” |

---

## 🔗 Related Pages

- [Center = 3 (Original Tree)](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center3.html)  
- [Center = 3 (Pascal + Sierpiński)](https://omaregeh.github.io/odd-product-identity/symmetric-odd-tree-center3-pascal.html)

---

## 🧾 Reference

Derived from the project *Symmetric Odd Number Tree (Center 3) + Pascal Multiplicities*:contentReference[oaicite:0]{index=0}  
© 2025 Omar Egeh — *Odd Product Identity Project*
