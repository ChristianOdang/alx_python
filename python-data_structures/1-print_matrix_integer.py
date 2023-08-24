# A function that print a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end=' ' if i < len(row)-1 else '')
        print()
