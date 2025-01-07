'''
-----------Functions-----------
task6_1(file_path)
    Дан файл f, содержащий сведения о веществах: указывается название вещества, его
    удельный вес и проводимость (проводник, полупроводник, изолятор). Найти удельные
    веса и названия всех полупроводников. Предусмотреть обработку всех возможных
    исключительных ситуаций.

task6_2(input_file, output_file)
    Дан текстовый файл f. Создать новый файл g и записать в него построчно все слова
    файла f нечетной длины, предварительно перенеся последнюю букву слова в начало.
    Предусмотреть обработку всех возможных исключительных ситуаций
-------------------------------
'''


def task6_1(file_path):
    '''
    Дан файл f, содержащий сведения о веществах: указывается название вещества, его
    удельный вес и проводимость (проводник, полупроводник, изолятор). Найти удельные
    веса и названия всех полупроводников. Предусмотреть обработку всех возможных
    исключительных ситуаций.

    :param file_path: путь к файлу
    :return: None
    '''
    def read_materials(file_path):
        materials = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # Предполагаем, что данные в файле разделены запятыми
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        print(f"Неверный формат строки: {line.strip()}")
                        continue
                    name, density, conductivity = parts
                    try:
                        density = float(density)
                        materials.append((name.strip(), density, conductivity.strip()))
                    except ValueError:
                        print(f"Неверное значение плотности для вещества: {name.strip()}")
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        return materials

    def find_semiconductors(materials):
        semiconductors = []
        for name, density, conductivity in materials:
            if conductivity.lower() == 'полупроводник':
                semiconductors.append((name, density))
        return semiconductors

    materials = read_materials(file_path)
    semiconductors = find_semiconductors(materials)

    if semiconductors:
        print("Полупроводники:")
        for name, density in semiconductors:
            print(f"Название: {name}, Удельный вес: {density}")
    else:
        print("Полупроводники не найдены.")




def task6_2(input_file, output_file):
    '''
    Дан текстовый файл f. Создать новый файл g и записать в него построчно все слова
    файла f нечетной длины, предварительно перенеся последнюю букву слова в начало.
    Предусмотреть обработку всех возможных исключительных ситуаций

    :param input_file: путь к исходному файлу
    :param output_file: путь, где создать файл g
    :return: None
    '''
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    processed_words = []

    for line in lines:
        words = line.split()
        for word in words:
            if len(word) % 2 != 0:  # Проверка на нечетную длину
                # Перемещение последней буквы в начало
                new_word = word[-1] + word[:-1]
                processed_words.append(new_word)

    try:
        with open(output_file, 'w', encoding='utf-8') as g:
            for word in processed_words:
                g.write(word + '\n')
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")







