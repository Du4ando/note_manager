username = input ('имя пользователя:')
title = input ('заголовок заметки:')
content = input ('описание заметки:')
status = input ('статус заметки:')
created_date = input ('дата создания заметки в формате (день-месяц-год):')
issue_date = input('дедлайн в формате (день-месяц-год):')
print(username)
print(title)
print(content)
print(status)
print(created_date[0:5])
print(issue_date[0:5])