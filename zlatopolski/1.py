# 1.1.	 Вывести на одной строке числа 31, 18 и  79 с  одним пробелом между ними. Текст '31 18 79' не использовать.
# 1.2.	 Вывести на одной строке числа 47, 52 и  150 с двумя пробелами между ними. Текст '47 52 150' не использовать.
# 1.3.	 Вывести на экран числа 50 и  10 одно под другим.
# 1.4.	 Вывести на экран числа 5, 10 и  21 одно под другим.
# a = ["13", "71", "19"]
# print(" ".join(a))
# print("  ".join(a))
# print("50\n", "10", sep="")
# print("5\n", "10\n", "21\n", sep="")
# 1.6.	 Число π примерно равно 3,1415926. Вывести на экран это
# число с тремя цифрами в дробной части. Текст '3.142' не использовать.
# 1.7.	 Число e (основание натурального логарифма) приблизительно равно 2,71828.
# Вывести на экран это число с  точностью до десятых. Текст '2.7' не использовать.
# from math import pi, e
# print(round(pi, 3))
# print(round(e, 1))
# 1.8.	 Составить программу вывода на экран числа, вводимого
# с  клавиатуры. Выводимому числу должно предшествовать сообщение «Вы ввели число».
# 1.9.	 Составить программу вывода на экран числа, вводимого
# с клавиатуры. После выводимого числа должно следовать сообщение «– вот какое число Вы ввели».
# print("Вы ввели число:", input())
# print(input(), "- вот такое число вы вывели")
# 1.10.	 Составить программу, которая запрашивает имя человека
# и  повторяет его на экране.
# 1.11.	 Составить программу, которая запрашивает название
# футбольной команды и  повторяет его на экране со словами «–
# это чемпион!»
# n = input("Enter your name:")
# print(n)
# m = input("Enter football team name:")
# print(m, "- is a champion")
# 1.12.	 Напишите программу, в которую вводится имя человека
# и выводится на экран приветствие в виде слова «Привет», после
# которого должна стоять запятая, введенное имя и восклицательный знак.
# После запятой должен стоять пробел, а  перед восклицательным знаком пробела быть не должно.
# name = input("Enter your name:")
# print(f"Hello, {name}!")
# 1.13.	 Напишите программу, в  которую вводится целое число,
# после чего на экран выводится следующее и  предыдущее целое
# число.
# number = int(input("Enter a number:"))
# print((number + 1), (number - 1))
# 1.14.	 Составить программу вывода на экран в одну строку трех
# любых чисел, вводимых с клавиатуры, с двумя пробелами между
# ними.
# n1 = input()
# n2 = input()
# n3 = input()
# print(n1, n2, n3, sep="  ")
# 1.15.	 Составить программу вывода на экран в одну строку четырех любых чисел, вводимых с  клавиатуры,
# с  одним пробелом между ними.
# n1 = input()
# n2 = input()
# n3 = input()
# n4 = input()
# print(n1, n2, n3, n4, sep=" ")
# 1.16.	 Составить программу вывода на экран следующей информации:
# а) 5 10 б) 100 t в) x 25
# 7 см 1949 v x y
# t = int(input("Enter t:"))
# v = int(input("Enter v:"))
# x = int(input("Enter x:"))
# print("a) 5 10\t\t b) 100 ", t, "\t\t v) ", x, " 25\n 7sm \t\t 1949 ", v, "\t\t\t ", x, " ", v, sep="")
# 1.17.	 Составить программу вывода на экран следующей информации:
# а) 2 кг   б) а 1   в) x y
# 13 17     19 b      5 y
# a = input()
# x = input()
# y = input()
# b = input()
# print("a) 2kg \t\t b) ", a, " 1\t\t v) ", x, " ", y, "\n13 17\t\t\t 19 ", b, "\t\t\t 5", y)
