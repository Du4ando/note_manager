from datetime import datetime
def create_note():
    date_now = datetime.now()
    date_now = date_now.strftime('%d-%m-%Y')
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    deadline = input("Введите дедлайн (день-месяц-год): ")

    note = {  # Создание словаря для заметки
        "Имя": user_name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": date_now,
        "Дедлайн": deadline
    }
    print("\nЗаметка создана:")  # Вывод всех заметок
    print(f"Имя: {note['Имя']}")
    print(f"Заголовок: {note['Заголовок']}")
    print(f"Описание: {note['Описание']}")
    print(f"Статус: {note['Статус']}")
    print(f"Дата создания: {note['Дата создания']}")
    print(f"Дедлайн: {note['Дедлайн']}\n")

create_note()