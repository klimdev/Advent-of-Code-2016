
from Checksum import Checksum
from DragonCurve import DragonCurveUpTo

#10000001111001111110000
#10000011110010000111110
print(DragonCurveUpTo('10000',20))
print(Checksum(DragonCurveUpTo('10000',20)[:20]))
print()
print(Checksum(DragonCurveUpTo('10011111011011001',272)[:272]))
print(Checksum(DragonCurveUpTo('10011111011011001',35651584)[:35651584]))