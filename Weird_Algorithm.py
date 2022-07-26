# I
# n = int(input())

# res = []
# while n != 1:
#     for i in range(n):
#         if n % 2 == 0:
#             n = n // 2 # !!!
#             res.append(n)
#         elif n % 2 == 1:
#             n = n*3 + 1
#             res.append(n)
#         elif n == 1:
#             break
#     print(*res)


# II
# n = int(input())

# res = [n]
# while n != 1:
#     for i in range(n):
#         if n % 2 == 0:
#             n = n // 2 # !!!
#             res.append(n)
#         else:
#             n = n*3 + 1
#             res.append(n)
#     print(*res)

    # 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
    # Loop infinito: 4 2 1 4 2 1 4 2 1 ... >> não tá parando no 1?


# III :
# n = int(input())

# res = []

# i = 1
# while i != 0:
#     for i in range(n):
#         if n % 2 == 0:
#             n = n // 2
#             res.append(n)
#         elif n % 2 == 1:
#             n = n*3 + 1
#             res.append(n)
#         elif n == 1:
#             i -= 1
#     print(*res)
# Note: p/ o Input 5 o resultado foi: 5 \n 16 8 4 2 1 \n 16 8 4 2 1 4

# IV:
n = int(input())

res = [n]
while n != 1:
    #tava usando um for sem necessidade aqui, talvez fosse isso
    if n % 2 == 0:
        n = n // 2
        res.append(n)
    elif n % 2 == 1:
        n = n*3 + 1
        res.append(n)
    elif n == 1:
        break
print(*res)