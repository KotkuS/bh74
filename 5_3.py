# Вывести четные числа от 2 до N по 5 в строку
n = 2
max_n = int(input("Enter max: "))
s = []
st = ''
while max_n >= n:
    if n % 2 == 0:
        s.append(str(n))
    n += 1
    while len(s) >= 5:
        st = ",".join(s[:5])
        del s[:5]
        print(st)
st = ",".join(s)
print(st)
