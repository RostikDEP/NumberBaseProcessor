import pyexcel as pe
import os
import sys

def create_excel_from_text_file(file_path):
    # Перевіряємо, чи існує файл
    if not os.path.exists(file_path):
        print("Файл не знайдено.")
        return

    # Отримуємо дані з файлу
    with open(file_path, 'r', encoding='utf-8') as file:
        data = [line.strip().split('-') for line in file.readlines()]

    # Створюємо екземпляр DataSheet
    sheet = pe.Sheet(data)

    # Створюємо папку для збереження excel файлів, якщо вона не існує
    folder_path = 'sheets'
    os.makedirs(folder_path, exist_ok=True)

    # Зберігаємо DataSheet у вигляді excel файлу
    excel_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.xlsx'
    excel_file_path = os.path.join(folder_path, excel_file_name)
    sheet.save_as(excel_file_path)

    print(f"Excel файл збережено у '{excel_file_path}'.")

if __name__ == "__main__":
    # Перевіряємо, чи був переданий аргумент командного рядка
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до файлу тексту як аргумент командного рядка.")
    else:
        file_path = sys.argv[1]
        create_excel_from_text_file(file_path)
