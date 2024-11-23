from queue import Queue

# takes in the graph (grid), start location, and end location
# returns int, distance from O to X
def shortestPathFloodFill(g, start, end):
    # visited[i][j] stores -1 if node not visited or distance from start if visited
    # this uses list comprehension if you want to look up how it works
    visited = [[-1 for i in g[0]] for j in g]
    visited[start[0]][start[1]] = 0 
   
    # FILO data structure
    # think of it as a waiting line
    q = Queue()
    q.put((start[0], start[1]))
    while not q.empty():
        i, j = q.get()
        # i delta and j delta. Movement up and left.
        for iD, jD in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nxtI = i + iD
            nxtJ = j + jD 
            if nxtI < 0 or nxtI >= len(g) or nxtJ < 0 or nxtJ >= len(g[0]): continue # out of range
            if g[nxtI][nxtJ] == "#": continue # wall
            if visited[nxtI][nxtJ] != -1: continue # been here
            visited[nxtI][nxtJ] = visited[i][j] + 1
            q.put((nxtI, nxtJ))
            # checking here so it doesn't have to pass through the queue
            if nxtI == end[0] and nxtJ == end[1]:
                return visited[nxtI][nxtJ]
    return -1


rows, cols = map(int, input().split())
grid = [input() for _ in range(rows)]
srt = [-1, -1]
ed = [-1, -1]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O": srt = [i, j]
        if grid[i][j] == "X": ed = [i, j]

print(shortestPathFloodFill(grid, srt, ed))


