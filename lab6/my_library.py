def prisv(f, g):
    try:
        # Открываем файл g для чтения
        file_g = open(g, 'r')
        numbers = []

        # Читаем все строки и преобразуем их в список целых чисел
        for line in file_g:
            numbers.append(int(line.strip()))

        file_g.close()

        # Проверяем, что в списке достаточно элементов
        if len(numbers) < 3:
            raise ValueError("В файле g должно быть как минимум 3 числа для исключения максимального и минимального.")

        # Находим максимальный и минимальный элементы
        max_num = max(numbers)
        min_num = min(numbers)

        # Создаем новый список для отфильтрованных чисел
        filtered_numbers = []
        for num in numbers:
            if num != max_num and num != min_num: # исключаем максимальный и минимальный элемент
                filtered_numbers.append(num)

        # Открываем файл f для записи
        file_f = open(f, 'w')

        # Записываем отфильтрованные числа в файл f
        for number in filtered_numbers:
            file_f.write(f"{number}\n")

        file_f.close()

    # обработка ошибок
    except FileNotFoundError:
        print(f"Ошибка: Файл {g} не найден.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")




def task6_2(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Переменная для хранения отформатированного текста
    formatted_lines = []
    current_line = ""

    # Разбиваем текст на слова
    words = text.split()

    for word in words:
        # Проверяем, если добавление слова не превышает 60 символов
        if len(current_line) + len(word) + 1 <= 60:
            if current_line:  # Если текущая строка не пустая, добавляем пробел
                current_line += " "
            current_line += word
        else:
            # Если текущая строка заканчивается на точку, добавляем её в список
            if current_line.endswith('.'):
                formatted_lines.append(current_line)
                current_line = word  # Начинаем новую строку с текущего слова
            else:
                # Если текущая строка не заканчивается на точку, добавляем её в список
                formatted_lines.append(current_line)
                current_line = word  # Начинаем новую строку с текущего слова

        # Если текущая строка достигла 60 символов, добавляем её в список
        if len(current_line) == 60:
            formatted_lines.append(current_line)
            current_line = ""

    # Добавляем последнюю строку, если она не пустая
    if current_line:
        formatted_lines.append(current_line)

    # Записываем отформатированный текст в выходной файл
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in formatted_lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")



