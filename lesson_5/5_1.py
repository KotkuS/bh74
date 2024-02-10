# Вывести первые N цисел кратные M и больше K
i = 0
M_krat = 2
N_count = 0
K_min = 1
# a = []
# for n in range(i, 100000000):
#         if n > K_min and n % M_krat:
#             while N_count < 5:
#                 i += M_krat
#                 N_count += 1
#                 print(i)
#         elif n < K_min and n % M_krat:
#             while n < K_min:
#                 n += 1
#         elif n > K_min and not n % M_krat:
#             while not n % M_krat:
#                 n += 1
while N_count < 6:
    while i < K_min and i % M_krat != 0:
        i += 1
        print(i)
    N_count += 1
    