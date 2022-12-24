    # Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
    # Пример:
    # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Введите натуральное число степени k: "))
list_num = [random.randint(0,100) for i in range(k+1)]
print(list_num)

str_ur= ""
for i in range(k,0,-1):
    if i > 1:
        str_ur += str(list_num[i]) + "*x**" + str(i) + " + "
    else:
        str_ur += str(list_num[i]) + "*x"

if list_num[0] != 0:
    str_ur += " + " + str(list_num[0]) + " = 0"
else:
    str_ur += " = 0"

f = open("file_0.txt", "w")
f.write(str_ur)
f.close

print(str_ur)