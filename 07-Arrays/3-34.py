def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


if __name__ == "__main__":
    print_matrix(identity_matrix(3))
    print()
    print_matrix(identity_matrix(5))
    print()
    print_matrix(identity_matrix(8))