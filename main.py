VERSION = 'v1.3b'

try: # Импорт библиотек
    print('Импорт библиотек...', end='', flush=True)
    import ollama # pip install ollama
    import os
    from random import randint
    from telegram import Bot # pip install python-telegram-bot
    from telegram.ext import Application, MessageHandler, filters
    from telegram.constants import ParseMode
    from datetime import datetime
    try: import tomllib
    except ModuleNotFoundError: import tomli as tomllib; print('\rtomlib заменён на tomli.') # pip install tomli если ваш python не имеет tomlib
except Exception as e: input(f'\rКритическая ошибка: {e}'); quit()
else: print('\rИмпорт библиотек завершён.')


try: # Импор settings.toml
    print('Загрузка настроек...', end='', flush=True)
    with open('settings.toml', 'rb') as f:
        data = tomllib.load(f)
        KEY = data['Bot']['Key']
        ID = data['Bot']['ID']
        RAN = data['Bot']['Random']
        LOGS = data['Script']['Logs']
        MODEL = data['Ollama']['Model']
        CPU = data['Ollama']['CPU']
        prompt = data['Ollama']['Prompt']
        translation = data['Translation'] # TODO: сделать функцию перевода
        BOT = data['Bot']['BotUsername']
        HISTORY = data['Ollama']['History']
    # Все настройки были перенесены в файл settings.toml
    # All settings have been moved to the settings.toml file
except Exception as e: input(f'\rКритическая ошибка: {e}'); quit()
else: print('Загрузка настроек завершена.')


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
    else: input(f'\rВставьте ключ в settings.toml в переменную Key = "ваш_ключ"'); quit()


try: # Достаётся промпт
    print('Загружается промпт...', end='', flush=True)
    with open(f'prompts/{prompt}.txt', 'r', encoding='utf-8') as f: prompt = f.read()
except Exception as e: input(f'\rКритическая ошибка: {e}'); quit()
else: print('\rЗагрузка промпта завершена.')


# Проверяею ядра
if not CPU: CPU = None


# История
history = []


# Never Wanted To Dance !!!
# Сколько я библиотек не перебирал, сменив уже три - везде либо документация устаревшая и сейчас работает вообще не так модуль, либо ошибка 502, либо "Слишком много запросов", когда он единственный.. Короче я выгорел
# То, что вы видите ниже - это конечно не код, который был изначально, тут сборная солянка из теста трёх библиотек, поэтому это и выглядит так... Хотя не работает оно вообще никак даже в исправленном виде
r'''
translation['Translate'] = True
try: # Инициализируется переводчик
    if translation['Translate']:
        print('Загружается переводчик...', end='', flush=True)
        import translators as translator
        print(translator.translate_text('Привет'))
        if translation['Engien'] == 'Google':
            def translate(text, lang): return translator.google(text, lang)
        elif translation['Engien'] == 'DeepL':
            def translate(text, lang): return translator.deepl(text, lang)
        elif translation['Engien'] == 'Amazon':
            def translate(text, lang): return translator.amazon(text, lang)
        elif translation['Engien'] == 'ModernMT':
            def translate(text, lang): return translator.modern_mt(text, lang)
        elif translation['Engien'] == 'LibreTranslate':
            def translate(text, lang): return translator.libre(text, lang)
        else: input(f'\rДвижок переводчика задан неправильно.'); quit()
except Exception as e: input(f'\rКритическая ошибка: {e}'); quit()
else: print('\rЗагрузка переводчика завершена.')

print(translate('Привет, Мир!', 'en'))
quit()'''


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
    try:
        print('\n> Вижу сообщение')
        try:
            user_text = update.message.text
            user = update.message.from_user
            first_name = user.first_name
            print('  Сообщение от', first_name)
        except: user_text = ''
        if (randint(1, 100) <= RAN*100) or (f'@{BOT}' in user_text):
            try:
                print(f'  Содержание: {user_text}'); logs(f'> Содержание: {user_text}')            
                if (update.message.chat_id != ID) or (not user_text):
                    return
                print('  Генерация ответа...')
                user = update.message.from_user
                first_name = user.first_name
                logs(f'Имя пользователя: {first_name}')
                # full_history = [{'role': 'system', 'content': prompt}, history, {'role': f'user "{first_name}"', 'content': user_text}]
                full_history = [{'role': 'system', 'content': prompt}, {'role': 'user', 'content': user_text}]
                response = ollama.chat(model=MODEL, messages=full_history, options={'num_predict': 4096, "num_thread": CPU})
                logs(f'ИИ внутрянка: {response}')
                response = str(response['message']['content'])
                try:
                    if any(tag in response for tag in ['<b>', '<i>', '<u>', '<s>', '<a', '<code>', '<pre>']): # попытка понять, что это HTML
                        await update.message.reply_text(response, parse_mode=ParseMode.HTML)
                    else:
                        await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
                except:
                    await update.message.reply_text(response)
                print(f'< ИИ: {response}'); logs(f'ИИ: {response}')
            except Exception as e: print('< Ошибка:', e); logs(f'< Ошибка: {e}')
        else: print(f'< Сообщение осталось без ответа, содержание: {user_text}'); logs(f'< Сообщение осталось без ответа, содержание: {user_text}')
    except Exception as e: logs(f'Критическая ошибка:\n{e}'); input(f'\nКритическая ошибка:\n{e}')


# Основной цикл/инициализация
logs(f'Версия: {VERSION}\n\nНастройки:\nШанс = {RAN*100}%\nМодель = {MODEL}\nЯдер = {CPU}\nWindows = {isWindows}')
application = Application.builder().token(KEY).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print('Бот запущен...\nВерсия', VERSION); logs('Бот запущен')
application.run_polling()


# TODO 2 сделать сейчас:
# [Сделано] Вынести настройки в TOML файл (Так как он как ini, но поддерживает комментарии через '#')
# [Сделано] Добавить папку Prompts с выборами из Prompt-8b+RU|Prompt-4b-RU|Prompt-8b+EN|Prompt-4b-EN для больших и маленький РУ и АНГ моделей
#   Добавить функцию/настройку, при включении которой через переводчик будет перевод и в настройках показывало на какой язык этот перевод (система язык пользователя -> английский для ИИ -> язык пользователя)
#   Написать интерфейс на streamlit, чтобы через localhost следить за статусом ИИ
#   Сделать поддержку линии мыслей (теперь я придумал как это сделать: запоминать последнии пять сообщений, добавляя их в history)
# [Сделано] Удалить предыдущий TODO
# [Сделано] Исправить readme.md
# [Сделано] Добавить натсройку BotUsername = "TT_GrenTeaBot"
# [Сделано] Прочитать TODO из settings.toml
#   Сделать TODO 3