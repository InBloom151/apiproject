<h1>REST API для системы комментариев блога</h1>

<h3>Используемые технологии:</h3>
<h4>- Django 4.0.4</h4>
<h4>- Django RESTFramework 3.13.1</h4>
<h4>- Postgresql 14.0</h4>
<h4>- Docker 3.8</h4>

<h2>Запуск проекта:</h2>

Проект запускается на локальном хосте через <b>docker-compose</b>

Поддерживаемые хосты:

    http://127.0.0.1:8000/
    http://localhost:8000/

Все зависимости находятся в файле <b>req.txt</b>

Все данные, необходимые для подключения к БД находятся в файле <b>.env.dev</b>

БД запускается локально и доступна через порт <b>5432</b>

<h2>Список поддерживаемых запросов:</h2>

<h3>api/v1/posts/</h3>

    GET - возвращает список всех постов

    POST - добавляет пост
        {
            "title": title,
            "text": text,
            "user": user_id /опционально
        }

<h3>api/v1/posts/{post_id}/</h3>

    GET - возвращает конкретный пост по id
    
    PATCH - изменяет данные поста по id
        {
            "title": title,
            "text": text,
        }

    DELETE - удаляет конкретный пост по id 

<h3>api/v1/posts/{post_id}/post_comments/</h3>

    GET - Получает ВСЕ комментарии к посту

<h3>api/v1/posts/{post_id}/post_comments_to_third/</h3>

    GET - Получает комментарии к посту ДО третьего уровня вложенности

<h3>api/v1/posts/{post_id}/post_comments_from_third/</h3>

    GET - Получает все вложенные комментарии для комментариев третьего уровня к посту

<h3>api/v1/comments/</h3>

    GET - Получает все комментарии из БД

    POST - Добавляет комментарий
        {
            "text": text,
            "children": [], /здесь будут храниться все дочерние комментарии
            "post": post_id,
            "user": user_id /опционально
            "parent": parent_comment_id /опционально
        }
    

<h3>api/v1/comments/{comment_id}/</h3>

    GET - Получает комментарий по id
    
    PATCH - Изменяет комментарий по id
        {
            "text": text,
        }

    DELETE - Удаляет комментарий по id

<h3>api/v1/comments/comments_to_third/</h3>

    GET - Получает все комментарии до третьего уровня вложенности

<h3>api/v1/comments/comments_from_third/</h3>

    GET - Получает все вложенные комментарии для комментариев третьего уровня
