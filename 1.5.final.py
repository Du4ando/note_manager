username = input ('Введите имя пользователя:')
title = input ('Введите заголовок заметки:')
subtitle1 = input('Введите подзаголовок №1')
subtitle2 = input('Введите подзаголовок №2')
subtitle3 = input('Введите подзаголовок №3')
subtitles = [subtitle1, subtitle2 , subtitle3]
content = input ('описание заметки:')
status = input ('статус заметки:')
created_date = input ('дата создания заметки в формате (день-месяц-год):')
issue_date = input('дедлайн в формате (день-месяц-год):')

note = [username,
        content,
        status,
        created_date,
        issue_date,
        title,subtitles
        ]
print(*note, sep='\n')
