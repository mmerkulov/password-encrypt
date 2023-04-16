import getpass
from pathlib import Path
import os
import string
import pyAesCrypt
from random import choice


def get_relative_path(file_name: str = 'data.txt') -> str:
    """
    Получение относительного пути, простой пример, т.к. файлы все находятся
    в корне, в более сложных примерах нужно добавлять "пути" по кусочкам в
    abspath,
        example:
            Path(os.path.abspath(current_dir.joinpath('..', '..', 'external_files')))
    :param file_name: имя файла, которое нужно найти
    :return: относительный путь до файла
    """
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    abs_path = os.path.abspath(current_dir.joinpath(file_name))
    relative_path_file = os.path.relpath(abs_path)
    return relative_path_file


def generate_random_text(length: int) -> str:
    """
    Генерируем текст
    :param length: количество символов в тексте
    :return: сгенированный текст длиной length
    """
    text_generator = [choice(string.ascii_letters +
                             string.ascii_lowercase +
                             string.ascii_uppercase +
                             string.hexdigits) for _ in range(length)]
    return ''.join(text_generator)


def filling_file(length: int = 1000) -> None:
    """
    Заполняем файл
    :return:
    """
    relative_path_file = get_relative_path(file_name='data.txt')

    with open(relative_path_file, 'w+') as file:
        file.write(generate_random_text(length=length))


filling_file(length=2000)

# input shadow password
password = getpass.getpass(prompt='Input your password: ')
print('Password written down')

# encrypt my data
pyAesCrypt.encryptFile(infile=get_relative_path(file_name='data.txt'),
                       outfile='data.txt.aes', #TODO можно сделать более универсально
                       passw=password)
