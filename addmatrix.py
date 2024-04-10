def add_matrices(X, Y):
    if len(X)!= len(Y) or len(X[0])!= len(Y[0]):
        print("Matrices have different dimensions. Addition not possible.")
        return None

    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]

    return result

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = add_matrices(X, Y)

if result:
    print("Result of matrix addition:")
    for row in result:
        print(row)
