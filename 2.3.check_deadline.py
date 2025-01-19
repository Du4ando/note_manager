from datetime import datetime
def main():
    date_now = datetime.now()
    print(f"Текущая дата: {date_now.strftime('%d-%m-%Y')}") #Дата из календаря формата (день-месяц-год)
    deadline_str = input('Введиде дату дедлайна (формат: день-месяц-год): ') #Вводим дату дедлайна
    deadline = datetime.strptime(deadline_str, format('%d-%m-%Y')) #Формат строки в число
    if deadline < date_now: #Задаем функции
        delta = date_now - deadline
        print(f"Внимание! Дедлайн истёк {delta.days} дня(ей) назад.")
    elif deadline > date_now:
        delta = deadline - date_now
        print(f"До дедлайна осталось {delta.days} дня(ей).")
main() #Запуск программы
