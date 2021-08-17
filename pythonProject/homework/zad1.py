from collections import deque

choko = [int(el) for el in input().split(', ')]
milk = deque([int(el) for el in input().split(', ')])
milk_shakes = 0
success = False

while milk and choko:
    if milk_shakes >= 5:
        success = True
        break
    curr_milk = milk.popleft()
    curr_choko = choko.pop()

    if curr_milk <= 0 and curr_choko <= 0:
        continue

    if curr_milk <= 0:
        choko.append(curr_choko)
        continue

    elif curr_choko <= 0:
        milk.appendleft(curr_milk)
        continue
    elif curr_choko == curr_milk:
        milk_shakes += 1
    else:
        curr_choko -= 5
        milk.append(curr_milk)
        choko.append(curr_choko)


if success:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if choko:
    print(f"Chocolate: {', '.join([str(el) for el in choko])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(el) for el in milk])}")
else:
    print("Milk: empty")