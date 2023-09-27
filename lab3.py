import os
import datetime

def main():
    # Ввод имени файла
    input_filename = input("Введите имя файла: ")
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не найден.")
        return
    
    # Задание числа строк на странице печати
    lines_per_page = int(input("Введите число строк на странице печати: "))
    
    # Задание числа пробелов слева на странице
    spaces_per_margin = int(input("Введите число пробелов слева на странице: "))
    
    # Печать текущей даты и времени
    print("Текущая дата и время:", datetime.datetime.now())
    
    # Печать имени файла, даты и времени
    print(f"Имя файла: {input_filename}")
    print("Дата и время:", datetime.datetime.now())
    
    # Вывод на принтер или в другой файл
    output_option = input("Выберите опцию вывода (принтер/файл/экран): ").lower()
    
    if output_option == "принтер":
        # Здесь можно добавить код для отправки на принтер
        print("Печать на принтере...")
    elif output_option == "файл":
        output_filename = input("Введите имя файла для вывода: ")
        with open(output_filename, 'w') as output_file:
            formatted_content = format_text(content, lines_per_page, spaces_per_margin)
            output_file.write(formatted_content)
        print(f"Файл '{output_filename}' успешно создан.")
    elif output_option == "экран":
        formatted_content = format_text(content, lines_per_page, spaces_per_margin)
        print(formatted_content)
    else:
        print("Неверная опция вывода.")

def format_text(text, lines_per_page, spaces_per_margin):
    # Разбиваем текст на строки
    lines = text.split('\n')
    
    formatted_lines = []
    page_number = 1
    
    for line in lines:
        formatted_line = ' ' * spaces_per_margin + line
        formatted_lines.append(formatted_line)
        
        if len(formatted_lines) == lines_per_page:
            # Вставляем номер страницы и перевод страницы
            formatted_lines.append(f"Страница {page_number}\n")
            page_number += 1
    
    formatted_text = '\n'.join(formatted_lines)
    return formatted_text

if __name__ == "__main__":
    main()
