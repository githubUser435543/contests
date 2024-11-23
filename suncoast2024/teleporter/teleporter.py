# This problem is a somewhat obsfuscated "find the lcm of 3 numbers"
# we can do this directly with math.lcm
# this gives us the answer in earth days and we need to divide by 365
# we now round like the problem says
from math import *
print(round(lcm(int(input()), int(input()), int(input()))/365))

