letterAs = 0

for n in range(int(input())):
    for char in input():
        if char in "Aa": letterAs += 2
print(letterAs)
