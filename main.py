"""Модуль создания персонажей и их навыков."""
from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """
    Применение атаки персонажем.

    Аргументы:
    char_name: str -- имя игрока
    char_class: str -- название персонажа

    Возвращаемое значение:
    str -- информация о нанесеном уроне противнику персонажем.
    """
    char_points: int = None
    points: int = None
    if char_class == 'warrior':
        char_points = 5
        points = char_points + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {points}')
    if char_class == 'mage':
        char_points = 5
        points = char_points + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {points}')
    if char_class == 'healer':
        char_points = 5
        points = char_points + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {points}')


def defence(char_name: str, char_class: str) -> str:
    """
    Применение защиты персонажем.

    Аргументы:
    char_name: str -- имя игрока
    char_class: str -- название персонажа

    Возвращаемое значение:
    str -- информация, какую атаку отразил персонаж.
    """
    char_points: int = None
    points: int = None
    if char_class == 'warrior':
        char_points = 10
        points = char_points + randint(5, 10)
        return (f'{char_name} блокировал {points} урона')
    if char_class == 'mage':
        char_points = 10
        points = char_points + randint(-2, 2)
        return (f'{char_name} блокировал {points} урона')
    if char_class == 'healer':
        char_points = 10
        points = char_points + randint(2, 5)
        return (f'{char_name} блокировал {points} урона')


def special(char_name: str, char_class: str) -> str:
    """
    Применение суперсилы персонажем.

    Аргументы:
    char_name: str -- имя игрока
    char_class: str -- название персонажа

    Возвращаемое значение:
    str -- информация, какую суперсилу и в каком количестве применил персонаж.
    """
    char_points: int = None
    points: int = None
    if char_class == 'warrior':
        char_points = 80
        points = char_points + 25
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {points}»')
    if char_class == 'mage':
        char_points = 5
        points = char_points + 40
        return (f'{char_name} применил специальное умение «Атака {points}»')
    if char_class == 'healer':
        char_points = 10
        points = char_points + 30
        return (f'{char_name} применил специальное умение «Защита {points}»')


def start_training(char_name: str, char_class: str) -> str:
    """
    Начать тренировку персонажем.

    Аргументы:
    char_name: str -- имя игрока
    char_class: str -- название персонажа

    Возвращаемое значение:
    str -- информация о ходе ведения тренировки персонажем
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или'
          ' special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """
    Выбор берсонажа.

    Возвращаемое значение:
    char_class: str -- название выбранного персонажа.
    """
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, '
                           'Маг — mage, '
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


# ...запишите:
if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
