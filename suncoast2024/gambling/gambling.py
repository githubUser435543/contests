import math

def profitsNeeded(debt, loss, gain):
    # gain - loss / 2 is the average profit 
    # the reason we use math.ceil and not math.round is because
    # the 0.2 still requires a full turn of profit
    return math.ceil(debt / ((gain - loss) / 2))

d, m, l = map(int, input().split())

# l - m is the profit over two games
if l - m > 0:
    print(profitsNeeded(d, m, l))
else:
    print("change rates!")
    

