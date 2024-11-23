x = int(input())
i = 0
while x != 1:
    x = 3*x + 1 if x & 1 else x // 2
    i= -~i
print(i)
