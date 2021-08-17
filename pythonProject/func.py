def matrix_maker():
    n, m = [int(el) for el in input().split()]
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in input().split():
            matrix[row].append(col)
    return matrix


def square_matrix():
    n = int(input())
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in input().split():
    #    for col in input():
            matrix[row].append(col)
    return matrix


def valid_index(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


def remove_25(rem, iter):
    while rem in iter:
        remove_index = iter.index(rem)
        iter.pop(remove_index)
        try:
            iter.pop(remove_index)
        except:
            pass
    return iter


def remove_25_f(rem, iter):
    while rem in iter:
        remove_index = iter.index(rem)
        del iter[remove_index]
        try:
            del iter[remove_index]
        except:
            pass
    return iter

movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}