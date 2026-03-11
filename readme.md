[![Telegram](https://img.shields.io/badge/Telegram-@TeaTechnology-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TeaTechnology)
[![GitHub](https://img.shields.io/badge/GitHub-MichiTheCat--RedStar-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MichiTheCat-RedStar)
[![Itch.io](https://img.shields.io/badge/Itch.io-michi--the--cat-FA5C5C?style=for-the-badge&logo=itch.io&logoColor=white)](https://michi-the-cat.itch.io)

# GreenTeaBot — Telegram AI с локальной нейросетью
## Русский

Бот для Telegram, который отвечает на сообщения **не всегда**, а с заданной вероятностью. Использует локальную модель через [Ollama](https://ollama.com) и не требует интернета для генерации ответов. Идеально подходит для уютных чатов, где хочется видеть остроумные комментарии от ИИ.

---

### Возможности
- **Вероятностные ответы** — можно настроить шанс ответа (по умолчанию 15%).
- **Обязательный ответ при упоминании** — если в сообщении есть `@TT_GrenTeaBot`, бот ответит всегда.
- **Логирование** — все диалоги и ошибки сохраняются в папку `logs` (можно отключить).
- **Гибкая настройка модели** — легко сменить модель Ollama, отредактировав параметр `Model` в файле `settings.toml`.
- **Автосоздание ключа** — если ключ не указан в `settings.toml`, бот создаст папку и файл-заготовку для ключа.
- **Поддержка разных промптов** — можно подготовить несколько вариантов (например, для маленьких моделей) и переключаться между ними через параметр `Prompt`.
- **Обработка ошибок форматирования** — пытается отправить ответ в HTML, затем в Markdown, иначе оборачивает в моноширинный блок.

### Требования
- Python **3.11** или выше (из-за использования встроенного модуля `tomllib`)
- Установленная и запущенная [Ollama](https://ollama.com) с загруженной моделью
- Telegram Bot Token (получить у [@BotFather](https://t.me/BotFather))
- ID группы/канала, куда будет добавлен бот

### Установка и настройка
1. **Клонируйте репозиторий** (или просто сохраните `main.py`, папку `prompts` и файл `settings.toml`).
2. **Установите зависимости**:
   ```bash
   pip install python-telegram-bot ollama
   ```
3. **Настройте бота**:
   - Откройте файл `settings.toml`.
   - В секции `[Bot]` укажите:
     - `Key` — можно вписать токен прямо в кавычках (`Key = "ваш_токен"`) или оставить `false`, тогда бот попытается прочитать ключ из файла `C:/MichiPythonFiles/GreenTeaBot/key` (на Windows).
     - `ID` — числовой идентификатор чата (группы или канала), где бот будет отвечать.
     - `BotUsername` — юзернейм вашего бота (например, `"TT_GrenTeaBot"`).
     - `Random` — вероятность ответа от 0.0 до 1.0 (например, `0.15` = 15%).
   - В секции `[Ollama]` укажите:
     - `Model` — имя модели, установленной в Ollama (например, `"llama3:8b"`).
     - `CPU` — количество потоков процессора (оставьте `false` для автоматического выбора).
     - `Prompt` — имя файла с промптом из папки `prompts` (без расширения `.txt`), например `"Prompt-8b+RU"`.
   - В секции `[Script]` включите или отключите логирование (`Logs = true`).
   - В секции `[Translation]` можно включить автоматический перевод сообщений (полезно для маленьких моделей).
4. **Запустите бота**:
   ```bash
   python main.py
   ```

Все основные настройки теперь хранятся в одном файле `settings.toml` с поддержкой комментариев.

---

# GreenTeaBot — Telegram AI with a local neural network
## English

A Telegram bot that replies to messages **not always**, but with a set probability. It uses a local model via [Ollama](https://ollama.com) and doesn't require an internet connection to generate responses. Ideal for cozy chats where you want to see witty comments from the AI.

---

### Features
- **Probabilistic responses** — you can configure the response probability (default is 15%).
- **Required reply when mentioned** — if the message contains `@TT_GrenTeaBot`, the bot will always reply.
- **Logging** — all dialogs and errors are saved in the `logs` folder (can be disabled).
- **Flexible model customization** — easily change the Ollama model by editing the `Model` parameter in the `settings.toml` file.
- **Auto-generation of key** — if the key is not provided in `settings.toml`, the bot will create a folder and a template key file.
- **Support for multiple prompts** — you can prepare several prompt variants (for example, for small models) and switch between them via the `Prompt` parameter.
- **Formatting error handling** — attempts to send a response in HTML, then in Markdown; otherwise, it wraps it in a monospace block.

### Requirements
- Python **3.11** or higher (due to the built-in `tomllib` module)
- [Ollama](https://ollama.com) installed and running with a downloaded model
- Telegram Bot Token (obtain from [@BotFather](https://t.me/BotFather))
- ID of the group/channel where the bot will be added

### Installation and Configuration
1. **Clone the repository** (or simply save `main.py`, the `prompts` folder, and the `settings.toml` file).
2. **Install dependencies**:
   ```bash
   pip install python-telegram-bot ollama
   ```
3. **Configure the bot**:
   - Open the `settings.toml` file.
   - In the `[Bot]` section, set:
     - `Key` — either put your token in quotes (`Key = "your_token"`) or leave `false`; the bot will then try to read the key from `C:/MichiPythonFiles/GreenTeaBot/key` (on Windows).
     - `ID` — the numeric ID of the chat (group or channel) where the bot will operate.
     - `BotUsername` — your bot's username (e.g., `"TT_GrenTeaBot"`).
     - `Random` — response probability from 0.0 to 1.0 (e.g., `0.15` = 15%).
   - In the `[Ollama]` section, set:
     - `Model` — the name of the model installed in Ollama (e.g., `"llama3:8b"`).
     - `CPU` — number of CPU threads (leave `false` for auto-detection).
     - `Prompt` — the name of the prompt file from the `prompts` folder (without the `.txt` extension), e.g., `"Prompt-8b+EN"`.
   - In the `[Script]` section, enable or disable logging (`Logs = true`).
   - In the `[Translation]` section, you can enable automatic message translation (useful for small models).
4. **Run the bot**:
   ```bash
   python main.py
   ```

All main settings are now stored in a single `settings.toml` file with comment support.