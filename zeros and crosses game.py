# Игра Крестики-Нолики (Tic-Tac-Toe)

# Цвета для консоли
COLOR_X = '\033[34m'  # Синий
COLOR_O = '\033[33m'  # Жёлто-оранжевый
COLOR_RESET = '\033[0m'  # Сброс цвета

def print_board(board):
    """Выводит текущее состояние игрового поля."""
    print("\n  0 1 2")
    for i, row in enumerate(board):
        line = []
        for cell in row:
            if cell == 'x':
                line.append(COLOR_X + 'x' + COLOR_RESET)
            elif cell == 'o':
                line.append(COLOR_O + 'o' + COLOR_RESET)
            else:
                line.append('-')
        print(f"{i} {' '.join(line)}")


def check_game_over(board):
    """
    Проверяет, завершена ли игра: есть ли победитель или ничья.
    - 'x' или 'o', если есть победитель
    - 'Draw', если ничья
    - None, если игра продолжается
    """

    # Все возможные линии для победы (строки, столбцы, диагонали)
    lines = []

    # Добавляем строки
    lines.extend(board)

    # Добавляем столбцы
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        lines.append(column)

    # Добавляем диагонали
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    # Проверяем заполнение каждой линии
    for line in lines:
        if line.count('x') == 3:
            return 'x'
        if line.count('o') == 3:
            return 'o'

    # Проверка на ничью
    if all(cell in ['x', 'o'] for row in board for cell in row):
        return 'Draw'

    # Продолжить игру
    return None


def get_move(player_name, board):
    """
    Запрашивает у игрока ход и проверяет его корректность.
    Возвращает допустимые координаты (row, col).
    """
    while True:
        try:
            move = input(f"\nХод игрока {player_name} (введите номер строки и столбца через пробел (например: 1 2): ")
            row, col = map(int, move.split())

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Ошибка: значения должны быть от 0 до 2.")
            elif board[row][col] in ['x', 'o']:
                print("Ошибка: эта ячейка уже занята!")
            else:
                return row, col
        except ValueError:
            print("Ошибка: введите два целых числа через пробел.")


def play_game():
    """Основная функция для запуска игры."""
    print('"Добро пожаловать в игру Крестики-Нолики!"')
    print("Игровое поле: ")

    player_x =  '"Первый игрок"'
    player_o =  '"Второй игрок"'

    # Инициализация пустого игрового поля
    board = [['-' for _ in range(3)] for _ in range(3)]

    current_player = 'x'
    current_player_name = player_x
    game_over = False

    while not game_over:
        print_board(board)
        row, col = get_move(current_player_name, board)
        board[row][col] = current_player

        result = check_game_over(board)

        if result == 'x' or result == 'o':
            print_board(board)
            print(f"\nИгрок {result} Вы победили!")
            game_over = True
        elif result == 'Draw':
            print_board(board)
            print("\nНичья! Игра окончена.")
            game_over = True
        else:
            # Меняем игрока
            if current_player == 'x':
                current_player = 'o'
                current_player_name = player_o
            else:
                current_player = 'x'
                current_player_name = player_x


# Запуск игры
if __name__ == "__main__":
    play_game()