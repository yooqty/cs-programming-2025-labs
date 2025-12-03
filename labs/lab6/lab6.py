#1
initial = input('Введите величину времени, исходную единицу измерения и единицу измерения, в которую нужно перевести (через пробел): ')
goo = initial.split(' ')
if goo[1] == 's' and goo[2] == 'm': print(str(float(goo[0])/60) + 'm')
if goo[1] == 's' and goo[2] == 'h': print(str(float(goo[0])/3600) + 'h')
if goo[1] == 'm' and goo[2] == 's': print(str(float(goo[0])*60) + 's')
if goo[1] == 'm' and goo[2] == 'h': print(str(float(goo[0])/60) + 'h')
if goo[1] == 'h' and goo[2] == 's': print(str(float(goo[0])*3600) + 's')
if goo[1] == 'h' and goo[2] == 'm': print(str(float(goo[0])*60) + 'm')
if goo[1] == 'h' and goo[2] == 'h': print(str(float(goo[0])) + 'h')
if goo[1] == 'm' and goo[2] == 'm': print(str(float(goo[0])) + 'm')
if goo[1] == 's' and goo[2] == 's': print(str(float(goo[0])) + 's')


#2
a = float(input('Вклад в банке в размере: '))
n = float(input('Срок: '))
deprate = 0
deprate3 = 3
deprate46 = 5
deprate6 = 2
profit = 0
every10deprate = 0

if a < 30000: print('Минимальный вклад - 30 000 рублей!')

elif a >= 30000:
    every10deprate += ((a+profit)//10000) * 0.3
    if every10deprate <= 5: deprate += ((a+profit)//10000) * 0.3
    elif every10deprate >= 5: deprate += 5

    if n <= 3:
        for i in range(int(n)):
            anew = a + profit
            profit += anew*(deprate3+deprate)/100

    elif n >= 4 and n <= 6:
        for i in range(3):
            anew = a + profit
            profit += anew*(deprate3+deprate)/100
        for i in range(int(n)-3):
            anew = a + profit
            profit += anew*(deprate46+deprate)/100
    
    elif n > 6:
        for i in range(3):
            anew = a + profit
            profit += anew*(deprate3+deprate)/100
        for i in range(3):
            anew = a + profit
            profit += anew*(deprate46+deprate)/100
        for i in range(int(n)-6):
            anew = a + profit
            profit += anew*(deprate6+deprate)/100

print(round(profit, 2))


#3
die = input('Введите начало и конец диапазона(через пробел): ')
startend = die.split(' ')

def isprime(n):
    d = 2
    while n % d != 0:
        d+=1
    return d == n

if startend[0].isdigit() == False or startend[1].isdigit() == False: print('Ошибка! Было введено не число!')

primes = []

if startend[0].isdigit() == True and startend[1].isdigit() == True:
    if int(startend[0]) > int(startend[1]): print('Ошибка! Начало больше конца!')
    elif (int(startend[0]) < int(startend[1])):
        if int(startend[0]) != 1:
            for i in range(int(startend[0]), int(startend[1])+1):
                if isprime(i) == True:
                    primes.append(i)
                i+=1
        else:
            for i in range(2, int(startend[1])+1):
                if isprime(i) == True:
                    primes.append(i)
                i+=1

        print(primes)


#4
import numpy as np
nn = int(input('Введите размер матрицы: '))

if nn < 3: print('Слишком маленький размер!')

if nn > 2:
    m1 = []
    m2 = []

    for i in range(nn):
        string = input('Введите строку первой матрицы: ')
        mat = string.split(' ')
        if len(mat) != nn:
            print('Неверная длина!')
            break
        if len(mat) == nn:
            matint = []
            for i in mat:
                matint.append(int(i))
            m1.append(matint)

    for i in range(nn):
        string = input('Введите строку второй матрицы: ')
        mat = string.split(' ')
        if len(mat) != nn: 
            print('Неверная длина!')
            break
        if len(mat) == nn:
            matint = []
            for i in mat:
                matint.append(int(i))
            m2.append(matint)

if len(m1) == nn and len(m2) == nn:
    matrix1 = np.array(m1)
    matrix2 = np.array(m2)

    print(matrix1 + matrix2)


#5
s = input('Введите строку: ')

ss = s.replace(' ', '').lower()

if ss == ss[::-1]: print('Да')
else: print('Нет')