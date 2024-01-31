text1 = input("Введите первое число:")
text2 = input("Введите второе число:")
text3 = input("Введите третье число:")
number1 = float(text1)
number2 = float(text2)
number3 = float(text3)
numbers = [number1, number2, number3]
average = sum(numbers)/len(numbers)
print("Среднее арифметическое равно:", round(average, 3))
