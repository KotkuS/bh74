indict = {}
a = indict.setdefault("name", input("Введите имя:"))
b = indict.setdefault("email", input("Введите почту:"))
dict_ = {n: indict for n in range(0, 3)}
print(dict_)
