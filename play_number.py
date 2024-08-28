from random import randint

def game():
    print('Добро пожаловать в игру!\n')
    print('Выбирите уровень сложности:\n1-легий\n2-средний\n3-сложный\n')
    y = 0
    while True:
        try:
            user1 = int(input('введите цифру, соответствующую уровню\n'))
        except ValueError:
            print('Ошибка. Необходимо ввести целое число.\n')
            continue
        if user1 == 1:
            import random
            x = random.randint(0,50)
            print("вы выбрали легкий уровень, угадайте число от 0 до 50")
            break
        elif user1 == 2:
            import random
            x = random.randint(0,200)
            print("вы выбрали средний уровень, угадайте число от 0 до 200")
            break
        elif user1 == 3:
            import random
            x = random.randint(0,350)
            print("вы выбрали сложный уровень, угадайте число от 0 до 350")
            break
        else:
            print("Необходимо выбрать уровень сложности из предложенных вариантов:\n1-легий\n2-средний\n3-сложный\n")
    
    while True:
        try:
            user2 = int(input('Введите число\n'))
        except ValueError:
            print('Ошибка. Необходимо ввести целое число.\n')
            continue
        y += 1
        if user2 == x:
            print("вы угадали, \nколичество попыток:" + str(y) + "\nспасибо за игру!")
            break
        elif user2 > x:
            print("мое число меньше, повторите попытку")
        else:
            print("мое число больше, повторите попытку")

game()
