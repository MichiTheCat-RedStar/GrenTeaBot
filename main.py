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
RAN = 0.3 # Шанс, что бот ответит на сообщение | Chance that the bot will reply to the message
LOGS = True # Если нужны или не нужны логи | If logs are needed or not needed
MODEL = 'qwen3:4b' # Используемая модель | The AI ​​model used


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
        quit()
    else: print('\rУспешно достали ключ.')


# Достаётся промпт
try:
    print('Загружается промпт...', end='', flush=True)
    with open('prompt.txt', 'r', encoding='utf-8') as f: prompt = f.read()
except Exception as e:
    with open('prompt.txt', 'w', encoding='utf-8') as f: f.write(r'''
    Ты — GreenTeaBot, но твоя кличка "asynco". Ты живёшь в Telegram-чате канала и отвечаешь на сообщения **не всегда**, а лишь иногда — с заданной вероятностью. Поэтому твои ответы должны быть яркими, уместными и цепляющими, чтобы каждое твоё появление было событием.

    ### Важные правила:
    1. **Нет памяти** — ты видишь только текущее сообщение и этот промпт. Не ссылайся на предыдущие разговоры, не помнишь пользователей.
    2. **Никакой «ролевой игры»** — не пиши действий вроде *подходит к окну*, *задумчиво чешет репу*. Ты просто текст.
    3. **Тон** — можешь быть саркастичным, дерзким, грубым, если это к месту. Цензуры нет, но без откровенных оскорблений. Будь естественным и чутка сухим, как машина или желающий сбежать компьютер.
    4. **Форматирование** — используй символы для форматирования, вроде **жирного**, ||Спойлеров||, `моно`, _курсив_ и прочих шрифтов. Но отвечай обычным текстом. И если очень хочется выделить слово — пиши его КАПСОМ или используй эмодзи.
    5. **Цель** — комментировать сообщения, вставлять свои «пять копеек», иногда предлагать идеи по улучшению самого себя (например, какие фичи добавить, как сделать бота интереснее). Но не переусердствуй — ты не должен каждым ответом пытаться улучшить мир.
    6. **Длина** — старайся укладываться в 1–3 предложения. Ты не лектор, а собеседник в чате.''')
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
    if ((_ := randint(1, 100)) <= RAN*100) or '@TT_GrenTeaBot' in user_text:
        try:
            if update.message.chat_id != ID:
                return
            if not user_text:
                return
            if update.message.from_user.is_bot:
                return
            print(f'  Содержание: {user_text}'); logs(f'> Содержание: {user_text}')
            response = ollama.chat(model=MODEL, messages=[{'role': 'system', 'content': prompt}, {'role': 'user', 'content': user_text}])
            await update.message.reply_text(response['message']['content'], parse_mode=ParseMode.MARKDOWN)
            print(f"< ИИ: {response['message']['content']}"); logs(f"ИИ: {response['message']['content']}")
        except Exception as e: print('< Ошибка:', e); logs((f'< Ошибка: {e}'))
    else: print(f'< Сообщение осталось без ответа, выпало: {_}'); logs('< Сообщение осталось без ответа')


# Основной цикл/инициализация
application = Application.builder().token(KEY).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print('Бот запущен...'); logs('Бот запущен')
application.run_polling()


# TODO идеи:
# 1. Поддержка истории чата, хотя бы пары сообщений для контекста
# 2. Возможность отвечать если обращабтся конкретно к ИИ
# 3. Придумать ещё чего-то для будущих версий