a = [1, 9, 11]
b = a
print(a, b)
a[1] = 55
print(a, b) # b가 참조 하는 객체와 a가 참조 하는 객체가 같다.
b[-1] = "Python"
print(a, b)
for i in range(2, -1, -1):
    print(i)