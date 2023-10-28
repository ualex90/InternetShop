import random

from users.models import User

# генератор списка символов (0-9, A-Z, a-z)
ascii_symbols = [chr(i) for i in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))]


def get_user_key():
    """Генератор уникального ключа пользователя"""

    # с целью оптимизации, вызов генератора списка символов производится один раз при запуске функции
    # и полученный список сохраняется в переменную symbols
    symbols = ascii_symbols
    key = ''.join([random.choice(symbols) for i in range(25)])
    # если сгенерированный ключ существует у какого либо из пользователей, генерируем новый
    # до тех пор, пока он не будет уникальным
    while User.objects.filter(key=key):
        key = ''.join([random.choice(symbols) for i in range(25)])

    return key
