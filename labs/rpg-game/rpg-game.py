print('='*100)
print('Добро пожаловать в игру «FEMBOY ALFA ORK DUNGEON»!')
print('='*100)

# check if int
import sys
def is_int(x):
    try:
        int(x)
    except ValueError:
        print('Должно быть введено ЦЕЛОЕ ЧИСЛО!!!!!!')
        sys.exit()


# class selection
classes = ['Фембойчик инкуб', 'Эльфийка', 'Альфа оборотень', 'Кошкодевочка']
print('Выбор класса')
print('='*100)
for i in range(len(classes)):
    print(f'{i+1}. {classes[i]}')
print('='*100)
class_choice = input(f'Выберите кем вы хотите быть (введите целое число от 1 до {len(classes)}): ')

# check if the entered data is valid
is_int(class_choice)
if (int(class_choice) > len(classes)) or (int(class_choice) < 1):
    print(f'ОТ 1 ДО {len(classes)}!!!!!')
    sys.exit()


# class choice
your_class = classes[int(class_choice)-1]

import random

if your_class == 'Фембойчик инкуб':
    stats = {'MaxHP': random.randint(10,13),
              'ATK': random.randint(2,3),
              'DEF': random.randint(1,3),
              'Agility': random.randint(7,8),
              'Height': random.randint(150,155),
              'Weight': random.randint(35,40),
              'Weapon': 'Отсутствует',
              'Armor': 'Отсутствует'}
if your_class == 'Эльфийка':
    stats = {'MaxHP': random.randint(10,14),
              'ATK': random.randint(1,3),
              'DEF': random.randint(3,4),
              'Agility': random.randint(5,7),
              'Height': random.randint(160,165),
              'Weight': random.randint(45,50),
              'Weapon': 'Лук',
              'Armor': 'Легкая броня'}
if your_class == 'Альфа оборотень':
    stats = {'MaxHP': random.randint(15,20),
              'ATK': random.randint(5,8),
              'DEF': random.randint(8,10),
              'Agility': random.randint(2,3),
              'Height': random.randint(185,190),
              'Weight': random.randint(90,100),
              'Weapon': 'Клыки',
              'Armor': 'Средняя броня'}
if your_class == 'Кошкодевочка':
    stats = {'MaxHP': random.randint(10,15),
              'ATK': random.randint(4,5),
              'DEF': random.randint(1,2),
              'Agility': random.randint(7,9),
              'Height': random.randint(155,160),
              'Weight': random.randint(40,45),
              'Weapon': 'Когти',
              'Armor': 'Отсутствует'}

if stats['Armor'] == 'Легкая броня':
    stats['DEF'] += 2
if stats['Armor'] == 'Средняя броня':
    stats['DEF'] += 4
if stats['Weapon'] != 'Отсутствует':
    stats['ATK'] += 2



print('='*100)
print(f'Вы - {your_class}!')
print('='*100)
print('Ваши характеристики: ')
print(f'HP - {stats['MaxHP']}')
print(f'ATK - {stats['ATK']}')
print(f'DEF - {stats['DEF']}')
print(f'Agility - {stats['Agility']}')
print(f'Height - {stats['Height']}')
print(f'Weight - {stats['Weight']}')
print(f'Weapon - {stats['Weapon']}')
print(f'Armor - {stats['Armor']}')

print('='*100)

if your_class == 'Фембойчик инкуб':
    print('Особая способность Фембойчика инкуба - Соблазнить!')
    print('Фембойчик инкуб может соблазнить противника!')
    print('Шанс успеха - 50%!')
    print('Когда Фембойчик инкуб встречается с Орком или Бесом, шанс успеха возрастает до 100%!')
    print('Когда Фембойчик инкуб встречается с Бобром, шанс успеха снижается до 0%!')
if your_class == 'Эльфийка':
    print('Особая способность Эльфийки - Запугать!')
    print('Эльфийка может запугать противника!')
    print('Шанс успеха - 50%!')
    print('Когда Эльфийка встречается с Бобром, шанс успеха возрастает до 100%!')
    print('Когда Эльфийка встречается с Ведьмой, шанс успеха снижается до 0%!')
if your_class == 'Альфа оборотень':
    print('Особая способность Альфа оборотня - Выть!')
    print('Альфа оборотень может издать вой, который полностью уничтожает врага!')
    print('Шанс успеха - 50%!')
    print('Когда Альфа оборотень встречается с Бобром, шанс успеха возрастает до 100%!')
    print('Когда Альфа оборотень встречается с Ведьмой, шанс успеха снижается до 0%!')
if your_class == 'Кошкодевочка':
    print('Особая способность Кошкодевочки - Умилить противника!')
    print('Кошкодевочка может сбежать с поля боя!')
    print('Шанс успеха - 50%!')
    print('Когда Кошкодевочка встречается с Орком или Бобром, шанс успеха возрастает до 100%!')
    print('Когда Кошкодевочка встречается с Ведьмой, шанс успеха снижается до 0%!')

print('='*100)



# opponents
opponents = ['Орк', 'Ведьма', 'Бобр', 'Бес']

orc_stats = {'MaxHP': random.randint(15,20),
              'ATK': random.randint(1,2),
              'DEF': random.randint(4,5),
              'Agility': random.randint(1,2),
              'Height': random.randint(200,250),
              'Weight': random.randint(250,300)}

witch_stats = {'MaxHP': random.randint(10,15),
              'ATK': random.randint(4,5),
              'DEF': random.randint(1,2),
              'Agility': random.randint(4,5),
              'Height': random.randint(160,165),
              'Weight': random.randint(45,50)}

beaver_stats = {'MaxHP': random.randint(2,3),
              'ATK': random.randint(1,2),
              'DEF': random.randint(1,2),
              'Agility': random.randint(5,6),
              'Height': 35,
              'Weight': 30}

imp_stats = {'MaxHP': random.randint(5,6),
              'ATK': random.randint(4,5),
              'DEF': random.randint(2,3),
              'Agility': random.randint(5,6),
              'Height': random.randint(140,145),
              'Weight': random.randint(30,35)}



# inventory
inventory = [0] # first value - number of gold coins
# max number of items in inventory - 5
weapon = [stats['Weapon']]
armor = [stats['Armor']]
MaxHP = stats['MaxHP'] 
hp = stats['MaxHP'] # can only be regenerated via health potions
# defence refreshes after every battle


def Inventory():
    global inventory
    global weapon
    global armor
    global MaxHP
    global hp

    print('='*100)

    # show inventory
    print('Просмотр инвентаря:')
    print(f'Инвентарь - {inventory}')
    print(f'Оружие - {weapon[0]}')
    print(f'Броня - {armor[0]}')
    print('='*100)
    print('1. Закрыть инвентарь')
    print('2. Использовать предмет')
    print('3. Выбросить предмет')
    inventory_choice = input('Что будете делать? ')

    is_int(inventory_choice)
    if (int(inventory_choice) > 3) or (int(inventory_choice) < 1):
        print('ОТ 1 ДО 3!!!!!')
        sys.exit()

    if inventory_choice == '1':
        return

    # use an item
    if inventory_choice == '2':
        print('='*100)

        for i in range(len(inventory)):
            print(f'{i+1}. {inventory[i]}')
        item_choice = input('Выберите предмет для использования (индекс): ')

        #check is the entered data is valid
        is_int(item_choice)
        if (int(item_choice) > len(inventory)) or (int(item_choice) < 1):
            print(f'ОТ 1 ДО {len(inventory)}!!!!!')
            sys.exit()

        if item_choice == '1':
            print('='*100)

            print('Вы не можете использовать золото в данный момент!')
            Inventory()
        if item_choice == '2':
            print('='*100)

            if inventory[1] == {'Зелье здоровья'}:
                if (hp < MaxHP) and ((hp + 2)<=MaxHP):
                    hp += 2
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif (hp < MaxHP) and ((hp + 2)>=MaxHP):
                    hp = MaxHP
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                else:
                    print('Невозможно использовать Зелье здоровья!')
                    print('Ваше здоровье полное!')
                    Inventory()
            if inventory[1] == {'Зелье молодости'}:
                print('Вам нет необходимости использовать Зелье молодости! Вы и так молоды!')
                Inventory()
        if item_choice == '3':
            print('='*100)

            if inventory[2] == {'Зелье здоровья'}:
                if (hp < MaxHP) and ((hp + 2)<=MaxHP):
                    hp += 2
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif (hp < MaxHP) and ((hp + 2)>=MaxHP):
                    hp = MaxHP
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif hp == MaxHP:
                    print('Невозможно использовать Зелье здоровья!')
                    print('Ваше здоровье полное!')
                Inventory()
            if inventory[2] == {'Зелье молодости'}:
                print('Вам нет необходимости использовать Зелье молодости! Вы и так молоды!')
                Inventory()
        if item_choice == '4':
            print('='*100)

            if inventory[3] == {'Зелье здоровья'}:
                if (hp < MaxHP) and ((hp + 2)<=MaxHP):
                    hp += 2
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif (hp < MaxHP) and ((hp + 2)>=MaxHP):
                    hp = MaxHP
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif hp == MaxHP:
                    print('Невозможно использовать Зелье здоровья!')
                    print('Ваше здоровье полное!')
                Inventory()
            if inventory[3] == {'Зелье молодости'}:
                print('Вам нет необходимости использовать Зелье молодости! Вы и так молоды!')
                Inventory()
        if item_choice == '5':
            print('='*100)

            if inventory[4] == {'Зелье здоровья'}:
                if (hp < MaxHP) and ((hp + 2)<=MaxHP):
                    hp += 2
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif (hp < MaxHP) and ((hp + 2)>=MaxHP):
                    hp = MaxHP
                    print('Зелье здоровья успешно использовано!')
                    print(f'Ваше текущее здоровье: {hp}')
                elif hp == MaxHP:
                    print('Невозможно использовать Зелье здоровья!')
                    print('Ваше здоровье полное!')
                Inventory()
            if inventory[4] == {'Зелье молодости'}:
                print('Вам нет необходимости использовать Зелье молодости! Вы и так молоды!')
                Inventory()


    # throw an item away
    if inventory_choice == '3':
        print('='*100)
        for i in range(len(inventory)):
            print(f'{i+1}. {inventory[i]}')
        item_choice = input('Какой предмет хотите выбросить? ')

        is_int(item_choice)
        if (int(item_choice) > len(inventory)) or (int(item_choice) < 1):
            print(f'ОТ 1 ДО {len(inventory)}!!!!!')
            sys.exit()

        if int(item_choice) >= 2:
            print('='*100)

            del inventory[int(item_choice)-1]
            print('Предмет был успешно выброшен!')
            print(f'Ваш текущий инвентарь: {inventory}')
            Inventory()
        else:
            print('='*100)

            inventory[0] = 0
            print('Предмет был успешно выброшен!')
            print(f'Ваш текущий инвентарь: {inventory}')
            Inventory()

