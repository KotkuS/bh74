# def length(a):
#     count = 0
#     for _ in a:
#         count += 1
#     return count
#
#
# text = "Hello world"
# c = length(a=text)
# print(c)
# def foo(a, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     print(b)
# foo(4)
# def baz(*args):
#     print(args)
# def foo2(**kwargs):
# print(kwargs)
# def key(a):
#     if isinstance(a, int, float):
#         return a
#     elif isinstance(a, str):
#         return int(a)
#
#
# objs = [3, 5, "4", 6, "-23", -45]
# # objs.sort(key=key)
# # print(objs)
# objs.sort(key=lambda a: a if isinstance(a, (int, float)) else int(a))
# def foo(a: list, **kwargs: int):
#     ...
# data: dict[str, dict[str, str]] = {
#
# }
# def bar():
#     ...
#
# print(bar.__annotations__)
# def func(a, b):
#     return int(a) * int(b)
#
#
# numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# m = map(func, numbers, numbers)
# for i in m:
#     print(i)
# objs = [2, 4, -5, 6, -23, 5, 3, -5, 7, 54, 7]
# f = filter(lambda x: x > 0, objs)
# for i in f:
#     print(i)
#
# text = "Hello world"
# objs = [True, False, None]
# s = (4, 7, 2, 5)
# # z = zip(text, objs, s)
# # for i in z:
# #     print(i)
# from  itertools import zip_longest
#
# a = zip_longest(text, objs, s, fillvalue="N/A")
# for i in a:
#     print(i)
# def my_range(start, stop, step):
#     numbers = []
#     for i in range(start, stop, step):
#         yield i
#
# a = my_range(1, 10, 2)
# print(next(a))
# text = "Hello"
# b = (i for i in text)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# def decorator(a):
#     def wrapper(b):
#         return a * b
#
#     return wrapper
#
#
# d = decorator(4)
# print(d(2))
# if i == "1":
#     i = 1
#     l.insert(-1, i)
# elif i == "2":
#     i = 2
# elif i == "3":
#     i = 3
# elif i == "4":
#     i = 4
# elif i == "5":
#     i = 5
# elif i == "6":
#     i = 6
# elif i == "7":
#     i = 7
# elif i == "8":
#     i = 8
# elif i == "9":
#     i = 9
# elif i == "0":
#     i = 0
# class User:
#     def __init__(self, name, email, password, age):
#         self.name = name
#         self.password = password
#         self.email = email
#         self.is_active = False
#         self.age = age
#
#     def __str__(self):
#         return f"name={self.name}"
#
#     def __bool__(self):
#         return self.is_active
#
#     def __int__(self):
#         return self.age ** 2
#
#
# user1 = User(name="vasya", email="email", password="1", age=3)
#
# print(int(user1))

# def alphabet_position(text):
#     alphabet = {
#         "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
#         "h": 8, "i": 9, "j": 10, "k": 11, "l": 11, "m": 12, "n": 13,
#         "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
#         "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,
#     }
#     for symbol in text:
#         if symbol.lower() == alphabet.keys():
#             new_symbol = alphabet.get(symbol)
#             print(new_symbol)
#         if not symbol.isalpha:
#             continue
#
#     pass


print(alphabet_position("The sun is fun"))
