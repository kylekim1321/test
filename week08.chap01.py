a = [-11, 72, 9]
b = a.copy()
c = list(a)
d = a[:]
e = a

print(a, b, c, d, e)
a[1] = 2.71
print(a, b, c, d, e)
e[0] = "ishs"
print(a, b, c, d, e)