#experience
exp = 0
# lvl increases every 5 exp
lvl = 1
points = 0

# experience reset
def exp_reset():
    global exp
    global lvl
    global points
    if exp == 5:
        lvl += 1
        points += 1
        exp = 0

def Upgrades():
    global stats
    global points
    global lvl
    global exp
    print('='*100)
    print(f'На данный момент у вас {points} очков прокачки')
    print('1. Выйти')
    print('2. Перейти к прокачке')
    upgrades_choice = input('Что будете делать? ')

    # check if the entered data is valid
    is_int(upgrades_choice)
    if (int(upgrades_choice) > 2) or (int(upgrades_choice) < 1):
        print(f'ОТ 1 ДО 2!!!!!')
        sys.exit()

    # exit
    if upgrades_choice == '1':
        return

    # upgrade
    elif upgrades_choice == '2':
        print('='*100)

        upgrades = ['+1MaxHP', '+1ATK', '+1DEF', '+1Agility']

        # insufficient points
        if points == 0:
            print('Недостаточно очков прокачки!')
            print(f'Текущее количество - {points}')
            Upgrades()

        # sufficient points
        else:
            print('Выберите характеристику для прокачки: ')
            for i in range(4):
                print(f'{i+1}. {upgrades[i]}')
            upgrade_choice = input('Прокачать: ')
            
            # check if the entered data is valid
            is_int(upgrade_choice)
            if (int(upgrade_choice) > 4) or (int(upgrade_choice) < 1):
                print(f'ОТ 1 ДО 4!!!!!')
                sys.exit()

            if upgrade_choice == '1':
                print('='*100)
                stats['MaxHP'] += 1
                points -= 1
                print('Ваше максимальное здоровье было увеличено на 1!')
                print(f'Текущее максимальное здоровье - {stats['MaxHP']}')
                Upgrades()
            if upgrade_choice == '2':
                print('='*100)
                stats['ATK'] += 1
                points -= 1
                print('Ваша атака была увеличена на 1!')
                print(f'Текущая атака - {stats['ATK']}')
                Upgrades()
            if upgrade_choice == '3':
                print('='*100)
                stats['DEF'] += 1
                points -= 1
                print('Ваша защита была увеличена на 1!')
                print(f'Текущая защита - {stats['DEF']}')
                Upgrades()
            if upgrade_choice == '4':
                print('='*100)

                # not max agility
                if stats['Agility'] < 10:
                    stats['Agility'] += 1
                    points -= 1
                    print('Ваша ловкость была увеличена на 1!')
                    print(f'Текущее ловкость - {stats['Agility']}')
                    Upgrades()

                # max agility
                else:
                    print('Ваша ловкость достигла максимального значения - 10!')
                    print('Дальнейшая прокачка невозможна!')
                    Upgrades()



# rooms
floor = 1
room_count = 0
total_rooms = 0
rooms = ['Боевая комната', 'Комната отдыха', 'Комната с сундуком']

# next floor
def next_floor():
    global floor
    global room_count
    
    if room_count == 10:
        floor += 1

        orc_stats['MaxHP'] += 2
        orc_stats['ATK'] += 2
        orc_stats['DEF'] += 2

        witch_stats['MaxHP'] += 2
        witch_stats['ATK'] += 2
        witch_stats['DEF'] += 2

        beaver_stats['MaxHP'] += 2
        beaver_stats['ATK'] += 2
        beaver_stats['DEF'] += 2

        imp_stats['MaxHP'] += 2
        imp_stats['ATK'] += 2
        imp_stats['DEF'] += 2

        room_count = 0



def directions():
    left = random.choice(rooms)
    right = random.choice(rooms)

    known_or_not_left = [left, 'Тьма темная']
    known_or_not_right = [right, 'Тьма темная']

    print('='*100)
    print('Перед вами развилка')
    print(f'Слева - {random.choice(known_or_not_left)}')
    print(f'Справа - {random.choice(known_or_not_right)}')
    print('1. Налево')
    print('2. Направо')
    direction_choice = input('Куда пойдете? ')

    is_int(direction_choice)
    if (int(direction_choice) > 2) or (int(direction_choice) < 1):
        print(f'ОТ 1 ДО 2!!!!!')
        sys.exit()

    if direction_choice == '1':
        print('='*100)
        print('Вы свернули налево')
        print(f'Слева - {left}')
        if left == rooms[0]:
            battle_room()
        elif left == rooms[1]:
            rest_room()
        elif left == rooms[2]:
            reward_room()

    if direction_choice == '2':
        print('='*100)
        print('Вы свернули направо')
        print(f'Справа - {right}')
        if right == rooms[0]:
            battle_room()
        if right == rooms[1]:
            rest_room()
        elif right == rooms[2]:
            reward_room()

def rest_room():
    print('='*100)

    # room counter
    global floor
    global room_count
    global total_rooms
    room_count+=1
    print(f'ЭТАЖ {floor}')
    print(f'Комната {room_count}')
    print(f'Всего пройдено комнат: {total_rooms}')
    total_rooms += 1
    next_floor()

    print('='*100)

    # rest room
    print('Вы попали в комнату отдыха!')
    print('1. Покинуть комнату отдыха')
    print('2. Прокачка')
    print('3. Открыть инвентарь')
    print('ВНИМАНИЕ!!! Если вы открываете инвентарь или прокачку в комнате отдыха, после их закрытия автоматически следует развилка!')
    rest_room_choice = input('Что будете делать? ')

    # check if the entered data is valid
    is_int(rest_room_choice)
    if (int(rest_room_choice) > 3) or (int(rest_room_choice) < 1):
        print(f'ОТ 1 ДО 3!!!!!')
        sys.exit()


    if rest_room_choice == '1':
        directions()
    if rest_room_choice == '2':
        Upgrades()
        directions()
    if rest_room_choice == '3':
        Inventory()
        directions()

