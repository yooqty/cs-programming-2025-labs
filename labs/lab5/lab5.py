#1
kitty = [1, 50, 58, 3, 67, 4, 6, 93, 19, 49]
print(kitty)
index_of_3 = kitty.index(3)
kitty[index_of_3] = 30
print(kitty)

#2
doggy = [2, 3, 4, 5, 6]
print(doggy)
length = len(doggy)
i=0
for i in range(length):
    doggy[i] = doggy[i]**2
    i+=1
print(doggy)

#3
huggy = [45, 4868, 29, 6699, 247, 90, 1, 2, 56, 9437, 7]
huggy.sort()
print(huggy[-1]/len(huggy))

#4
collar = (357, 9, 18, 496)
collar = sorted(collar)
print(collar)

#5
shop_items = {
    'киви': 50,
    'банан': 40,
    'свекла': 60,
    'арбуз': 100
}
min_shop_key = min(shop_items, key=shop_items.get)
max_shop_key = max(shop_items, key=shop_items.get)
print('Товар с минимальной ценой: ' + min_shop_key)
print('Товар с максимальной ценой: ' + max_shop_key)

#6
jjba = ['night owl', 'ILE', 'sp7']
print(dict(zip(jjba, jjba)))

#7
en_dict = {
    'crucifix': 'распятие',
    'bludgeon': 'дубинка',
    'blister': 'волдырь',
    'cockpit': 'кабина пилота',
    'bootleg': 'контрабандный'
}
reversed_en_dict = {
    value: key
    for key, value
    in en_dict.items()
}
ru = input('Введите слово на русском для перевода: ')
print('Перевод слова ' + ru + ': ' + reversed_en_dict[ru])

#8
import random
game = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
user_input = input('Ввод (камень/ножницы/бумага/ящерица/спок): ')
random_item = random.choice(game)
print('Пользователь: ' + user_input + ', ' + 'Программа: ' + random_item)
if user_input == 'ножницы' and random_item == 'бумага': print('Ножницы режут бумагу! Пользователь победил!')
if random_item == 'ножницы' and user_input == 'бумага': print('Ножницы режут бумагу! Программа победила!')
if user_input == 'бумага' and random_item == 'камень': print('Бумага покрывает камень! Пользователь победил!')
if random_item == 'бумага' and user_input == 'камень': print('Бумага покрывает камень! Программа победила!')
if user_input == 'камень' and random_item == 'ящерица': print('Камень давит ящерицу! Пользователь победил!')
if random_item == 'камень' and user_input == 'ящерица': print('Камень давит ящерицу! Программа победила!')
if user_input == 'ящерица' and random_item == 'спок': print('Ящерица отравляет Спока! Пользователь победил!')
if random_item == 'ящерица' and user_input == 'спок': print('Ящерица отравляет Спока! Программа победила!')
if user_input == 'спок' and random_item == 'ножницы': print('Спок ломает ножницы! Пользователь победил!')
if random_item == 'спок' and user_input == 'ножницы': print('Спок ломает ножницы! Программа победила!')
if user_input == 'ножницы' and random_item == 'ящерица': print('Ножницы обезглавливают ящерицу! Пользователь победил!')
if random_item == 'ножницы' and user_input == 'ящерица': print('Ножницы обезглавливают ящерицу! Программа победила!')
if user_input == 'ящерица' and random_item == 'бумага': print('Ящерица съедает бумагу! Пользователь победил!')
if random_item == 'ящерица' and user_input == 'бумага': print('Ящерица съедает бумагу! Программа победила!')
if user_input == 'бумага' and random_item == 'спок': print('Бумага подставляет Спока! Пользователь победил!')
if random_item == 'бумага' and user_input == 'спок': print('Бумага подставляет Спока! Программа победила!')
if user_input == 'спок' and random_item == 'камень': print('Спок испаряет камень! Пользователь победил!')
if random_item == 'спок' and user_input == 'камень': print('Спок испаряет камень! Программа победила!')
if user_input == 'камень' and random_item == 'ножницы': print('Камень разбивает ножницы! Пользователь победил!')
if random_item == 'камень' and user_input == 'ножницы': print('Камень разбивает ножницы! Программа победила!')
if random_item == 'камень' and user_input == 'камень': print('Ничья!')
if random_item == 'ножницы' and user_input == 'ножницы': print('Ничья!')
if random_item == 'бумага' and user_input == 'бумага': print('Ничья!')
if random_item == 'ящерица' and user_input == 'ящерица': print('Ничья!')
if random_item == 'спок' and user_input == 'спок': print('Ничья!')

#9
words = ['раскалывать', 'ящерица', 'мангус', 'бегемот', 'рысь']
def create_dict(words):
    frost = {}
    for word in words:
        first_letter = word[0]
        if first_letter in frost: frost[first_letter].append(word)
        else: frost[first_letter] = [word]
    return frost
print(create_dict(words))

#10
students = [
    ('Алиса', [2,2,2]),
    ('Даша', [5,5,5]),
    ('Денис', [3,2,2])
]
labubu = {
    student: sum(grades) / len(grades)
    for student, grades in students
}
max_avg = max(labubu, key=labubu.get)
print(max_avg + ' имеет наивысший средний балл: ' + str(labubu.get(max_avg)))