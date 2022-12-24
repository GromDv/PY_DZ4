# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list_num = [random.randint(0,10) for i in range(100)]
print(list_num)
print(set(list_num))