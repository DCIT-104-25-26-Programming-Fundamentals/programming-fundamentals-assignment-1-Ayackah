# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if matrix_a else 0
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if matrix_a else 0
    cols_b = len(matrix_b[0]) if matrix_b else 0
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            sum_product = 0
            for k in range(cols_a):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(sum_product)
        result.append(new_row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def read_matrix(prompt):
    rows = int(input(f"Enter number of rows for {prompt}: "))
    cols = int(input(f"Enter number of columns for {prompt}: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} for {prompt}: ").split()))
        matrix.append(row)
    return matrix


def main():
    print("Part A - Transpose Matrix")
    matrix = read_matrix("matrix")
    print("Original matrix:")
    print_matrix(matrix)
    print("Transpose:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed)

    print("\nPart B - Add Two Matrices")
    matrix_a = read_matrix("matrix A")
    matrix_b = read_matrix("matrix B")
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Matrices must have the same dimensions")
        return
    result = add_matrices(matrix_a, matrix_b)
    print("Sum of matrices:")
    print_matrix(result)

    print("\nPart C - Multiply Two Matrices")
    matrix_a = read_matrix("matrix A")
    matrix_b = read_matrix("matrix B")
    if len(matrix_a[0]) != len(matrix_b):
        print("Incompatible matrix dimensions")
        return
    result = multiply_matrices(matrix_a, matrix_b)
    print("Result of A * B:")
    print_matrix(result)


if __name__ == "__main__":
    main()