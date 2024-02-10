# Пользователь вводит химическую формулу (элементы однобуквенныe и формула без скобок)
# Подсчитать количество молекул
# input: C2H5OH
# output: {"C": 2, "H": 6, "O": 1}
formula = list(input("Введите химическу формулу: "))
formula_dict = {}
alphas = []
for elms in formula:
    while elms.isalpha():
        alphas.append(elms)
print(alphas)
