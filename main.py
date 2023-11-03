def print_map(matrix: list):
    '''
    Функция отвечает за вывод игрового поля согласно шаблону
    На вход подаётся само поле
    '''
    title = [0, 1, 2]
    print(' ', *title)
    for i in range(3):
        print(title[i], *matrix[i])
    return


def progress(x, y, count, matrix: list):
    '''
    Функция поочерёдно выставляет на игровое поле "х" и "о"
    :param x: Координата по вертикали (int)
    :param y: Координата по горизонтали (int)
    :param count: Счётчик, благодаря которому решается какой именно символ выставляется (int)
    :param matrix: Игровое поле (list)
    :return: Обновлённое игровое поле (list)
    '''
    if matrix[x][y] == '-':
        if count % 2 == 0:
            matrix[x][y] = 'x'
        else:
            matrix[x][y] = 'o'
        return matrix
    else:
        return False

def victory(matrix: list):
    '''
    Функция, которая определяет, закончена ли игра
    :param matrix: Игровое поле (list)
    :return: (bool)
    '''
    if matrix[0][0] != '-' and matrix[0][0] == matrix[0][1] == matrix[0][2]  \
            or matrix[1][0] != '-' and matrix[1][0] == matrix[1][1] == matrix[1][2]  \
            or matrix[2][0] != '-' and matrix[2][0] == matrix[2][1] == matrix[2][2]:
        return True
    elif matrix[0][0] != '-' and matrix[0][0] == matrix[1][0] == matrix[2][0] \
            or matrix[0][1] != '-' and matrix[0][1] == matrix[1][1] == matrix[2][1] \
            or matrix[0][2] != '-' and matrix[0][2] == matrix[1][2] == matrix[2][2]:
        return True
    elif matrix[0][0] != '-' and matrix[0][0] == matrix[1][1] == matrix[2][2] \
            or matrix[0][2] != '-' and matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return True
    else:
        return False


def game():
    '''
    В этой функции происходит сам процесс игры
    Ввод координат в формате "01", "20"
    '''
    count = 2
    game_ = [['-'] * 3 for i in range(3)]
    print_map(game_)
    ascii_digits = lambda s: s >= '0' and s <= '2'
    counter = 0
    while counter < 9:
        input_ = str(input())
        if len(input_) == 2 and ascii_digits(input_[0]) and ascii_digits(input_[1]):
            x, y = int(input_[0]), int(input_[1])
        else:
            print('Invalid input')
            continue
        buffer = progress(x, y, count, game_)
        if buffer is False:
            print('Occupied')
            continue
        game_ = buffer
        print_map(game_)
        if victory(game_):
            return
        count += 1
        counter += 1
        print('#' * 20)



game()
