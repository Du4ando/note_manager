def programm():
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
    notes = []  # Список для хранения заметок

    while True: # Ввод данных для новой заметки
        user_name = input("Введите имя пользователя: ")
        title = input("Введите заголовок заметки: ")
        description = input("Введите описание заметки: ")


        note = {         # Создание словаря для заметки
            "Имя": user_name,
            "Заголовок": title,
            "Описание": description,

        }

        notes.append(note)    # append добавляет заметки в список

        another = input("Хотите добавить еще одну заметку? (да/нет): ")  # Запрос на добавление еще одной заметки
        if another != 'да':
            break

    print("\nСписок заметок:")       # Вывод всех заметок
    for index, note in enumerate(notes, start=1):
        print(f"{index}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")

    while True:
        delete_title = input("Вы хотите удалить заметку? (да/нет): ")
        if delete_title != 'да':
            print("Программа завершена.")
            break

        delete_criteria = input("Введите имя пользователя или заголовок для удаления заметки: ")
        initial_count = len(notes)

        # Удаление заметок по критерию
        notes = [note for note in notes if note['Имя'] != delete_criteria and note['Заголовок'] != delete_criteria]

        if len(notes) < initial_count:
            print("Успешно удалено. Остались следующие заметки:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. Имя: {note['Имя']}")
                print(f"   Заголовок: {note['Заголовок']}")
                print(f"   Описание: {note['Описание']}")

        else:
            print("Заметок с таким именем пользователя или заголовком не найдено.")


programm()







