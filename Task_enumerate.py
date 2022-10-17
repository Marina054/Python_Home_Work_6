# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


print('Введите число:')
num_list =list(input())
print(num_list)
sum_dig = 0
for i in range(len(num_list)):
    if num_list[i] == '.':
        continue
    sum_dig += int(num_list[i])
print("сумма:",sum_dig)
for i, val in enumerate(num_list, start = 1):
    print(f'№ {i} => {val}')