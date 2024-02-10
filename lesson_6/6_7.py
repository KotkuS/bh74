# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_list = []
left_number = -1
right_number = -len(numbers_list) + 1
n = 0
while n < len(numbers_list):
    sum_list.append(numbers_list[left_number] + numbers_list[right_number])
    n += 1
    left_number += 1
    right_number += 1
sum_for_number_in_list = list(zip(numbers_list, sum_list))
for _ in sum_for_number_in_list:
    print(_)
