item = [1, 2, 3, 4, 5]

from functools import reduce
product = reduce((lambda x, y: x**2 + y**2), [1,2,3,4])