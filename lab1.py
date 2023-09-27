import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def sum_upper_triangle(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            total_sum += matrix[i][j]
    return total_sum

def max_elements_in_each_row(matrix):
    max_elements = []
    for row in matrix:
        max_element = max(row)
        max_elements.append(max_element)
    return max_elements

def max_column_sum(matrix):
    max_sum = float('-inf')
    for j in range(len(matrix[0])):
        column_sum = sum(matrix[i][j] for i in range(len(matrix)))
        max_sum = max(max_sum, column_sum)
    return max_sum

def calculate():
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            entry_value = entry_widgets[i][j].get()
            try:
                value = float(entry_value)
                row.append(value)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите числовые значения.")
                return
        matrix.append(row)
    
    upper_triangle_sum = sum_upper_triangle(matrix)
    max_elements = max_elements_in_each_row(matrix)
    max_column = max_column_sum(matrix)
    
    result_text = f"Сумма элементов верхней треугольной матрицы: {upper_triangle_sum}\n"
    result_text += "Наибольшие элементы в каждой строке матрицы:\n"
    for i, max_element in enumerate(max_elements):
        result_text += f"Строка {i + 1}: {max_element}\n"
    result_text += f"Наибольшая сумма элементов столбцов матрицы: {max_column}"

    result_label.config(text=result_text)

def clear_entries():
    for i in range(rows):
        for j in range(columns):
            entry_widgets[i][j].delete(0, tk.END)

def create_matrix_input():
    global rows, columns, entry_widgets
    rows = int(rows_entry.get())
    columns = int(columns_entry.get())
    
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    
    entry_widgets = []
    for i in range(rows):
        row_widgets = []
        for j in range(columns):
            entry = ttk.Entry(matrix_input_frame, width=10)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_widgets.append(entry)
        entry_widgets.append(row_widgets)

# Создание основного окна
root = tk.Tk()
root.title("Вычисления с матрицей")

# Создание верхней панели
top_frame = ttk.Frame(root)
top_frame.pack(padx=10, pady=10)

ttk.Label(top_frame, text="Строки:").grid(row=0, column=0)
rows_entry = ttk.Entry(top_frame, width=5)
rows_entry.grid(row=0, column=1)

ttk.Label(top_frame, text="Столбцы:").grid(row=0, column=2)
columns_entry = ttk.Entry(top_frame, width=5)
columns_entry.grid(row=0, column=3)

create_matrix_button = ttk.Button(top_frame, text="Создать матрицу", command=create_matrix_input)
create_matrix_button.grid(row=0, column=4)

# Создание рамки для ввода матрицы
matrix_input_frame = ttk.Frame(root)
matrix_input_frame.pack(padx=10, pady=10)

# Создание кнопок
calculate_button = ttk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

clear_button = ttk.Button(root, text="Очистить", command=clear_entries)
clear_button.pack()

# Создание метки для вывода результата
result_label = ttk.Label(root, text="")
result_label.pack(padx=10, pady=10)

root.mainloop()