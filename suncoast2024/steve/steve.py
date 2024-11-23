import itertools
perfectSquares = []

for i in itertools.count():
    if i * i < 1e8:
        perfectSquares.append(i * i)
    else:
        break

numRepeaters, repeaterLim = map(int, input().split())
repeaters = list(map(int, input().split()))
repeaterLo = len(repeater)
repeaterHi = repeaterLim * len(repeater)
