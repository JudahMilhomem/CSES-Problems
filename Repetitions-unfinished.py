# Try number 1:
# n = input()
# #ex.: AATTTGGCTAGCCTTA

# sequence = list(n) #Separar cada caractere da sequência e adicioná-los a uma lista, na ordem
# ##Fazer a comparação para cada posição com a posição seguinte
# count = 1
# repetitions = []
# for p in range(len(sequence)-1):
#     if sequence[p] == sequence[p+1]: #Se for a mesma letra, 
#         count += 1 #adicionar um a um contador (que já começa com um*)
#     elif sequence[p] == sequence[p+1]: #Se forem letras diferentes,
#         repetitions.append(count) # adicionar o valor atual do contador a uma segunda lista,
#         count = 0 #e depois zerar a contagem
# print(repetitions)
# #Printar o maior valor da segunda lista


n = input()
#ex.: AATTTGGCTAGCCTTA

sequence = list(n)
count = 1
repetitions = []



for p in range(len(sequence)-1):
    if sequence[p] == sequence[p+1]:
        count += 1
    elif sequence[p] != sequence[p+1]:
        repetitions.append(count)
        count = 1

repetitions.sort(reverse = True)
print(repetitions[0])