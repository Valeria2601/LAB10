import random
import logging

# настройка логгера
logging.basicConfig(filename='guess_the_number.log', level=logging.INFO)

def guess_the_number(N, k):
    # загадываем число от 1 до N
    number = random.randint(1, N)
    logging.info(f'Было загадано число: {number}')
    
    # цикл для k попыток отгадать число
    for i in range(k):
        # просим пользователя ввести число
        user_number = int(input(f"Попытка {i+1}. Введите число от 1 до {N}: "))
        logging.info(f'Попытка {i+1}. Пользователь ввел число: {user_number}')
        
        # проверяем, угадал ли пользователь число
        if user_number == number:
            print("Вы угадали!")
            logging.info('Игрок угадал число')
            return
        elif user_number < number:
            print("Загаданное число больше")
            logging.info('Загаданное число больше, чем введенное игроком')
        else:
            print("Загаданное число меньше")
            logging.info('Загаданное число меньше, чем введенное игроком')
    
    # если пользователь не угадал за k попыток
    print("Попытки закончились. Было загадано число", number)
    logging.info('Попытки закончились')

# диалог с пользователем для ввода данных
try:
    N = int(input("Введите верхнюю границу диапазона (натуральное число): "))
    k = int(input("Введите количество попыток (натуральное число): "))
    
    # вызываем функцию отгадывания числа
    guess_the_number(N, k)
except ValueError:
    print("Ошибка: введите натуральное число")
    logging.error('Ошибка: введено некорректное значение')
