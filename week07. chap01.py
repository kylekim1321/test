numbers = list()
for i in range(0, 11):
    numbers.append(i)
print(numbers)
reverse_numbers = numbers[::-1]
print(reverse_numbers)
print(numbers)
numbers.reverse() #자체 값 변경
print(numbers)
numbers.append(-11)
print(numbers)
numbers.insert(__index=5, __object=99)
print(numbers)
numbers.insert(-2, __object=55) #list multiplication
numbers = numbers * 2
print(numbers)