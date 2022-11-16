import math

from countInv import count_inversions as myinversions
from otherTest import count_inversions as otherinversions

RND_SIZE = 100

result = list(reversed(range(1, RND_SIZE + 1)))

print(myinversions(result))
print(result)
print(f"n logn = {RND_SIZE * math.log2(RND_SIZE)}")

result = list(reversed(range(1, RND_SIZE + 1)))

print(otherinversions(result))
print(result)
print(f"n logn = {RND_SIZE * math.log2(RND_SIZE)}")




