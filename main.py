# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

my_list = []
i = 0
while i < 10:
    my_list.append(random.randint(0, 10))
    i += 1
print(my_list)
sum = 0
for i in my_list[::2]:
    sum += i
print(sum)