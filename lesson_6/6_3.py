# Дан список чисел и на вход поступает число N,
# необходимо сместить список на указанное число,
# пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
N = int(input("Enter a number to shift the list: "))
counter = 0
while counter < N:
    number = numbers.pop()
    numbers.insert(0, number)
    counter += 1
print(numbers)
