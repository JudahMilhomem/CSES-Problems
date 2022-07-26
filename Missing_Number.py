# First Try
# Input:
# n = int(input()) #line 1
# numbers = list(map(int, input().split())) #line 2
# numbers.sort()

# for i in range(1,n+1):
#     if i != 1 and numbers[i] - numbers[i - 1] != 0:
#         missing_number = i + 1
# print(missing_number)


# II
# Input n:
n = int(input())
# Input list of numbers::
between = map(int, input().split())

sumA = 0
sumB = 0
for correct in range(1,n+1):
    sumA += correct
for missing in list(between):
    sumB += missing

missing_number = sumA - sumB
print(missing_number)