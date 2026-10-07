# Игракрестики - н олики
# from colorama import Fore, Back, Style


# Рисуем игровое поле
def draw_game_board(game_state):
    print('--------')
    print(f'|{game_state[0][0]}|{game_state[1][0]}|{game_state[2][0]}|')
    print('--------')
    print(f'|{game_state[0][1]}|{game_state[1][1]}|{game_state[2][1]}|')
    print('--------')
    print(f'|{game_state[0][2]}|{game_state[1][2]}|{game_state[2][2]}|')
    print('--------')


# Запрашиваем ход игрока и проверяем корректность ввода координат
def get_move(game_state, user):
    while True:
        try:
            x,y = (
                input(f'Игрок {user}, введите координаты '\
                   'через пробел(пример 0 1): ').strip().split(' '))
            x = int(x)
            y = int(y)
            if (0 <= x <= 2) and (0 <= y <= 2) and (game_state[x][y]) == ' ':
                print(f'x = {x} y = {y} зачение [x][y]= "{game_state[x][y]}"')
                return x,y
            else:
                print(f'x = {x} y = {y} ')
                print('Координата за пределами диапазона или уже занята')
        except ValueError:
            print('Значение не корректно')


# Проверка победы
def check_win(game_state, user):

    # Проверяем равенство значений в строках и столбцах
    for i in range(3):
        # ..столбцы
        if (game_state[i][0] == user) and (game_state[i][1]==user)\
                and (game_state[i][2]== user):
            return True
        # ..строки
        if (game_state[0][i] == user) and (game_state[1][i]==user)\
                and (game_state[2][i]== user):
            return True

    # Проверяем диагональ слева направо-вниз
    if (game_state[0][0] == user and
        game_state[1][1] == user and
        game_state[2][2] == user):
        return True

    # Проверяем диагональ слева направо-вниз
    if (game_state[2][0] == user and
        game_state[1][1] == user and
        game_state[0][2] == user):
        return True

    return False


# Функция запуска игры
def play_game():
    # задаем поле состоящее из пробелов
    game_state = [[' ' for i in range(3)] for j in range(3)]
    # устанавливаем первого игрока
    user = 'x'
    # Рисуем поле
    draw_game_board(game_state)

    # Запускаем бесконечный ход
    while True:
        # Запрашиваем ход
        x, y = get_move(game_state, user)
        # Запоминаемсделанный ход
        game_state[x][y] = user

        draw_game_board(game_state)

        # Проверяем выигрыш
        if check_win(game_state, user):
            print(f'Победил участник {user} !!!')
            return 0

        # Проверяем ничью
        if all(cell != " " for row in game_state for cell in row):
            print("Ничья!")
            return 0

        # Передаем ход другому игроку
        user = '0' if user == 'x' else 'x'
        # player = "0" if player == "X" else "X"


play_game()