import math

def valid_index(r, c):

    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


n = int(input())
matrix = [[j for j in input().split()]for i in range(n)]

movement = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
coins = 0
p = False
path = []
win = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            while True:
                command = input()
                if command in movement:
                    new_row = row + int(movement[command][0])
                    new_col = col + int(movement[command][1])
                    if valid_index(new_row, new_col):
                        try:
                            coins += int(matrix[new_row][new_col])
                            path.append([new_row, new_col])

                        except:
                            p = True
                            coins /= 2
                            break
                    else:
                        p = False
                        coins /= 2
                        break
                    if coins >= 100:
                        p = True
                        win = True
                        break

                    row = new_row
                    col = new_col
        if p:
            break
    if p:
        break
if win:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins)} coins.")
print(f'Your path:')
for el in path:
    print(el)

