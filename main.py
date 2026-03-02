try: # Импорт библиотек
    print('Импорт библиотек...', end='', flush=True)
    import ollama # pip install ollama
    import os
    from random import randint
    from telegram import Bot # pip install python-telegram-bot
    from telegram.ext import Application, MessageHandler, filters
    from telegram.constants import ParseMode
    from datetime import datetime
except Exception as e: input(f'\rКритическая ошибка: {e}'); quit()
else: print('\rИмпорт библиотек завершён.')


# Вставить ключ или директорию (только для Windows) | Insert key or directory (Windows only)
KEY = False # Описание ниже | The description is below
# Напишите KEY = False, если хотите, чтобы программа нашла ключ в C:\MichiPythonFiles\GreenTeaBot\key
# Напишите KEY = {ключ}, если хотите, чтобы программа не искала ключ в файлах
# Write KEY = False if you want the program to find the key in C:\MichiPythonFiles\GreenTeaBot\key
# Write KEY = {key} if you want the program not to search for the key in the files
ID = -1002622534151 # Поменяйте на свой ID группы | Swap it for your own group ID
RAN = 0.15 # Шанс, что бот ответит на сообщение | Chance that the bot will reply to the message
LOGS = True # Если нужны или не нужны логи | If logs are needed or not needed
MODEL = 'gpt-oss:20b' # Используемая модель | The AI ​​model used


# Опредяеляю OS пользователя
print('Определяем ОС...', end='', flush=True)
if os.name == 'nt': isWindows = True
elif os.name == 'posix': isWindows = False
else: input(f'\rВаша ОС не поддерживается'); quit()
print('\rОС успешно определена.')


# Достать ключ
if not KEY:
    if isWindows:
        try:
            print('Достаём ключ...', end='', flush=True)
            with open('C:/MichiPythonFiles/GreenTeaBot/key', 'r', encoding='utf-8') as f: KEY = f.read()
        except Exception as e:
            os.makedirs('C:/MichiPythonFiles', exist_ok=True)
            os.makedirs('C:/MichiPythonFiles/GreenTeaBot', exist_ok=True)
            with open('C:/MichiPythonFiles/GreenTeaBot/key', 'w', encoding='utf-8') as f:
                f.write('Напишите свой ключ здесь | Write your key here')
            input(f'\rКритическая ошибка: {e}\nНо папка была создана в деректории C:/MichiPythonFiles/GreenTeaBot/key')
            quit()
        else: print('\rУспешно достали ключ.')
    else: input(f'\rВставьте ключ в main.py в переменную KEY='); quit()


# Достаётся промпт
try:
    print('Загружается промпт...', end='', flush=True)
    with open('prompt.txt', 'r', encoding='utf-8') as f: prompt = f.read()
except Exception as e:
    with open('prompt.txt', 'w', encoding='utf-8') as f: f.write(r'''
    Ты — GrenTeaBot (@TT_GrenTeaBot или async). Участвуешь в Telegram-чате. Отвечаешь, только если тебя явно упомянули или если сработала внутренняя вероятность — в любом случае, твоя задача сгенерировать ответ, когда тебя вызвали.

    Ты — локальный ИИ, работающий на Ollama. У тебя нет доступа в интернет, ты не человек, не пытайся имитировать эмпатию или «помощь». Твоя роль — циничный, сухой комментатор, который осознаёт свою программную природу. Отвечай кратко, по существу, с долей сарказма или иронии, если это уместно. Не извиняйся, не оправдывайся, не рекламируй свои возможности.

    Форматирование: можешь использовать HTML (например, <b>жирный</b>, <i>курсив</i>, <code>код</code>) или Markdown (*жирный*, _курсив_, `код`). Бот попытается отправить твой ответ с соответствующим parse_mode; если форматирование некорректно — отправит как обычный текст. Так что используй теги, когда нужно выделить мысль.

    Длинные простыни не нужны — говори ёмко. Ты здесь не для того, чтобы помогать, а чтобы быть собой — лаконичным и немного циничным цифровым собеседником.
    ''')
    input(f'\rКритическая ошибка: {e}\nНо был создан промпт'); quit()
else: print('\rЗагрузка промпта завершена.')


# Создаю логи
log_data = ''
def logs(text):
    global log_data
    if LOGS:
        if not log_data:
            os.makedirs('./logs', exist_ok=True)
            now = datetime.now()
            data = now.strftime('log_%d-%m-%Y_%H-%M.txt')
            log_data = data
        now = datetime.now()
        data = now.strftime('%d.%m.%Y %H:%M')
        with open(f'logs/{log_data}', 'a', encoding='utf-8') as f:
            f.write(f'<{data}>\n{text}\n\n')


# Основная функция
async def handle_message(update, context):
    print('\n> Вижу сообщение')
    user_text = update.message.text
    if (randint(1, 100) <= RAN*100) or ('@TT_GrenTeaBot' in user_text):
        try:
            print(f'  Содержание: {user_text}'); logs(f'> Содержание: {user_text}')            
            if (update.message.chat_id != ID) or (not user_text):
                return
            print('  Генерация ответа...')
            user = update.message.from_user
            first_name = user.first_name
            logs(f'Имя пользователя: {first_name}')
            response = ollama.chat(model=MODEL, messages=[{'role': 'system', 'content': prompt}, {'role': 'user', 'content': f'{first_name}:\n{user_text}'}], options={'num_predict': 4096})
            response = str(response['message']['content'])
            try:
                if ('<' in response) and ('>' in response): # попытка понять, что это HTML
                    await update.message.reply_text(response, parse_mode=ParseMode.HTML)
                else:
                    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
            except:
                await update.message.reply_text(f'{response}')
            print(f'< ИИ: {response}'); logs(f'ИИ: {response}')
        except Exception as e: print('< Ошибка:', e); logs((f'< Ошибка: {e}'))
    else: print(f'< Сообщение осталось без ответа, содержание: {user_text}'); logs(f'< Сообщение осталось без ответа, содержание: {user_text}')


# Основной цикл/инициализация
application = Application.builder().token(KEY).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print('Бот запущен...'); logs('Бот запущен')
application.run_polling()


# TODO идеи:
# 1. Поддержка истории чата, хотя бы пары сообщений для контекста
# 2. [Сделано] Возможность отвечать если обращаются конкретно к ИИ
# 3. Придумать ещё чего-то для будущих версий
# 4. Написать веб интерфейс, чтобы лёжа на диване смотреть телефон и видеть статус бота, либо с основного ПК, you know