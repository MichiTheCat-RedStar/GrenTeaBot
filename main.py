try: # Импорт библиотек
    print('Импорт библиотек...', end='', flush=True)
    import ollama # pip install ollama
    import asyncio
    import os
    from random import randint
    from telegram import Bot # pip install python-telegram-bot
    from telegram.ext import Application, MessageHandler, filters
except Exception as e: input('\rКритическая ошибка:', e); quit()
else: print('\rИмпорт библиотек завершён.')


# Вставить ключ или директорию (только для Windows) | Insert key or directory (Windows only)
KEY = False # Описание ниже | The description is below
# Напишите KEY = False, если хотите, чтобы программа нашла ключ в C:\MichiPythonFiles\GreenTeaBot\key
# Напишите KEY = {ключ}, если хотите, чтобы программа не искала ключ в файлах
# Write KEY = False if you want the program to find the key in C:\MichiPythonFiles\GreenTeaBot\key
# Write KEY = {key} if you want the program not to search for the key in the files
ID = -1002622534151 # Поменяйте на свой | Swap it for your own


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


# Основной цикл
async def handle_message(update, context):
    if update.message.chat_id != ID:
        return

    user_text = update.message.text
    if not user_text:
        return

    reply_text = f"Вы написали: {user_text}"

    await update.message.reply_text(reply_text)

def main():
    application = Application.builder().token(KEY).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен и слушает сообщения в группе...")
    application.run_polling()


main()


# >> https://t.me/c/2622534151/20065
# > Сначала научился писать сообщение в чат, потом научился доставать сообщения и возвращать их с ответом.. Теперь осталось подключить Ollama  и дописать рандом