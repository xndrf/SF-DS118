import numpy as np

def random_predict(number:int=1) -> int:
    """Алгорит угадывания числа не более чем за 20 попыток.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Количество попыток
    """
    # Задаем начальное количество попыток
    count = 0
    # Задаем минимальную и максимульную границу чисел
    # Термины для справки (minimum number and maximum number)
    min_num, max_num = 1, 101
    #  Создаем цикл while
    while True:
        count += 1
    # Термины для справки  guessed number - g_num:
    # Создаем оператор-выражения if-else
    # if g_num == number:
    #     min_num + (max_num - min_num)//2
    # return count
    # Записываем код более компактно (Синтаксический сахар):
        if (g_num := min_num + (max_num - min_num)//2) == number:
            return count
    # Условную инструкцию if/else:
    #   if g_num < number:
    #       min_num, max_num = g_num, max_num
    #   else:
    #       min_num, max_num = min_num, g_num
    # записываем в виде трехместном выражение if/else
        min_num, max_num = ((g_num, max_num) if g_num < number else
                            (min_num, g_num))


def score_game(random_predict) -> int:
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":
    # RUN
    score_game(random_predict)