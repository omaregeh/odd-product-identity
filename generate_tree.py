# Generate the tree shown in the image: each row expands with two additional odds (symmetric around 15),
# and displays the sum at the beginning of the row.
def generate_symmetric_odd_tree(center, num_rows):
    rows = []
    for i in range(num_rows):
        # Number of terms in the row = 1 (center) + 2*i (symmetrical expansion)
        p = 1 + 2*i
        half = p // 2
        sequence = [center + 2 * k for k in range(-half, half + 1)]
        total = sum(sequence)
        rows.append((total, sequence))
    return rows

# Generate rows centered at 15, expanding outward
tree_rows = generate_symmetric_odd_tree(center=15, num_rows=10)

# Print the rows nicely
for total, sequence in tree_rows:
    print(f"{total:4}  =  {' + '.join(map(str, sequence))}")
