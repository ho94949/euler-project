import fractions
from functools import reduce

print (reduce(lambda x, y: x*y//fractions.gcd(x, y), list(range(1,21))))