def battle_room():
    print('='*100)

    # room counter
    global floor
    global room_count
    global total_rooms
    room_count+=1
    print(f'ЭТАЖ {floor}')
    print(f'Комната {room_count}')
    print(f'Всего пройдено {total_rooms} комнат')
    total_rooms += 1
    next_floor()

    # global values
    global stats
    global hp
    defence = stats['DEF']
    agility = stats['Agility']
    atk = stats['ATK']
    global inventory
    global exp

    print('='*100)

    # battle room
    print('Вы попали в боевую комнату!')
    global opponents
    opponent = random.choice(opponents)
    print(f'Ваш противник - {opponent}!')

    # orc
    if opponent == opponents[0]:
        global orc_stats
        orc_hp = orc_stats['MaxHP']
        orc_def = orc_stats['DEF']
        orc_agility = orc_stats['Agility']
        orc_atk = orc_stats['ATK']
        
        # orc / femboy incubus
        if your_class == 'Фембойчик инкуб':
            while orc_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Орка - {orc_hp}')
                print(f'DEF Орка - {orc_def}')

                print('='*100)

                print(f'HP Фембочика инкуба - {hp}')
                print(f'DEF Фембойчика инкуба - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Соблазнить')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Фембойчик инкуб атакует Орка!')

                        # orc evasion success
                        orc_evasion_success = 0
                        if orc_agility < random.randint(1,10):
                            orc_evasion_success = 0
                        else:
                            orc_evasion_success = 1

                        # orc doesn't evade
                        if orc_evasion_success == 0:
                            print('Фембойчик инкуб наносит удар Орку!')
                            print(f'Нанесенный урон - {atk}!')
                            if (orc_def > 0) and (orc_def - atk >= 0):
                                orc_def -= atk
                            elif (orc_def > 0) and (orc_def - atk < 0):
                                orc_def = 0
                            elif orc_def == 0:
                                orc_hp -= atk

                            print('='*100)
                        

                            print('Орк атакует Фембойчика инкуба!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Фембойчику инкубу!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от удара Орка!')

                        # orc evades
                        elif orc_evasion_success == 1:
                            print('Орк уклонился от удара Фембойчика инкуба и атакует его!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Фембойчику инкубу!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от удара Орка!')

                # seduce
                if battle_choice == '2':
                    print('='*100)

                    print('Фембойчик инкуб успешно соблазняет Орка и тем самым покидает поле битвы!')
                    print('Фембойчик инкуб получает +1 к опыту и 15 золотых монет за победу над Орком!')
                    inventory[0] += 15
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # orc defeated
                if orc_hp <= 0:
                    print('='*100)
                    print('Фембойчик инкуб побеждает Орка!')
                    print('Фембойчик инкуб получает +1 к опыту и 15 золотых монет за победу над Орком!')
                    inventory[0] += 15
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # femboy incubus defeated
                elif hp <= 0:
                    print('='*100)
                    print('Орк побеждает Фембойчика инкуба и утаскивает к себе в пещеру!')
                    print('Игра завершена!')
                    sys.exit()
        
        # orc / elf girl
        if your_class == 'Эльфийка':
            while orc_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Орка - {orc_hp}')
                print(f'DEF Орка - {orc_def}')

                print('='*100)

                print(f'HP Эльфийки - {hp}')
                print(f'DEF Эльфийки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Запугать')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Эльфийка стреляет в Орка из лука!')

                        # orc evasion success
                        orc_evasion_success = 0
                        if orc_agility < random.randint(1,10):
                            orc_evasion_success = 0
                        else:
                            orc_evasion_success = 1

                        # orc doesn't evade
                        if orc_evasion_success == 0:
                            print('Стрела Эльфийки попадает в Орка!')
                            print(f'Нанесенный урон - {atk}!')
                            if (orc_def > 0) and (orc_def - atk >= 0):
                                orc_def -= atk
                            elif (orc_def > 0) and (orc_def - atk < 0):
                                orc_def = 0
                            elif orc_def == 0:
                                orc_hp -= atk

                            print('='*100)

                            print('Орк атакует Эльфийку!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Эльфийке!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от удара Орка!')

                        # orc evades
                        elif orc_evasion_success == 1:
                            print('Орк уклонился стрелы Эльфийки и атакует ее!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Эльфийке!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от удара Орка!')

                # threaten
                if battle_choice == '2':
                    print('='*100)

                    # threat success
                    threat_success = random.randint(0,1)

                    # failed threat
                    if threat_success == 0:
                        print('Орк не испугался угроз Эльфийки!')
                        print('Орк атакует Эльфийку!')

                        # elf girl evasion success
                        evasion_success = 0
                        if agility < random.randint(1,10):
                            evasion_success = 0
                        else:
                            evasion_success = 1

                        # elf girl doesn't evade
                        if evasion_success == 0:
                            print('Орк наносит удар Эльфийке!')
                            print(f'Нанесенный урон - {orc_atk}!')
                            if (defence > 0) and (defence - orc_atk >= 0):
                                defence -= orc_atk
                            elif (defence > 0) and (defence - orc_atk < 0):
                                defence = 0 
                            elif defence == 0:
                                hp -= orc_atk

                        # elf girl evades
                        elif evasion_success == 1:
                            print('Эльфийка уклонилась от удара Орка!')

                    # succeeded threat
                    if threat_success == 1:
                        print('Орк испугался угроз Эльфийки и сбежал с поля битвы!')
                        print('Эльфийка получает +1 к опыту и 15 золотых монет за победу над Орком!')
                        inventory[0] += 15
                        print(f'Текущий инвентарь: {inventory}')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # orc defeated
                if orc_hp <= 0:
                    print('='*100)
                    print('Эльфийка побеждает Орка!')
                    print('Эльфийка получает +1 к опыту и 15 золотых монет за победу над Орком!')
                    inventory[0] += 15
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # elf girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Орк побеждает Эльфийку и утаскивает к себе пещеру!')
                    print('Конец!')
                    sys.exit()

        # orc / alfa werewolf
        if your_class == 'Альфа оборотень':
            while orc_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Орка - {orc_hp}')
                print(f'DEF Орка - {orc_def}')

                print('='*100)

                print(f'HP Альфы оборотня - {hp}')
                print(f'DEF Альфы оборотня - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Выть')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Альфа оборотень бросается на Орка!')

                        # orc evasion success
                        orc_evasion_success = 0
                        if orc_agility < random.randint(1,10):
                            orc_evasion_success = 0
                        else:
                            orc_evasion_success = 1

                        # orc doesn't evade
                        if orc_evasion_success == 0:
                            print('Альфа оборотень кусает Орка!')
                            print(f'Нанесенный урон - {atk}!')
                            if (orc_def > 0) and (orc_def - atk >= 0):
                                orc_def -= atk
                            elif (orc_def > 0) and (orc_def - atk < 0):
                                orc_def = 0
                            elif orc_def == 0:
                                orc_hp -= atk

                            print('='*100)

                            print('Орк атакует Альфа Оборотня!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Альфе оборотню!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфа оборотень уклонился от клыков Орка!')

                        # orc evades
                        elif orc_evasion_success == 1:
                            print('Орк уклонился от удара Альфы оборотня и атакует его!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Альфе оборотню!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфа оборотень уклонился от удара Орка!')

                # howl
                if battle_choice == '2':
                    print('='*100)

                    # howl success
                    howl_success = random.randint(0,1)

                    # failed howl
                    if howl_success == 0:
                        print('Вой Альфы оборотня абсолютно никак не повлиял на Орка!')
                        print('Орк атакует Альфу оборотня!')

                        # alfa werewolf evasion success
                        evasion_success = 0
                        if agility < random.randint(1,10):
                            evasion_success = 0
                        else:
                            evasion_success = 1

                        # alfa werewolf doesn't evade
                        if evasion_success == 0:
                            print('Орк наносит удар Альфе оборотню!')
                            print(f'Нанесенный урон - {orc_atk}!')
                            if (defence > 0) and (defence - orc_atk >= 0):
                                defence -= orc_atk
                            elif (defence > 0) and (defence - orc_atk < 0):
                                defence = 0 
                            elif defence == 0:
                                hp -= orc_atk

                        # alfa werewolf evades
                        elif evasion_success == 1:
                            print('Альфа оборотень уклонился от удара Орка!')

                    # succeeded howl
                    if howl_success == 1:
                        print('Орк падает в обморок от воя Альфы оборотня!')
                        print('Альфа оборотень получает +1 к опыту и 15 золотых монет за победу над Орком!')
                        inventory[0] += 15
                        print(f'Текущий инвентарь: {inventory}')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # orc defeated
                if orc_hp <= 0:
                    print('='*100)
                    print('Альфа оборотень побеждает Орка!')
                    print('Альфа оборотень получает +1 к опыту и 15 золотых монет за победу над Орком!')
                    inventory[0] += 15
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # alfa werewolf defeated
                elif hp <= 0:
                    print('='*100)
                    print('Орк побеждает Альфу оборотня!')
                    print('Конец!')
                    sys.exit()

        # orc / cat girl
        if your_class == 'Кошкодевочка':
            while orc_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Орка - {orc_hp}')
                print(f'DEF Орка - {orc_def}')

                print('='*100)

                print(f'HP Кошкодевочки - {hp}')
                print(f'DEF Кошкодевочки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Сбежать')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Кошкодевочка бросается на Орка!')

                        # orc evasion success
                        orc_evasion_success = 0
                        if orc_agility < random.randint(1,10):
                            orc_evasion_success = 0
                        else:
                            orc_evasion_success = 1

                        # orc doesn't evade
                        if orc_evasion_success == 0:
                            print('Кошкодевочка царапает Орка!')
                            print(f'Нанесенный урон - {atk}!')
                            if (orc_def > 0) and (orc_def - atk >= 0):
                                orc_def -= atk
                            elif (orc_def > 0) and (orc_def - atk < 0):
                                orc_def = 0
                            elif orc_def == 0:
                                orc_hp -= atk

                            print('='*100)
                        
                            print('Орк атакует Кошкодевочку!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Кошкодевочке!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от удара Орка!')

                        # orc evades
                        elif orc_evasion_success == 1:
                            print('Орк уклонился от когтей Кошкодевочки и атакует ее!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Орк наносит удар Кошкодевочке!')
                                print(f'Нанесенный урон - {orc_atk}!')
                                if (defence > 0) and (defence - orc_atk >= 0):
                                    defence -= orc_atk
                                elif (defence > 0) and (defence - orc_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= orc_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от удара Орка!')

                # escape
                if battle_choice == '2':
                    print('='*100)

                    print('Кошкодевочка успешно сбегает с поля битвы!')
                    print('Кошкодевочка получает +1 к опыту за побег от Орка!')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # orc defeated
                if orc_hp <= 0:
                    print('='*100)
                    print('Кошкодевочка побеждает Орка!')
                    print('Кошкодевочка получает +1 к опыту и 15 золотых монет за победу над Орком!')
                    inventory[0] += 15
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # cat girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Орк побеждает Кошкодевочку и утаскивает к себе в пещеру!')
                    print('Конец!')
                    sys.exit()
    
    # witch
    if opponent == opponents[1]:
        global witch_stats
        witch_hp = witch_stats['MaxHP']
        witch_def = witch_stats['DEF']
        witch_agility = witch_stats['Agility']
        witch_atk = witch_stats['ATK']
        defence = stats['DEF']
        agility = stats['Agility']
        atk = stats['ATK']

        # witch / femboy incubus
        if your_class == 'Фембойчик инкуб':
            while witch_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Ведьмы - {witch_hp}')
                print(f'DEF Ведьмы - {witch_def}')

                print('='*100)

                print(f'HP Фембочика инкуба - {hp}')
                print(f'DEF Фембойчика инкуба - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Соблазнить')
                print('3. Открыть инвентарь')
                print('4. Подкупить (100 золотых монет)')
                print('5. Подкупить (Зелье молодости)')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 5) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 5!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Фембойчик инкуб атакует Ведьму!')

                        # witch evasion success
                        witch_evasion_success = 0
                        if witch_agility < random.randint(1,10):
                            witch_evasion_success = 0
                        else:
                            witch_evasion_success = 1

                        # witch doesn't evade
                        if witch_evasion_success == 0:
                            print('Фембойчик инкуб наносит удар Ведьме!')
                            print(f'Нанесенный урон - {atk}!')
                            if (witch_def > 0) and (witch_def - atk >= 0):
                                witch_def -= atk
                            elif (witch_def > 0) and (witch_def - atk < 0):
                                witch_def = 0
                            elif witch_def == 0:
                                witch_hp -= atk

                            print('='*100)

                            print('Ведьма кидает в Фембойчика инкуба картами таро!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро Ведьмы попадают в Фембойчика инкуба!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от карт таро Ведьмы!')
                        
                        # witch evades
                        elif witch_evasion_success == 1:
                            print('Ведьма уклонилась от удара Фембойчика инкуба и кидает в него картами таро!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро Ведьмы попадают в Фембойчика инкуба!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от карт таро Ведьмы!')

                # seduce
                if battle_choice == '2':
                    print('='*100)

                    # seduction success
                    seduction_success = random.randint(0,1)

                    # failed seduction
                    if seduction_success == 0:
                        print('Фембойчику инкубу не удалось соблазнить Ведьму!')
                        print('Ведьма кидает в Фембойчика инкуба картами таро!')

                        # femboy incubus evasion success
                        evasion_success = 0
                        if agility < random.randint(1,10):
                            evasion_success = 0
                        else:
                            evasion_success = 1

                        # femboy incubus doesn't evade
                        if evasion_success == 0:
                            print('Карты таро Ведьмы попадают в Фембойчика инкуба!')
                            print(f'Нанесенный урон - {witch_atk}!')
                            if (defence > 0) and (defence - witch_atk >= 0):
                                defence -= witch_atk
                            elif (defence > 0) and (defence - witch_atk < 0):
                                defence = 0 
                            elif defence == 0:
                                hp -= witch_atk

                        # femboy incubus evades
                        elif evasion_success == 1:
                            print('Фембойчик инкуб уклонился от карт таро Ведьмы!')

                    # succeeded seduction
                    if seduction_success == 1:
                        print('Фембойчик инкуб успешно соблазняет Ведьму и тем самым покидает поле битвы!')
                        print('Фембойчик инкуб получает +1 к опыту и 20 золотых монет за победу над Ведьмой!')
                        inventory[0] += 20
                        print(f'Текущий инвентарь: {inventory}')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()


                # bribe with money
                if battle_choice == '4':
                    print('='*100)

                    # insufficient funds
                    if inventory[0] < 100:
                        print('Недостаточно средств!')

                    # sufficient funds
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Фембойчик инкуб получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # bribe with a potion of youth
                if battle_choice == '5':
                    print('='*100)

                    # no potion of youth
                    if {'Зелье молодости'} not in inventory:
                        print('У вас нет Зелья молодости и нечем подкупить Ведьму!')

                    # potion of youth
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Фембойчик инкуб получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

            else:
                # witch defeated
                if witch_hp <= 0:
                    print('='*100)
                    print('Фембойчик инкуб побеждает Ведьму!')
                    print('Фембойчик инкуб получает +1 к опыту и 20 золотых монет за победу над Ведьмой!')
                    inventory[0] += 20
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # femboy incubus defeated
                elif hp <= 0:
                    print('='*100)
                    print('Ведьма побеждает Фембойчика инкуба и продает его Оркам!')
                    print('Конец!')
                    sys.exit()
        
        # witch / elf girl
        if your_class == 'Эльфийка':
            while witch_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Ведьмы - {witch_hp}')
                print(f'DEF Ведьмы - {witch_def}')

                print('='*100)

                print(f'HP Эльфийки - {hp}')
                print(f'DEF Эльфийки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Запугать')
                print('3. Открыть инвентарь')
                print('4. Подкупить (100 золотых монет)')
                print('5. Подкупить (Зелье молодости)')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 5) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 5!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Эльфийка стреляет в Ведьму из лука!')

                        # witch evasion success
                        witch_evasion_success = 0
                        if witch_agility < random.randint(1,10):
                            witch_evasion_success = 0
                        else:
                            witch_evasion_success = 1

                        # witch doesn't evade
                        if witch_evasion_success == 0:
                            print('Стрела Эльфийки попадает в Ведьму!')
                            print(f'Нанесенный урон - {atk}!')
                            if (witch_def > 0) and (witch_def - atk >= 0):
                                witch_def -= atk
                            elif (witch_def > 0) and (witch_def - atk < 0):
                                witch_def = 0
                            elif witch_def == 0:
                                witch_hp -= atk

                            print('='*100)

                            print('Ведьма кидает в Эльфийку картами таро!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро Ведьмы попадают в Эльфийку!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась карт таро Ведьмы!')
                        
                        # witch evades
                        elif witch_evasion_success == 1:
                            print('Ведьма уклонилась от стрелы Эльфийки и атакует ее!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Ведьма кидает в Эльфийку картами таро!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от карт таро Ведьмы!')

                # threaten
                if battle_choice == '2':
                    print('='*100)

                    print('Ведьма не испугалась угроз Эльфийки!')
                    print('Ведьма кидает в Эльфийку картами таро!')

                    # elf girl evasion success
                    evasion_success = 0
                    if agility < random.randint(1,10):
                        evasion_success = 0
                    else:
                        evasion_success = 1

                    # elf girl doesn't evade
                    if evasion_success == 0:
                        print('Карты таро Ведьмы попадают в Эльфийку!')
                        print(f'Нанесенный урон - {witch_atk}!')
                        if (defence > 0) and (defence - witch_atk >= 0):
                            defence -= witch_atk
                        elif (defence > 0) and (defence - witch_atk < 0):
                            defence = 0 
                        elif defence == 0:
                            hp -= witch_atk

                    # elf girl evades
                    elif evasion_success == 1:
                        print('Эльфийка уклонилась от карт таро Ведьмы!')

                # open inventory
                if battle_choice == '3':
                    Inventory()


                # bribe with money
                if battle_choice == '4':
                    print('='*100)

                    # insufficient funds
                    if inventory[0] < 100:
                        print('Недостаточно средств!')

                    # sufficient funds
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Эльфийка получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # bribe with a potion of youth
                if battle_choice == '5':
                    print('='*100)

                    # no potion of youth
                    if {'Зелье молодости'} not in inventory:
                        print('У вас нет Зелья молодости и нечем подкупить Ведьму!')

                    # potion of youth
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Эльфийка получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

            else:
                # witch defeated
                if witch_hp <= 0:
                    print('='*100)
                    print('Эльфийка побеждает Ведьму!')
                    print('Эльфийка получает +1 к опыту и 20 золотых монет за победу над Ведьмой!')
                    inventory[0] += 20
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # elf girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Ведьма побеждает Эльфийку и продает ее Оркам!')
                    print('Конец!')
                    sys.exit()

        # witch / alfa werewolf
        if your_class == 'Альфа оборотень':
            while witch_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Ведьмы - {witch_hp}')
                print(f'DEF Ведьмы - {witch_def}')

                print('='*100)

                print(f'HP Альфы оборотня - {hp}')
                print(f'DEF Альфы оборотня - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Выть')
                print('3. Открыть инвентарь')
                print('4. Подкупить (100 золотых монет)')
                print('5. Подкупить (Зелье молодости)')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 5) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 5!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Альфа оборотень бросается на Ведьму!')

                        # witch evasion success
                        witch_evasion_success = 0
                        if witch_agility < random.randint(1,10):
                            witch_evasion_success = 0
                        else:
                            witch_evasion_success = 1

                        # witch doesn't evade
                        if witch_evasion_success == 0:
                            print('Альфа оборотень кусает Ведьму!')
                            print(f'Нанесенный урон - {atk}!')
                            if (witch_def > 0) and (witch_def - atk >= 0):
                                witch_def -= atk
                            elif (witch_def > 0) and (witch_def - atk < 0):
                                witch_def = 0
                            elif witch_def == 0:
                                witch_hp -= atk

                            print('='*100)

                            print('Ведьма кидает в Альфу оборотня картами таро!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро Ведьмы попадают в Альфу оборотня!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфа оборотень уклонился от карт таро Ведьмы!')
                        
                        # witch evades
                        elif witch_evasion_success == 1:
                            print('Ведьма уклонилась от клыков Альфы оборотня и кидает в него картами таро!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро Ведьмы попадают в Альфу оборотня!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфа оборотень уклонился от карт таро Ведьмы!')

                # howl
                if battle_choice == '2':
                    print('='*100)

                    print('Вой Альфы оборотня абсолютно никак не повлиял на Ведьму!')
                    print('Ведьма кидает в Альфу оборотня картами таро!')

                    # alfa werewolf evasion success
                    evasion_success = 0
                    if agility < random.randint(1,10):
                        evasion_success = 0
                    else:
                        evasion_success = 1

                    # alfa werewolf doesn't evade
                    if evasion_success == 0:
                        print('Карты таро Ведьмы попадают в Альфу оборотня!')
                        print(f'Нанесенный урон - {witch_atk}!')
                        if (defence > 0) and (defence - witch_atk >= 0):
                            defence -= witch_atk
                        elif (defence > 0) and (defence - witch_atk < 0):
                            defence = 0 
                        elif defence == 0:
                            hp -= witch_atk

                    # alfa werewolf evades
                    elif evasion_success == 1:
                        print('Альфа оборотень уклонился от карт таро Ведьмы!')

                # open inventory
                if battle_choice == '3':
                    Inventory()


                # bribe with money
                if battle_choice == '4':
                    print('='*100)

                    # insufficient funds
                    if inventory[0] < 100:
                        print('Недостаточно средств!')

                    # sufficient funds
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Альфа оборотень получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # bribe with a potion of youth
                if battle_choice == '5':
                    print('='*100)

                    # no potion of youth
                    if {'Зелье молодости'} not in inventory:
                        print('У вас нет Зелья молодости и нечем подкупить Ведьму!')

                    # potion of youth
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Альфа оборотень получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

            else:
                # witch defeated
                if witch_hp <= 0:
                    print('='*100)
                    print('Альфа оборотень побеждает Ведьму!')
                    print('Альфа оборотень получает +1 к опыту и 20 золотых монет за победу над Ведьмой!')
                    inventory[0] += 20
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # alfa werewolf defeated
                elif hp <= 0:
                    print('='*100)
                    print('Ведьма побеждает Альфу оборотня и забирает себе в качестве домашнего питомца!')
                    print('Конец!')
                    sys.exit()

        # witch / cat girl
        if your_class == 'Кошкодевочка':
            while witch_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Ведьмы - {witch_hp}')
                print(f'DEF Ведьмы - {witch_def}')

                print('='*100)

                print(f'HP Кошкодевочки - {hp}')
                print(f'DEF Кошкодевочки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Сбежать')
                print('3. Открыть инвентарь')
                print('4. Подкупить (100 золотых монет)')
                print('5. Подкупить (Зелье молодости)')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 5) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 5!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Кошкодевочка бросается на Ведьму!')

                        # witch evasion success
                        witch_evasion_success = 0
                        if witch_agility < random.randint(1,10):
                            witch_evasion_success = 0
                        else:
                            witch_evasion_success = 1

                        # witch doesn't evade
                        if witch_evasion_success == 0:
                            print('Кошкодевочка царапает Ведьму!')
                            print(f'Нанесенный урон - {atk}!')
                            if (witch_def > 0) and (witch_def - atk >= 0):
                                witch_def -= atk
                            elif (witch_def > 0) and (witch_def - atk < 0):
                                witch_def = 0
                            elif witch_def == 0:
                                witch_hp -= atk

                            print('='*100)

                            print('Ведьма кидает в Кошкодевочку картами таро!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро Ведьмы попадают в Кошкодевочку!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от карт таро Ведьмы!')
                        
                        # witch evades
                        elif witch_evasion_success == 1:
                            print('Ведьма уклонилась от когтей Кошкодевочки и кидает в нее картами таро!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Карты таро попадают в Кошкодевочку!')
                                print(f'Нанесенный урон - {witch_atk}!')
                                if (defence > 0) and (defence - witch_atk >= 0):
                                    defence -= witch_atk
                                elif (defence > 0) and (defence - witch_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= witch_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от карт таро Ведьмы!')

                # escape
                if battle_choice == '2':
                    print('='*100)

                    print('Ведьма создает силовое поле, которое не позволяет Кошкодевочке сбежать!')
                    print('Ведьма кидает в Кошкодевочку картами таро!')

                    # cat girl evasion success
                    evasion_success = 0
                    if agility < random.randint(1,10):
                        evasion_success = 0
                    else:
                        evasion_success = 1

                    # cat girl doesn't evade
                    if evasion_success == 0:
                        print('Карты таро Ведьмы попадают в кошкодевочку!')
                        print(f'Нанесенный урон - {witch_atk}!')
                        if (defence > 0) and (defence - witch_atk >= 0):
                            defence -= witch_atk
                        elif (defence > 0) and (defence - witch_atk < 0):
                            defence = 0 
                        elif defence == 0:
                            hp -= witch_atk

                    # cat girl evades
                    elif evasion_success == 1:
                        print('Кошкодевочка уклонилась от карт таро Ведьмы!')

                # open inventory
                if battle_choice == '3':
                    Inventory()


                # bribe with money
                if battle_choice == '4':
                    print('='*100)

                    # insufficient funds
                    if inventory[0] < 100:
                        print('Недостаточно средств!')

                    # sufficient funds
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Кошкодевочка получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # bribe with a potion of youth
                if battle_choice == '5':
                    print('='*100)

                    # no potion of youth
                    if {'Зелье молодости'} not in inventory:
                        print('У вас нет Зелья молодости и нечем подкупить Ведьму!')

                    # potion of youth
                    else:
                        print('Вы успешно подкупаете Ведьму и покидаете поле битвы!')
                        print('Кошкодевочка получает +1 к опыту за подкуп Ведьмы!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

            else:
                # witch defeated
                if witch_hp <= 0:
                    print('='*100)
                    print('Кошкодевочка побеждает Ведьму!')
                    print('Кошкодевочка получает +1 к опыту и 20 золотых монет за победу над Ведьмой!')
                    inventory[0] += 20
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # cat girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Ведьма побеждает Кошкодевочку и забирает себе в качестве домашнего питомца!')
                    print('Конец!')
                    sys.exit()
    
    # beaver
    if opponent == opponents[2]:
        global beaver_stats
        beaver_hp = beaver_stats['MaxHP']
        beaver_def = beaver_stats['DEF']
        beaver_agility = beaver_stats['Agility']
        beaver_atk = beaver_stats['ATK']
        defence = stats['DEF']
        agility = stats['Agility']
        atk = stats['ATK']

        # beaver / femboy incubus
        if your_class == 'Фембойчик инкуб':
            while beaver_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Бобра - {beaver_hp}')
                print(f'DEF Бобра - {beaver_def}')
                
                print('='*100)

                print(f'HP Фембочика инкуба - {hp}')
                print(f'DEF Фембойчика инкуба - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Соблазнить')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Фембойчик инкуб атакует Бобра!')

                        # beaver evasion success
                        beaver_evasion_success = 0
                        if beaver_agility < random.randint(1,10):
                            beaver_evasion_success = 0
                        else:
                            beaver_evasion_success = 1

                        # beaver doesn't eavade
                        if beaver_evasion_success == 0:
                            print('Фембойчик инкуб наносит удар Бобру!')
                            print(f'Нанесенный урон - {atk}!')
                            if (beaver_def > 0) and (beaver_def - atk >= 0):
                                beaver_def -= atk
                            elif (beaver_def > 0) and (beaver_def - atk < 0):
                                beaver_def = 0
                            elif beaver_def == 0:
                                beaver_hp -= atk

                            print('='*100)

                            print('Бобер бьет Фембойчика инкуба хвостом!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Фембойчику инкубу удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от хвоста Бобра!')
                        
                        # beaver evades
                        elif beaver_evasion_success == 1:
                            print('Бобер уклонился от удара Фембойчика инкуба и бьет его хвостом!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Фембойчику инкубу удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от хвоста Бобра!')

                # seduce
                if battle_choice == '2':
                    print('='*100)

                    print('Фембойчику инкубу не удалось соблазнить Бобра!')
                    print('Бобер бьет Фембойчка инкуба хвостом!')

                    # femboy incubus evasion success
                    evasion_success = 0
                    if agility < random.randint(1,10):
                        evasion_success = 0
                    else:
                        evasion_success = 1

                    # femboy incubus doesn't evade
                    if evasion_success == 0:
                        print('Бобер наносит Фембойчику инкубу удар хвостом!')
                        print(f'Нанесенный урон - {beaver_atk}!')
                        if (defence > 0) and (defence - beaver_atk >= 0):
                            defence -= beaver_atk
                        elif (defence > 0) and (defence - beaver_atk < 0):
                            defence = 0 
                        elif defence == 0:
                            hp -= beaver_atk

                    # femboy incubus evades
                    elif evasion_success == 1:
                        print('Фембойчик инкуб уклонился от хвоста Бобра!')

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # beaver defeated
                if beaver_hp <= 0:
                    print('='*100)
                    print('Фембойчик инкуб побеждает Бобра!')
                    print('Фембойчик инкуб получает +1 к опыту и 5 золотых монет за победу над Бобром!')
                    inventory[0] += 5
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # femboy incubus defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бобер побеждает Фембойчика инкуба!')
                    print('Конец!')
                    sys.exit()

        # beaver / elf girl
        if your_class == 'Эльфийка':
            while beaver_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Бобра - {beaver_hp}')
                print(f'DEF Бобра - {beaver_def}')
                
                print('='*100)

                print(f'HP Эльфийки - {hp}')
                print(f'DEF Эльфийки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Угрожать')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Эльфийка стреляет в Бобра из лука!')

                        # beaver evasion success
                        beaver_evasion_success = 0
                        if beaver_agility < random.randint(1,10):
                            beaver_evasion_success = 0
                        else:
                            beaver_evasion_success = 1

                        # beaver doesn't eavade
                        if beaver_evasion_success == 0:
                            print('Стрела Эльфийки попадает в Бобра!')
                            print(f'Нанесенный урон - {atk}!')
                            if (beaver_def > 0) and (beaver_def - atk >= 0):
                                beaver_def -= atk
                            elif (beaver_def > 0) and (beaver_def - atk < 0):
                                beaver_def = 0
                            elif beaver_def == 0:
                                beaver_hp -= atk

                            print('='*100)

                            print('Бобер бьет Эльфийку хвостом!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Эльфийке удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от хвоста Бобра!')
                        
                        # beaver evades
                        elif beaver_evasion_success == 1:
                            print('Бобер уклонился от стрелы Эльфийки и бьет ее хвостом!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Эльфийке удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от хвоста Бобра!')

                # threaten
                if battle_choice == '2':
                    print('='*100)

                    print('Эльфийка успешно запугивает Бобра и он сбегает с поля битвы!')
                    print('Эльфийка получает +1 к опыту и 5 золотых монет за победу над Бобром!')
                    inventory[0] += 5
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # beaver defeated
                if beaver_hp <= 0:
                    print('='*100)
                    print('Эльфийка побеждает Бобра!')
                    print('Эльфийка получает +1 к опыту и 5 золотых монет за победу над Бобром!')
                    inventory[0] += 5
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # elf girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бобер побеждает Эльфийку!')
                    print('Конец!')
                    sys.exit()
                
        # beaver / alfa werewolf
        if your_class == 'Альфа оборотень':
            while beaver_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Бобра - {beaver_hp}')
                print(f'DEF Бобра - {beaver_def}')
                
                print('='*100)

                print(f'HP Альфы оборотня - {hp}')
                print(f'DEF Альфы оборотня - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Выть')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Альфа оборотень бросается на Бобра!')

                        # beaver evasion success
                        beaver_evasion_success = 0
                        if beaver_agility < random.randint(1,10):
                            beaver_evasion_success = 0
                        else:
                            beaver_evasion_success = 1

                        # beaver doesn't eavade
                        if beaver_evasion_success == 0:
                            print('Альфа оборотень кусает Бобра!')
                            print(f'Нанесенный урон - {atk}!')
                            if (beaver_def > 0) and (beaver_def - atk >= 0):
                                beaver_def -= atk
                            elif (beaver_def > 0) and (beaver_def - atk < 0):
                                beaver_def = 0
                            elif beaver_def == 0:
                                beaver_hp -= atk

                            print('='*100)

                            print('Бобер бьет Альфу оборотня хвостом!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Альфе оборотню удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфы оборотень уклонился от хвоста Бобра!')
                        
                        # beaver evades
                        elif beaver_evasion_success == 1:
                            print('Бобер уклонился от удара Альфы оборотня и бьет его хвостом!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Альфе оборотню удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфы оборотень уклонился от хвоста Бобра!')

                # howl
                if battle_choice == '2':
                    print('='*100)

                    print('Бобер падает в обморок от воя Альфы оборотня!')
                    print('Альфа оборотень получает +1 к опыту и 5 золотых монет за победу над Бобром!')
                    inventory[0] += 5
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # beaver defeated
                if beaver_hp <= 0:
                    print('='*100)

                    print('Альфа оборотень побеждает Бобра!')
                    print('Альфа оборотень получает +1 к опыту и 5 золотых монет за победу над Бобром!')
                    inventory[0] += 5
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # alfa werewolf defeated
                elif hp <= 0:
                    print('='*100)

                    print('Бобер побеждает Альфу оборотня!')
                    print('Конец!')
                    sys.exit()

        # beaver / cat girl
        if your_class == 'Кошкодевочка':
            while beaver_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Бобра - {beaver_hp}')
                print(f'DEF Бобра - {beaver_def}')

                print('='*100)

                print(f'HP Кошкодевочки - {hp}')
                print(f'DEF Кошкодевочки - {defence}')
                
                print('='*100)
                print('1. Атаковать')
                print('2. Сбежать')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Кошкодевочка бросается на Бобра!')

                        # beaver evasion success
                        beaver_evasion_success = 0
                        if beaver_agility < random.randint(1,10):
                            beaver_evasion_success = 0
                        else:
                            beaver_evasion_success = 1

                        # beaver doesn't eavade
                        if beaver_evasion_success == 0:
                            print('Кошкодевочка царапает Бобра!')
                            print(f'Нанесенный урон - {atk}!')
                            if (beaver_def > 0) and (beaver_def - atk >= 0):
                                beaver_def -= atk
                            elif (beaver_def > 0) and (beaver_def - atk < 0):
                                beaver_def = 0
                            elif beaver_def == 0:
                                beaver_hp -= atk

                            print('='*100)

                            print('Бобер бьет Кошкодевочку хвостом!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Кошкодевочке удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от хвоста Бобра!')
                        
                        # beaver evades
                        elif beaver_evasion_success == 1:
                            print('Бобер уклонился от когтей Кошкодевочки и бьет ее хвостом!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1

                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бобер наносит Кошкодевочке удар хвостом!')
                                print(f'Нанесенный урон - {beaver_atk}!')
                                if (defence > 0) and (defence - beaver_atk >= 0):
                                    defence -= beaver_atk
                                elif (defence > 0) and (defence - beaver_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= beaver_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от хвоста Бобра!')

                # escape
                if battle_choice == '2':
                    print('='*100)

                    print('Кошкодевочка успешно сбегает с поля битвы!')
                    print('Кошкодевочка получает +1 к опыту за побег от Бобра!')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # beaver defeated
                if beaver_hp <= 0:
                    print('='*100)
                    print('Кошкодевочка побеждает Бобра!')
                    print('Кошкодевочка получает +1 к опыту и 5 золотых монет за победу над Бобром!')
                    inventory[0] += 5
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # cat girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бобер побеждает Кошкодевочку!')
                    print('Конец!')
                    sys.exit()

    # imp
    if opponent == opponents[3]:
        global imp_stats
        imp_hp = imp_stats['MaxHP']
        imp_def = imp_stats['DEF']
        imp_agility = imp_stats['Agility']
        imp_atk = imp_stats['ATK']

        # imp / femboy incubus
        if your_class == 'Фембойчик инкуб':
            while imp_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Беса - {imp_hp}')
                print(f'DEF Беса - {imp_def}')

                print('='*100)

                print(f'HP Фембочика инкуба - {hp}')
                print(f'DEF Фембойчика инкуба - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Соблазнить')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Фембойчик инкуб атакует Беса!')

                        # imp evasion success
                        imp_evasion_success = 0
                        if imp_agility < random.randint(1,10):
                            imp_evasion_success = 0
                        else:
                            imp_evasion_success = 1

                        # imp doesn't evade
                        if imp_evasion_success == 0:
                            print('Фембойчик инкуб наносит удар Бесу!')
                            print(f'Нанесенный урон - {atk}!')
                            if (imp_def > 0) and (imp_def - atk >= 0):
                                imp_def -= atk
                            elif (imp_def > 0) and (imp_def - atk < 0):
                                imp_def = 0
                            elif imp_def == 0:
                                imp_hp -= atk

                            print('='*100)

                            print('Бес атакует Фембойчика инкуба дьявольскими вилами!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает дявольскими вилами в Фембойчика инкуба!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от дьявольских вил Беса!')

                        # imp evades
                        elif imp_evasion_success == 1:
                            print('Бес уклонился от удара Фембойчика инкуба и атакует его дьявольскими вилами!')

                            # femboy incubus evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # femboy incubus doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает в Фембойчика инкуба дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # femboy incubus evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Фембойчик инкуб уклонился от дьявольских вил Беса!')

                # seduce
                if battle_choice == '2':
                    print('='*100)

                    print('Фембойчик инкуб успешно соблазняет Беса и тем самым покидает поле битвы!')
                    print('Фембойчик инкуб получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                    inventory[0] += 10
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # imp defeated
                if imp_hp <= 0:
                    print('='*100)
                    print('Фембойчик инкуб побеждает Беса!')
                    print('Фембойчик инкуб получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                    inventory[0] += 10
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # femboy incubus defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бес побеждает Фембойчика инкуба и утаскивает его к себе в пещеру!')
                    print('Конец!')
                    sys.exit()

        # imp / elf girl
        if your_class == 'Эльфийка':
            while imp_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Беса - {imp_hp}')
                print(f'DEF Беса - {imp_def}')

                print('='*100)

                print(f'HP Эльфийки - {hp}')
                print(f'DEF Эльфийки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Запугать')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Эльфийка стреляет в Беса из лука!')

                        # imp evasion success
                        imp_evasion_success = 0
                        if imp_agility < random.randint(1,10):
                            imp_evasion_success = 0
                        else:
                            imp_evasion_success = 1

                        # imp doesn't evade
                        if imp_evasion_success == 0:
                            print('Стрела Эльфийки попадает в Беса!')
                            print(f'Нанесенный урон - {atk}!')
                            if (imp_def > 0) and (imp_def - atk >= 0):
                                imp_def -= atk
                            elif (imp_def > 0) and (imp_def - atk < 0):
                                imp_def = 0
                            elif imp_def == 0:
                                imp_hp -= atk

                            print('='*100)

                            print('Бес атакует Эльфийку дьявольскими вилами!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает в Эльфийку дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от дьявольских вил Беса!')

                        # imp evades
                        elif imp_evasion_success == 1:
                            print('Бес уклонился от стрелы Эльфийки и атакует ее дьявольскими вилами!')

                            # elf girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # elf girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает в Эльфийку дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # elf girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Эльфийка уклонилась от дьявольских вил Беса!')

                # threaten
                if battle_choice == '2':
                    print('='*100)

                    # threat success
                    threat_success = random.randint(0,1)

                    # failed threat
                    if threat_success == 0:
                        print('Бес не испугался угроз Эльфийки!')
                        print('Бес атакует Эльфийку дьявольскими вилами!')

                        # elf girl evasion success
                        evasion_success = 0
                        if agility < random.randint(1,10):
                            evasion_success = 0
                        else:
                            evasion_success = 1

                        # elf girl doesn't evade
                        if evasion_success == 0:
                            print('Бес попадает в Эльфийку дьявольскими вилами!')
                            print(f'Нанесенный урон - {imp_atk}!')
                            if (defence > 0) and (defence - imp_atk >= 0):
                                defence -= imp_atk
                            elif (defence > 0) and (defence - imp_atk < 0):
                                defence = 0 
                            elif defence == 0:
                                hp -= imp_atk

                        # elf girl evades
                        elif evasion_success == 1:
                            print('Эльфийка уклонилась от дьявольских вил Беса!')

                    # succeeded threat
                    if threat_success == 1:
                        print('Бес испугался угроз Эльфийки и сбежал с поля битвы!')
                        print('Эльфийка получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                        inventory[0] += 10
                        print(f'Текущий инвентарь: {inventory}')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # imp defeated
                if imp_hp <= 0:
                    print('='*100)
                    print('Эльфийка побеждает Беса!')
                    print('Эльфийка получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                    inventory[0] += 10
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # elf girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бес побеждает Эльфийку и утаскивает ее к себе в пещеру!')
                    print('Конец!')
                    sys.exit()

        # imp / alfa werewolf
        if your_class == 'Альфа оборотень':
            while imp_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Беса - {imp_hp}')
                print(f'DEF Беса - {imp_def}')

                print('='*100)

                print(f'HP Альфы оборотня - {hp}')
                print(f'DEF Альфы оборотня - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Выть')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Альфа оборотень бросается на Беса!')

                        # imp evasion success
                        imp_evasion_success = 0
                        if imp_agility < random.randint(1,10):
                            imp_evasion_success = 0
                        else:
                            imp_evasion_success = 1

                        # imp doesn't evade
                        if imp_evasion_success == 0:
                            print('Альфа оборотень кусает Беса!')
                            print(f'Нанесенный урон - {atk}!')
                            if (imp_def > 0) and (imp_def - atk >= 0):
                                imp_def -= atk
                            elif (imp_def > 0) and (imp_def - atk < 0):
                                imp_def = 0
                            elif imp_def == 0:
                                imp_hp -= atk

                            print('='*100)

                            print('Бес атакует Альфу оборотня дьявольскими вилами!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает в Альфу оборотня дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфа оборотень уклонился от дьявольских вил Беса!')

                        # imp evades
                        elif imp_evasion_success == 1:
                            print('Бес уклонился от клыков Альфы оборотня и атакует его дьявольскими вилами!')

                            # alfa werewolf evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # alfa werewolf doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает по Альфе оборотню дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # alfa werewolf evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Альфа оборотень уклонился от дьявольских вил Беса!')

                # howl
                if battle_choice == '2':
                    print('='*100)

                    # howl success
                    howl_success = random.randint(0,1)

                    # failed howl
                    if howl_success == 0:
                        print('Вой Альфы оборотня абсолютно никак не повлиял на Беса!')
                        print('Бес атакует Альфу оборотня дьявольскими вилами!')

                        # alfa werewolf evasion success
                        evasion_success = 0
                        if agility < random.randint(1,10):
                            evasion_success = 0
                        else:
                            evasion_success = 1

                        # alfa werewolf doesn't evade
                        if evasion_success == 0:
                            print('Бес попадает по Альфе оборотню дьявольскими вилами!')
                            print(f'Нанесенный урон - {imp_atk}!')
                            if (defence > 0) and (defence - imp_atk >= 0):
                                defence -= imp_atk
                            elif (defence > 0) and (defence - imp_atk < 0):
                                defence = 0 
                            elif defence == 0:
                                hp -= imp_atk

                        # alfa werewolf evades
                        elif evasion_success == 1:
                            print('Альфа оборотень уклонился от дьявольских вил Беса!')

                    # succeeded howl
                    if threat_success == 1:
                        print('Бес упас в обморок от воя Альфы оборотня!')
                        print('Альфа оборотень получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                        inventory[0] += 10
                        print(f'Текущий инвентарь: {inventory}')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # imp defeated
                if imp_hp <= 0:
                    print('='*100)
                    print('Альфа оборотень побеждает Беса!')
                    print('Альфа оборотень получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                    inventory[0] += 10
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # alfa werewolf defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бес побеждает Альфу оборотня!')
                    print('Конец!')
                    sys.exit()
        
        # imp / cat girl
        if your_class == 'Кошкодевочка':
            while imp_hp > 0 and hp > 0:
                print('='*100)

                print(f'HP Беса - {imp_hp}')
                print(f'DEF Беса - {imp_def}')

                print('='*100)

                print(f'HP Кошкодевочки - {hp}')
                print(f'DEF Кошкодевочки - {defence}')

                print('='*100)
                print('1. Атаковать')
                print('2. Сбежать')
                print('3. Открыть инвентарь')
                battle_choice = input('Что будете делать? ')


                # check if the entered data is valid
                is_int(battle_choice)
                if (int(battle_choice) > 3) or (int(battle_choice) < 1):
                    print(f'ОТ 1 ДО 3!!!!!')
                    sys.exit()

                # attack
                if battle_choice == '1':
                        print('='*100)

                        print('Кошкодевочка бросается на Беса!')

                        # imp evasion success
                        imp_evasion_success = 0
                        if imp_agility < random.randint(1,10):
                            imp_evasion_success = 0
                        else:
                            imp_evasion_success = 1

                        # imp doesn't evade
                        if imp_evasion_success == 0:
                            print('Кошкодевочка царапает Беса!')
                            print(f'Нанесенный урон - {atk}!')
                            if (imp_def > 0) and (imp_def - atk >= 0):
                                imp_def -= atk
                            elif (imp_def > 0) and (imp_def - atk < 0):
                                imp_def = 0
                            elif imp_def == 0:
                                imp_hp -= atk

                            print('='*100)

                            print('Бес атакует Кошкодевочку дьявольскими вилами!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает в Кошкодевочку дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от дьявольских вил Беса!')

                        # imp evades
                        elif imp_evasion_success == 1:
                            print('Бес уклонился от когтей Кошкодевочки и атакует ее дьявольскими вилами!')

                            # cat girl evasion success
                            evasion_success = 0
                            if agility < random.randint(1,10):
                                evasion_success = 0
                            else:
                                evasion_success = 1
                        
                            # cat girl doesn't evade
                            if evasion_success == 0:
                                print('='*100)

                                print('Бес попадает в Кошкодевочку дьявольскими вилами!')
                                print(f'Нанесенный урон - {imp_atk}!')
                                if (defence > 0) and (defence - imp_atk >= 0):
                                    defence -= imp_atk
                                elif (defence > 0) and (defence - imp_atk < 0):
                                    defence = 0 
                                elif defence == 0:
                                    hp -= imp_atk

                            # cat girl evades
                            elif evasion_success == 1:
                                print('='*100)

                                print('Кошкодевочка уклонилась от дьявольских вил Беса!')

                # escape
                if battle_choice == '2':
                    print('='*100)

                    # escape success
                    escape_success = random.randint(0,1)

                    # failed escape
                    if escape_success == 0:
                        print('Бес поймал Кошкодевочку за хвост!')
                        print('Бес атакует Кошкодевочку дьявольскоми вилами!')

                        # cat girl evasion success
                        evasion_success = 0
                        if agility < random.randint(1,10):
                            evasion_success = 0
                        else:
                            evasion_success = 1

                        # cat girl doesn't evade
                        if evasion_success == 0:
                            print('Бес попадает в Кошкодевочку дьявольскими вилами!')
                            print(f'Нанесенный урон - {imp_atk}!')
                            if (defence > 0) and (defence - imp_atk >= 0):
                                defence -= imp_atk
                            elif (defence > 0) and (defence - imp_atk < 0):
                                defence = 0 
                            elif defence == 0:
                                hp -= imp_atk

                        # cat girl evades
                        elif evasion_success == 1:
                            print('Кошкодевочка уклонилась от дьявольских вил Беса!')

                    # succeeded escape
                    if escape_success == 1:
                        print('Бес не смог поймать Кошкодевочку и она успешно сбежала!')
                        print('Кошкодевочка получает +1 к опыту за побег от Беса!')
                        exp += 1
                        exp_reset()
                        print(f'Текущий уровень: {lvl}')
                        print(f'Текущий опыт: {exp}/5')
                        directions()

                # open inventory
                if battle_choice == '3':
                    Inventory()

            else:
                # imp defeated
                if imp_hp <= 0:
                    print('='*100)
                    print('Кошкодевочка побеждает Беса!')
                    print('Кошкодевочка получает +1 к опыту и 10 золотых монет за победу над Бесом!')
                    inventory[0] += 10
                    print(f'Текущий инвентарь: {inventory}')
                    exp += 1
                    exp_reset()
                    print(f'Текущий уровень: {lvl}')
                    print(f'Текущий опыт: {exp}/5')
                    directions()

                # cat girl defeated
                elif hp <= 0:
                    print('='*100)
                    print('Бес побеждает Кошкодевочку и утаскивает ее к себе в пещеру!')
                    print('Конец!')
                    sys.exit()
          
def reward_room():
    print('='*100)

    # room counter
    global floor
    global room_count
    global total_rooms
    room_count+=1
    print(f'ЭТАЖ {floor}')
    print(f'Комната {room_count}')
    print(f'Всего пройдено {total_rooms} комнат')
    total_rooms += 1
    next_floor()

    print('='*100)

    print('Вы попали в Комнату с сундуком!')

    print('='*100)

    print('1. Уйти')
    print('2. Заглянуть в сундук')
    chest_choice = input('Что будете делать? ')

    # check if the entered data is valid
    is_int(chest_choice)
    if (int(chest_choice) > 2) or (int(chest_choice) < 1):
        print(f'ОТ 1 ДО 2!!!!!')
        sys.exit()

    # leave
    if chest_choice == '1':
        directions()
    
    # take a look
    if chest_choice == '2':
        print('='*100)

        available_items = [5, 10, 25, 30, 50, 'Зелье здоровья', 'Зелье молодости', 'Пыль']
        chest = random.choice(available_items)
        print('Вы заглядывате в сундук, а там...')
        if chest == 'Пыль':
            print('Пыль')
            print('Кажется, вы не первый, кто сюда пришел')
            print('Увы, вы уходите без добычи')
            directions()

        # gold coins
        if chest == 5 or chest == 10 or chest == 25 or chest == 30 or chest == 50:
            print(f'{chest} золотых монет!')

            print('='*100)


            print('1. Нет')
            print('2. Да')
            take_choice = input('Забрать? ')

            # check if the entered data is valid
            is_int(take_choice)
            if (int(take_choice) > 2) or (int(take_choice) < 1):
                print(f'ОТ 1 ДО 2!!!!!')
                sys.exit()

            # no not take
            if take_choice == '1':
                print('='*100)

                print(f'Вы решаете не поддаваться капитализму и оставляете {chest} золотых монет там, где нашли!')
                print(f'Ваш текущий инвентарь: {inventory}')
                directions()

            # yes take
            if take_choice == '2':
                print('='*100)

                print(f'Вы забираете {chest} золотых монет!')
                inventory[0] += chest
                print(f'Ваш текущий инвентарь: {inventory}')
                directions()

        # health potion
        if chest == 'Зелье здоровья':
            print(f'{chest}!')

            print('='*100)

            print('1. Нет')
            print('2. Да')
            take_choice = input('Забрать? ')

            # check if the entered data is valid
            is_int(take_choice)
            if (int(take_choice) > 2) or (int(take_choice) < 1):
                print(f'ОТ 1 ДО 2!!!!!')
                sys.exit()

            # no not take
            if take_choice == '1':
                print('='*100)

                print(f'Вы решаете, что хил для слабаков и оставляете Зелье здоровья там, где нашли!')
                print(f'Ваш текущий инвентарь: {inventory}')
                directions()

            # take if enough space
            if take_choice == '2' and len(inventory) < 5:
                print('='*100)

                print(f'Вы забираете Зелье здоровья!')
                inventory.append({chest})
                print(f'Ваш текущий инвентарь: {inventory}')
                directions()

            # take if not enough space
            if take_choice == '2' and len(inventory) == 5:
                print('='*100)

                print(f'Увы, вам не хватает слотов в инвентаре')
                print('Вы можете выбросить какой-то предмет из инвентаря или смириться')

                print('='*100)

                print('1. Уйти')
                print('2. Выбросить предмет')
                slots_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(take_choice)
                if (int(take_choice) > 2) or (int(take_choice) < 1):
                    print(f'ОТ 1 ДО 2!!!!!')
                    sys.exit()

                # leave
                if slots_choice == '1':
                    print('='*100)

                    print('Вы принимаете свою судьбу такой, какая она есть и идете дальше')
                    print(f'Ваш текущий инвентарь: {inventory}')
                    directions()

                #trow an item away
                if slots_choice == '2':
                    print('='*100)

                    for i in range(len(inventory)):
                        print(f'{i+1}. {inventory[i]}')
                    item_choice = input('Какой предмет хотите выбросить? ')

                    # check if the entered data is valid
                    is_int(item_choice)
                    if (int(item_choice) > len(inventory)) or (int(item_choice) < 1):
                        print(f'ОТ 1 ДО {len(inventory)}!!!!!')
                        sys.exit()

                    del inventory[int(item_choice)-1]
                    print('Предмет был успешно выброшен!')
                    print(f'Ваш текущий инвентарь: {inventory}')

                    print('='*100)

                    print(f'Вы забираете Зелье здоровья!')
                    inventory.append({chest})
                    print(f'Ваш текущий инвентарь: {inventory}')
                    directions()

        # youth potion
        if chest == 'Зелье молодости':
            print(f'{chest}!')

            print('='*100)

            print('1. Нет')
            print('2. Да')
            take_choice = input('Забрать? ')

            # check if the entered data is valid
            is_int(take_choice)
            if (int(take_choice) > 2) or (int(take_choice) < 1):
                print(f'ОТ 1 ДО 2!!!!!')
                sys.exit()

            # no not take
            if take_choice == '1':
                print('='*100)

                print(f'Вы решаете, что молодость вам не нужна и оставляете Зелье молодости там, где нашли!')
                print(f'Ваш текущий инвентарь: {inventory}')
                directions()

            # take if enough space
            if take_choice == '2' and len(inventory) < 5:
                print('='*100)

                print(f'Вы забираете Зелье молодости!')
                inventory.append({chest})
                print(f'Ваш текущий инвентарь: {inventory}')
                directions()
            
            # take if not enough space
            if take_choice == '2' and len(inventory) == 5:
                print('='*100)

                print(f'Увы, вам не хватает слотов в инвентаре')
                print('Вы можете использовать/выбросить какой-то предмет из инвентаря или смириться')

                print('='*100)

                print('1. Избавиться от предмета')
                print('2. Уйти')
                slots_choice = input('Что будете делать? ')

                # check if the entered data is valid
                is_int(take_choice)
                if (int(take_choice) > 2) or (int(take_choice) < 1):
                    print(f'ОТ 1 ДО 2!!!!!')
                    sys.exit()

                # leave
                if slots_choice == '1':
                    print('='*100)

                    print('Вы принимаете свою судьбу такой, какая она есть и идете дальше')
                    print(f'Ваш текущий инвентарь: {inventory}')
                    directions()

                # trow an item away
                if slots_choice == '1':
                    print('='*100)

                    for i in range(len(inventory)):
                        print(f'{i+1}. {inventory[i]}')
                    item_choice = input('Какой предмет хотите выбросить? ')

                    # check if the entered data is valid
                    is_int(item_choice)
                    if (int(item_choice) > len(inventory)) or (int(item_choice) < 1):
                        print(f'ОТ 1 ДО {len(inventory)}!!!!!')
                        sys.exit()

                    del inventory[int(item_choice)-1]
                    print('Предмет был успешно выброшен!')
                    print(f'Ваш текущий инвентарь: {inventory}')

                    print('='*100)

                    print(f'Вы забираете Зелье молодости!')
                    inventory.append({chest})
                    print(f'Ваш текущий инвентарь: {inventory}')
                    directions()



print('Вы попали в подземелье!')
print(f'ЭТАЖ {floor}')
print(f'Всего пройдено комнат: {total_rooms}')
print(f'Текущий инвентарь: {inventory}')
directions()