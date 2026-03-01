try: # Импорт библиотек
    print('Импорт библиотек...', end='', flush=True)
    import ollama # pip install ollama
    import os
    from random import randint
    from telegram import Bot # pip install python-telegram-bot
    from telegram.ext import Application, MessageHandler, filters
    from datetime import datetime
except Exception as e: input('\rКритическая ошибка:', e); quit()
else: print('\rИмпорт библиотек завершён.')


# Вставить ключ или директорию (только для Windows) | Insert key or directory (Windows only)
KEY = False # Описание ниже | The description is below
# Напишите KEY = False, если хотите, чтобы программа нашла ключ в C:\MichiPythonFiles\GreenTeaBot\key
# Напишите KEY = {ключ}, если хотите, чтобы программа не искала ключ в файлах
# Write KEY = False if you want the program to find the key in C:\MichiPythonFiles\GreenTeaBot\key
# Write KEY = {key} if you want the program not to search for the key in the files
ID = -1002622534151 # Поменяйте на свой ID группы | Swap it for your own group ID
RAN = 0.1 # Шанс, что бот ответит на сообщение | Chance that the bot will reply to the message
LOGS = True # Если нужны или не нужны логи | If logs are needed or not needed


# Достать ключ
if not KEY:
    try:
        print('Достаём ключ...', end='', flush=True)
        with open('C:/MichiPythonFiles/GreenTeaBot/key', 'r', encoding='utf-8') as f: KEY = f.read()
    except Exception as e:
        os.makedirs('C:/MichiPythonFiles', exist_ok=True)
        os.makedirs('C:/MichiPythonFiles/GreenTeaBot', exist_ok=True)
        with open('C:/MichiPythonFiles/GreenTeaBot/key', 'w', encoding='utf-8') as f:
            f.write('Напишите свой ключ здесь | Write your key here')
        input(f'\rКритическая ошибка: {e}\nНо папка была создана в деректории C:/MichiPythonFiles/GreenTeaBot/key')
        quit
    else: print('\rУспешно достали ключ.')


# Создаю логи
log_data = ''
def logs(text):
    global log_data
    if LOGS:
        if not log_data:
            now = datetime.now()
            data = now.strftime('log_%d-%m-%Y_%H-%M.txt')
            log_data = data
        now = datetime.now()
        data = now.strftime("%d.%m.%Y %H:%M")
        with open(f'logs/{log_data}', 'a', encoding='utf-8') as f:
            f.write(f'<{data}>\n{text}\n\n')


# Основная функция
async def handle_message(update, context):
    print('\n> Вижу сообщение')
    if (_ := randint(0, int(RAN*100))) == 0:
        try:
            if update.message.chat_id != ID:
                return
            user_text = update.message.text
            print(f'  Содержание: {user_text}'); logs(f'> Содержание: {user_text}')
            if not user_text:
                return
            reply_text = f"Вы написали: {user_text}"
            await update.message.reply_text(reply_text)
        except Exception as e: print('< Ошибка:', e); logs((f'< Ошибка: {e}'))
    else: print(f'< Сообщение осталось без ответа: {_} != 0'); logs('< Сообщение осталось без ответа')


# Основной цикл/инициализация
application = Application.builder().token(KEY).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print("Бот запущен..."); logs('Бот запущен')
application.run_polling()