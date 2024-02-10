# Дан список чисел, необходимо его развернуть
# без использования метода revese и функции reversed,
# а так же дополнительного списка и среза
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers_list)
counter = 0
n = len(numbers_list)
while counter < n:
    number = numbers_list.pop()
    numbers_list.insert(counter, number)
    counter += 1
print(numbers_list)
