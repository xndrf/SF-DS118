import numpy as np
a = np.int8(25)
print(a)
print(type(a))

print(np.iinfo(a))
b = np.uint8(124)
print(b)
print(np.iinfo(b))


print(np.iinfo(np.int64))

print(len(np.sctypeDict))
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

print(np.int8(456))