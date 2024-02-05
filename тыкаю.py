# a = 5
# if a > 0:
#     print("a is positive")
# elif a == 0:
#     print("a is 0")
# elif a < 0:
#     print("a is not positive")
#
# is_human = False
# if not is_human:
#     ...
# a = 5
# if a % 2:
#     is_even = "No"
# else:
#     is_even = "Yes"
# is_even = "No" if a % 2 else "Yes"
# a = 1234
# if isinstance(a, str) and a.isdigit():
#     ...
# print(isinstance("wrr", int | float))
# a = 2
# if isinstance(a, int) and not isinstance(a, bool):
#     print("a is int, a is not bool")
# city = "Minsk"
# user = {}
# user["city"] = city or "Mogilev"
# print(user)
# for i in text:
#     print(i.upper())
# text = "Hello"
# for i in enumerate(text):
#     print(i)
# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print("Finish!")
# i = 0
# while i < 5:
#     i += 1
#     print(i)
# text = input("Введите число:")
# while not text.isdigit():
#     text = input("Вы ввели не число! Введите число:")
# print("Ваше число:", text)
# data = {
#     "key1": "value1",
#     "key2": "value2",
# }
# objs = ["AB", "CD2", "EF34", "GH"]
# for i, j, *k in objs:
# #     print(i, j, k)
# for _ in range(5):
#      print("Hello")
# text = input("Enter sent:")
# a = []
# for i in text:
#     a = [",".join(i.upper())]
#     print(a)
# text = input("Enter sent:")
# a = []
# for i in text:
#     if i.isalpha():
#        a.append(i.upper())
# print(a)
# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except (ValueError, ZeroDivisionError) as e:
#     print(e)
# else:
#     print("not exception")
# try:
#     a = int(input())
# finally:
#     print("Always")
# raise ValueError("some text")
# status_code = {
#     200: "OK",
#     201: "CREATED",
#     202: "ACCEPTED",
# }
# print(status_codes.get(status_code, "ERROR"))
