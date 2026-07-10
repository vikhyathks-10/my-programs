# ==========================================================
# Month 7 - Day 10
# Matrix Problems
#
# Topics Covered:
# 1. Matrix Transpose
# 2. Matrix Addition
# 3. Matrix Multiplication
# 4. Spiral Traversal
# 5. Rotate Matrix (90° Clockwise)
# 6. Diagonal Sum
# ==========================================================

print("=" * 60)
print("1. MATRIX TRANSPOSE")
print("=" * 60)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = []

for col in range(len(matrix[0])):
    row_data = []
    for row in range(len(matrix)):
        row_data.append(matrix[row][col])
    transpose.append(row_data)

print("Original Matrix")
for row in matrix:
    print(row)

print("\nTranspose")
for row in transpose:
    print(row)


print("\n" + "=" * 60)
print("2. MATRIX ADDITION")
print("=" * 60)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Matrix A")
for row in A:
    print(row)

print("\nMatrix B")
for row in B:
    print(row)

print("\nAddition")
for row in result:
    print(row)


print("\n" + "=" * 60)
print("3. MATRIX MULTIPLICATION")
print("=" * 60)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

rows = len(A)
cols = len(B[0])
common = len(B)

product = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        for k in range(common):
            product[i][j] += A[i][k] * B[k][j]

print("Product Matrix")

for row in product:
    print(row)


print("\n" + "=" * 60)
print("4. SPIRAL TRAVERSAL")
print("=" * 60)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

top = 0
bottom = len(matrix)-1
left = 0
right = len(matrix[0])-1

spiral = []

while top <= bottom and left <= right:

    for i in range(left, right+1):
        spiral.append(matrix[top][i])
    top += 1

    for i in range(top, bottom+1):
        spiral.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left-1, -1):
            spiral.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top-1, -1):
            spiral.append(matrix[i][left])
        left += 1

print("Spiral Order")
print(spiral)


print("\n" + "=" * 60)
print("5. ROTATE MATRIX (90° CLOCKWISE)")
print("=" * 60)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Original")

for row in matrix:
    print(row)

rotated = [list(row) for row in zip(*matrix[::-1])]

print("\nRotated")

for row in rotated:
    print(row)


print("\n" + "=" * 60)
print("6. DIAGONAL SUM")
print("=" * 60)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

primary = 0
secondary = 0
n = len(matrix)

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n-i-1]

print("Primary Diagonal Sum :", primary)
print("Secondary Diagonal Sum :", secondary)

if n % 2 == 1:
    total = primary + secondary - matrix[n//2][n//2]
else:
    total = primary + secondary

print("Total Diagonal Sum :", total)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Matrix Transpose
Swap rows and columns.

Time:
O(rows × cols)

----------------------------------------

✔ Matrix Addition

Add corresponding elements.

Time:
O(rows × cols)

----------------------------------------

✔ Matrix Multiplication

Row × Column multiplication.

Time:
O(n³)

----------------------------------------

✔ Spiral Traversal

Traverse matrix layer by layer.

Time:
O(rows × cols)

----------------------------------------

✔ Rotate Matrix

90° Clockwise

Reverse rows
+
Transpose

OR

zip(*matrix[::-1])

----------------------------------------

✔ Diagonal Sum

Primary:
matrix[i][i]

Secondary:
matrix[i][n-i-1]

----------------------------------------

Interview Tip

Whenever a question involves:

✔ Grid
✔ Image
✔ Chess Board
✔ Game Board

Think:

👉 Matrix Problem

Common Patterns:

• Traversal
• Rotation
• Transpose
• Spiral
• Diagonal
""")