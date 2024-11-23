# this problem just sucks

grid = [input() for _ in range(6)]
placelocations = [5 for _ in range(7)]

for j in range(7):
    for i in range(6):
        if grid[i][j] != ".":
            placelocations[j] = i - 1
            break


for m in range(len(placelocations)):
    if placelocations[m] < 0: continue
    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i-1 > 0 and i-1 < 6) or (j+1 > 0 and j < 7): # while in bounds
        i -= 1
        j += 1
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)

    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i > 0 and i < 6) or (j+1 > 0 and j+1 < 7): # while in bounds
        i -= 0
        j += 1
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)

    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i+1 > 0 and i+1 < 6) or (j+1 > 0 and j+1< 7): # while in bounds 
        i += 1
        j += 1
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)

    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i+1 > 0 and i+1 < 6) or (j > 0 and j< 7): # while in bounds
        i += 1
        j += 0
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)

    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i+1 > 0 and i+1 < 6) or (j-1 > 0 and j-1< 7): # while in bounds
        i += 1
        j -= 1
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)

    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i > 0 and i < 6) or (j-1 > 0 and j-1 < 7): # while in bounds
        i += 0
        j -= 1
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)

    i = placelocations[m]
    j = m
    amtInRow = 1
    while (i-1 > 0 and i-1 < 6) or (j-1 > 0 and j-1 < 7): # while in bounds
        i -= 1
        j -= 1
        if grid[i][j] != "X": break
        amtInRow += 1
        if amtInRow == 4:
            print(m)
            exit(0)
print("Time to give up")
