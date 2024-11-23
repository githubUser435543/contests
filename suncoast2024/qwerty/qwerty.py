left = list("qwertasdfgzxcv")
right = list("yuiophjklbnm")

s = input()
score = len(s)
for i in range(1, len(s)):
    bothInLeft = (s[i] in left) and (s[i-1] in left)
    bothInRight = (s[i] in right) and (s[i-1] in right)

    if bothInLeft or bothInRight:
        score += 0.5
    else:
        score -= 0.2

print(score)
    
