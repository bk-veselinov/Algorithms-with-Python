def get_magic_triangle(n):
    matrix = []
    big_mat = []
    a = ''
    for line in range(0, n):

        for i in range(0, line + 1):
            matrix.append((binomialCoeff(line, i)))
        big_mat.append(matrix)
        matrix = []
    return big_mat


def binomialCoeff(n, k):
    res = 1

    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res




get_magic_triangle(5)
