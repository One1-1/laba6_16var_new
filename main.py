"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""


from lab6.my_library import task6_1, task6_2


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        print('программа запустилась')


        match choice:

            case 1:
                file_path = 'lab6\\f.txt'
                task6_1(file_path)

            case 2:
                input_file = 'lab6\\f2.txt'
                output_file = 'lab6\\g2.txt'
                task6_2(input_file, output_file)

            case _:
                break

        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

