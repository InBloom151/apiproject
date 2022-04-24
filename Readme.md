#REST API для системы комментариев блога

###Используемые технологии:
###- Django 4.0.4
###- Django RESTFramework 3.13.1
###- Postgresql 14.0
###- Docker 3.8

##Запуск проекта:

Проект запускается на локальном хосте через docker-compose

Поддерживаемые хосты:

    http://127.0.0.1:8000/
    http://localhost:8000/

Все зависимости находятся в файле req.txt

Все данные, необходимые для подключения к БД находятся в файле .env.dev

БД запускается локально и доступна через порт 5432

##Список поддерживаемых запросов:

###api/v1/posts/
    GET - возвращает список всех постов

    POST - добавляет пост
        {
            "title": title,
            "text": text,
            "user": user_id /опционально
        }

###api/v1/posts/{post_id}/
    GET - возвращает конкретный пост по id
    
    PATCH - изменяет данные поста по id
        {
            "title": title,
            "text": text,
        }

    DELETE - удаляет конкретный пост по id 

###api/v1/posts/{post_id}/post_comments
    GET - Получает ВСЕ комментарии к посту

###api/v1/posts/{post_id}/post_comments_to_third
    GET - Получает комментарии к посту ДО третьего уровня вложенности

###api/v1/posts/{post_id}/post_comments_from_third
    GET - Получает все вложенные комментарии для комментариев третьего уровня к посту

###api/v1/comments/
    GET - Получает все комментарии из БД

    POST - Добавляет комментарий
        {
            "text": text,
            "children": [], /здесь будут храниться все дочерние комментарии
            "post": post_id,
            "user": user_id /опционально
            "parent": parent_comment_id /опционально
        }
    

###api/v1/comments/{comment_id}
    GET - Получает комментарий по id
    
    PATCH - Изменяет комментарий по id
        {
            "text": text,
        }

    DELETE - Удаляет комментарий по id

###api/v1/comments/comments_to_third
    GET - Получает все комментарии до третьего уровня вложенности

###api/v1/comments/comments_from_third
    GET - Получает все вложенные комментарии для комментариев третьего уровня