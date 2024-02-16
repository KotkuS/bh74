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


# print(alphabet_position("The sun is fun"))
# class User:
#     def __init__(self, first_name: str, email: str) -> None:
#         self.first_name = first_name.title()
#         self.email = email.lower()
#
#     def __str__(self) -> str:
#         return f"User first_name={self.first_name} email={self.email}"
#
#
# class Manager(User):
#     ...
#
#
# vasya = Manager("vasya", "saf@fdgf")
# print(vasya)
#
# class B:
#     ...
#
# class C:
#     def __init__(self, b: B):
#         self.obj = b
#
# class A:
#     i: int = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def foo(self):
#          return self.name.upper()
#
#
# class N(A):
#     _i: int = 5

#     def foo(self):
#         result = super().foo()
#         return result
#
#
# b = N(name="name")
# print(b._i)
# class Debcard():
#     number = 123456789101112
#     def __init__(self, number):
#         self.__number = number
#     @property
#     def get_number(self):
#         return self.__number[-4:]
#
#     @get_number.setter
#     def get_number(self, value: str):
#         if len(value) == 16:
#             self.__number = value
#             return self.__number
#
#
# card1 = Debcard(123456789101112)
# print(card1.get_number)
# from dataclasses import dataclass
#
# @dataclass(frozen=True)
# class User:
#     name: str
#     email: str
#
from abc import ABC, abstractmethod
#
# class AbstractView(ABC):
#     @abstractmethod
#     def get(self, request):
#         ...
#     def post(self, request):
#         ...
#
# class ListView(AbstractView):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass
#     @classmethod
#     def dispatch(cls, request):
#         pass


class AbstarctPhone(ABC):
    @abstractmethod
    def call(self):
        pass


class SMSMixin:
    def sms(self):
        ...


class MobilePhone(AbstarctPhone, SMSMixin):
    def call(self):
        pass

    def sms(self):
        pass


class StaticPhone(AbstarctPhone):
    def call(self):
        pass
    