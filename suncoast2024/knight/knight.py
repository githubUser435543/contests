# any honorable position must be a knights distance from a rook
# we can find the posions of all rooks in O(n^2)
# for each rook we can then look at the positions one knight move away from them 
# (this is O(1) because there are always 8 knight moves)
# and then we can check if those knight positions are attacked by rooks in O(1) using a set
# this solution has a total time complexity of O(n^2)
# if you don't know what a set is, it is a datastructure that allows you to
# insert, delete or find if an item is inside O(1)
# sets are cool

knightOffsets = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
rookLocations = []
rookRows = set()
rookColumns = set()
honorablePositions = []

grid = [input() for i in range(int(input()))]
grid = list(reversed(grid)) # 0, 0 at bottom
def inBounds(index): return index >= 0 and index < len(grid)

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == "R":
            rookLocations.append((i, j))
            rookRows.add(i)
            rookColumns.add(j)

for i, j in rookLocations:

    # delta i and delta j 
    for dI, dJ in knightOffsets:

        # if out of bounds
        if (not inBounds(i + dI)) or (not inBounds(j + dJ)): continue

        # can't place knight on a rook
        if grid[i + dI][j + dJ] == "R": continue

        # if positon is honorable
        # j is x and i is y
        if i + dI in rookRows or j + dJ in rookColumns: honorablePositions.append((j + dJ, i + dI))
honorablePositions.sort()
for x, y in honorablePositions:
    print(f"{x}, {y}")
