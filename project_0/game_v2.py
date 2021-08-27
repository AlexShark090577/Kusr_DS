"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    mn = 1
    mx = 101
    while True:
        new_num = (mn+mx) // 2
        count += 1
        if number == new_num:
            break  # выход из цикла если угадали
        elif new_num < number: # сдвигаем нижнюю границу вверх
            mn = new_num
        elif new_num > number: # сдвигаем верхнюю границу вниз
            mx = new_num
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(10000))  # загадали список чисел
        
    for number in random_array:
        count_ls.append(random_predict(number))
              
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
