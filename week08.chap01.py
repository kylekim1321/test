a = [-11, [3, 0], 9]
b = a.copy()
c = list(a)
d = a[:]
e = a

print(a, b, c, d, e)
a[1][0] = 7
# a[1] = 99
print(a, b, c, d, e)
