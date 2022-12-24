# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def getKoeff(strKoef):
    pos = str(strKoef).find("*x")
    if pos > 0:
        resK = str(strKoef)[0:pos] 
    else:
        resK = strKoef
    return resK

def getStepen(strKoef):
    posStp = str(strKoef).find("x**")
    pos = str(strKoef).find("*x")
    if posStp > 0:
        resSt = str(strKoef)[posStp+3:] 
    elif posStp < 0 and pos > 0:
        resSt = '1'
    else:
        resSt = '0'
    return resSt

def getListKoeff(inpt):
    global list_no
    list_t = inpt.split(" ")
    list_res = []
    for i in list_t:
        if i not in list_no:
            list_res.append(i)
    return list_res

def getDictKoeff(list_in):
    dict_res = dict()
    for i in range(len(list_in)):
        dict_res[int(getStepen(list_in[i]))] = int(getKoeff(list_in[i]))
    return dict_res

# читаем первый файл
f1 = open("file_1.txt", "r")
ur1 = f1.readline()
f1.close
print("    Многочлен 1: ", ur1)

# читаем второй файл
f2 = open("file_2.txt", "r")
ur2 = f2.readline()
f2.close
print("    Многочлен 2: ", ur2)

# сформируем список лишних символов
list_no = ["0","+","-","="]

# получим список элементов для первого многочлена без лишних символов
list_1a = getListKoeff(ur1)

# получим список элементов для второго многочлена без лишних символов
list_2a = getListKoeff(ur2)

# сформируем словарь "степень:значение коэффициента" для первого многочлена
dict_1b = getDictKoeff(list_1a)

# сформируем словарь "степень:значение коэффициента" для второго многочлена
dict_2b = getDictKoeff(list_2a)

# сформируем множество объединения всех ключей обоих словарей
set_keys = dict_1b.keys() | dict_2b.keys()

# сформируем и отсортируем список всех присутствующих степеней в итоговом многочлене
list_keys = []
for i in set_keys:
    list_keys.append(i)
list_keys.sort()
list_keys.reverse()

# сформируем словарь "степень:значение коэффициента" для итогового многочлена как сумму двух исходных
list_res = dict()
for i in list_keys:
    list_res[i] = dict_1b.get(i, 0) + dict_2b.get(i, 0)

# сформируем строку итогового многочлена
strRes = ""
for i in list_keys:
    if i > 1:
        strRes += str(list_res.get(i)) + "*x**" + str(i)
    elif i == 1:
        strRes += str(list_res.get(i)) + "*x"
    elif i == 0:
        strRes += str(list_res.get(i))
    strRes += " + "
strRes = strRes[:-3:]
strRes += " = 0"
print("Многочлен суммы: ", strRes)

# запишем итоговую строку в файл
f = open("file_res.txt", "w")
f.write(strRes)
f.close