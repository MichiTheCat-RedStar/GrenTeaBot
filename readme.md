[![Telegram](https://img.shields.io/badge/Telegram-@TeaTechnology-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TeaTechnology)
[![GitHub](https://img.shields.io/badge/GitHub-MichiTheCat--RedStar-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MichiTheCat-RedStar)
[![Itch.io](https://img.shields.io/badge/Itch.io-michi--the--cat-FA5C5C?style=for-the-badge&logo=itch.io&logoColor=white)](https://michi-the-cat.itch.io)


# Русский | Russian
## Задачи

- Проект представляет собой маленькую модель ИИ, завёрнутую в код таким образом, чтобы она могла отвечать на сообщения... Специально предназначена для чата [моего канала](https://t.me/TeaTechnology)

- Сервер рабоатет на Xubuntu, поэтому нужна кросплатформенность, учитывая, что я программирую на Windows

- Используются [`Ollma`](https://github.com/ollama/ollama) в связке с [`python-telegram-bot`](https://pypi.org/project/python-telegram-bot/) на базе Python 3.13

## Принцип работы

Пока что предполагаю, что принцип работы будет устроен так:

1. Скрипт мониторит чат 24/7

2. Скрипт вызывает функцию каждый раз, как видит, что кто-то прислал сообщение

3. Функция вызывает `random.randint` в диапозоне от 0 до 100, условно

4. Когда выпадает 0, то функция передаёт запрос [`Ollma`](https://github.com/ollama/ollama) и заставляет выбранную модель генерировать ответ

---
**Для работы | For works**
```bash
pip install python-telegram-bot ollama
```

# English | Английский
## Tasks

- The project is a small AI model wrapped in code so that it can respond to messages... Specifically designed for the chat of [my channel](https://t.me/TeaTechnology)

- The server runs on Xubuntu, so cross-platform compatibility is needed, considering that I program on Windows

- It uses [`Ollama`](https://github.com/ollama/ollama) in conjunction with [`python-telegram-bot`](https://pypi.org/project/python-telegram-bot/) based on Python 3.13

## Operating Principle

For now, I assume the operating principle will be structured as follows:

1. The script monitors the chat 24/7

2. The script calls a function every time it sees that someone has sent a message

3. The function calls `random.randint` in a range from 0 to 100, conditionally

4. When 0 comes up, the function passes the request to [`Ollama`](https://github.com/ollama/ollama) and forces the selected model to generate a response