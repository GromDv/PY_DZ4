# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите натуральное число N: "))

def isSimple(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def isMultiplyer(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

def getMultiplyers(num):
    global list_simple
    if num < 2:
        return
    else:
        for i in list_simple:
            if(isMultiplyer(num, i)):
                list_mult.append(i)
                getMultiplyers(num / i)
                break

list_simple = []
for i in range(2,n+1):
    if(isSimple(i)):
        list_simple.append(i)
# print(list_simple)
if n in list_simple:
    print("Это простое число, у него нет множителей!")
else:
    list_mult = []
    getMultiplyers(n)
    print("Простые множители для него: ", list_mult)
    

