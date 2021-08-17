def valid_index(r, c):
    if 0 <= r < 5 and 0 <= c < 5:
        return True
    return False


def shoot(r, c, dir, tar):
    while True:
        new_row = r + movement[dir][0]
        new_col = c + movement[dir][1]
        if valid_index(new_row, new_col):
            if matrix[new_row][new_col] == "x":
                tar -= 1
                positions.append([new_row, new_col])
                matrix[new_row][new_col] = '.'
                break
            else:
                r = new_row
                c = new_col
                continue
        else:
            break

    return tar


def move(r, c, dir, num):
    new_row = r + movement[dir][0] * num
    new_col = c + movement[dir][1] * num
    if new_row >= 5:
        new_row = 4
    if new_col >= 5:
        new_col = 4
    if valid_index(new_row, new_col):
        if not matrix[new_row][new_col] == "x":
            matrix[r][c] = '.'
            matrix[new_row][new_col] = 'A'
            r = new_row
            c = new_col

    return [r, c]


movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

n = 5
matrix = []
pl_position = []
positions = []
targets = 0
for i in range(5):
    curr_row = input().split()
    if 'A' in curr_row:
        pl_position = [i, curr_row.index('A')]
    for el in curr_row:
        if el == "x":
            targets += 1
    matrix.append(curr_row)
a = 6
m = int(input())
all_targest = targets

for _ in range(m):
    command = input()
    try:
        com, direction, times = command.split()
        pl_position = move(pl_position[0], pl_position[1], direction, int(times))
    except:
        com, dir = command.split()
        targets = shoot(pl_position[0], pl_position[1], dir, targets)
    if targets <= 0:
        break

if targets <= 0:
    print(f"Training completed! All {all_targest} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
for el in positions:
    print(el)
