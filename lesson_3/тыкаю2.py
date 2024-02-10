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
