#1
name = input('Введите имя: ')
age = input('Введите возраст: ')
h = 1
while h <= 10:
    print(f'Меня зовут {name} и мне {age} лет.')
    h+=1

#2
num = input('Введите число от 1 до 9: ')
hi = 1
while hi <= 10:
    g = int(num)*hi
    print(str(num) + '*' + str(hi) + '=' + str(g))
    hi+=1

#3
for ij in range(0,101,3):
    print(ij)

#4
numm = int(input('Введите число: '))
f = 1
while numm > 1:
    f = f * numm
    numm = numm - 1
print('Факториал числа: ' + str(f))

#5
l = 20
while l >= 0:
    print(l)
    l-=1

#6
nun = int(input('Введите число: '))
f1 = 1
f2 = 1
k = 0
sum = 1
print(sum)
while k < nun-2:
    if sum <= nun:
        print(sum)
    sum = f1+f2
    f1 = f2
    f2 = sum
    k+=1

#7
s = input('Введите строку: ')
ns = ''
for j, c in enumerate(s):
    ns += c + str(j+1)
print(ns)

#8
while True:
    nunn = input('Введите два числа через пробел: ')
    gh = nunn.split(' ')
    print('Сумма чисел: ' + str(int(gh[0]) + int(gh[1])))