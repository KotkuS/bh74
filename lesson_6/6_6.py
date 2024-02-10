# Дан список рандомных чисел, необходимо отсортировать его в виде,
# сначала четные, потом нечётные
from random import randint
numbers_list = [randint(1, 100) for _ in range(10)]
print(numbers_list)
first_list = list(filter(lambda x: not x % 2, numbers_list))
second_list = list(filter(lambda x: x % 2, numbers_list))
sorted_list = first_list + second_list
print(sorted_list)
