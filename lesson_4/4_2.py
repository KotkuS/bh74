text = input("Введите текст:")
little = text.lower()
little = "".join(x for x in little if x.isalpha())
little.split()
dict_ = {i: little.count(i) for i in little}
for key, value in dict_.items():
    print(key, " = ", value)
