# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


#
# my_list = []
# i = 0
# while i < 10:
#     my_list.append(random.randint(0, 10))
#     i += 1
# print(my_list)
# sum = 0
# for i in my_list[::2]:
#     sum += i
# print(sum)
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# # [2, 3, 5, 6] => [12, 15]
# def get_solv_idx(my_list):
#     list_solved = []
#     for i in range(my_list):
#         solved = my_list[i] * my_list[-i]
#         list_solved.append(solved)
#     return list_solved

def get_random_list(range):
    my_list = []
    i = 0
    while i < range:
        my_list.append(random.randint(1, 10))
        i += 1
    return my_list


# my_list = get_random_list(int(input('Введите длину списка: ')))
# print(my_list)
def get_solv_idx(my_list):
    solv_list = []
    if len(my_list) % 2 == 0:
        for i in range(len(my_list) // 2):
            solved = my_list[i] * my_list[-i - 1]
            solv_list.append(solved)
    else:
        for i in range(len(my_list) // 2 + 1):
            solved = my_list[i] * my_list[-i - 1]
            solv_list.append(solved)
    return solv_list


# print(get_solv_idx(my_list))
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = []
i = 0
while i < 10:
    my_list.append(round(random.uniform(0, 10), 10))
    i += 1
print(my_list)
for i in range(len(my_list)):
    my_list[i] = my_list[i] - int(my_list[i])
print(my_list)
print(f'Разница максимальной дробной частью {max(my_list)} и минимальной {min(my_list)} равна: {max(my_list)-min(my_list)}')
