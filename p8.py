# wapp to discover different functions in tuple
t1 = (10, 30, 20, 10)
t2 = (50, 10)

print(t1 + t2)

print(t1 * 3)

print(10 in t2)
print(20 in t1)
print(21 in t1)

#t1.apeend(80)
#t1.remove(10)
#tuples are immutable we cannot add or remove

print(t1.count(10))
print(t1.count(11))

print(t1.index(10))
#print(t1.index(11))
# since 11 is not in t1