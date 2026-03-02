[![Telegram](https://img.shields.io/badge/Telegram-@TeaTechnology-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TeaTechnology)
[![GitHub](https://img.shields.io/badge/GitHub-MichiTheCat--RedStar-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MichiTheCat-RedStar)
[![Itch.io](https://img.shields.io/badge/Itch.io-michi--the--cat-FA5C5C?style=for-the-badge&logo=itch.io&logoColor=white)](https://michi-the-cat.itch.io)

# GreenTeaBot — Telegram AI с локальной нейросетью
## Русский | Russian

Бот для Telegram, который отвечает на сообщения **не всегда**, а с заданной вероятностью. Использует локальную модель через [Ollama](https://ollama.com) и не требует интернета для генерации ответов. Идеально подходит для уютных чатов, где хочется видеть остроумные комментарии от ИИ.

---

### Возможности
- **Вероятностные ответы** — можно настроить шанс ответа (по умолчанию 30%).
- **Обязательный ответ при упоминании** — если в сообщении есть `@TT_GrenTeaBot`, бот ответит всегда.
- **Логирование** — все диалоги и ошибки сохраняются в папку `logs` (можно отключить).
- **Гибкая настройка модели** — легко сменить модель Ollama, отредактировав переменную `MODEL`.
- **Автосоздание ключа и промпта** — если файлы отсутствуют, бот создаст их сам.
- **Обработка ошибок форматирования** — пытается отправить ответ в HTML, затем в Markdown, иначе оборачивает в моноширинный блок.
- **Поддержка разных промптов** — можно подготовить несколько вариантов (например, для маленьких моделей) и переключаться между ними.

### Требования
- Python 3.7+
- Установленная и запущенная [Ollama](https://ollama.com)
- Telegram Bot Token (получить у [@BotFather](https://t.me/BotFather))
- ID группы/канала, куда будет добавлен бот

### Установка и настройка
1. **Клонируйте репозиторий** (или просто сохраните `main.py` и файлы промптов).
2. **Установите зависимости**:
   ```bash
   pip install python-telegram-bot ollama
   ```

# GreenTeaBot — Telegram AI with a local neural network
## English | Английский

A Telegram bot that replies to messages **not always**, but with a set probability. It uses a local model via [Ollama](https://ollama.com) and doesn't require an internet connection to generate responses. Ideal for cozy chats where you want to see witty comments from the AI.

---

### Features
- **Probabilistic responses** — you can configure the response probability (default is 30%).
- **Required reply when mentioned** — if the message contains `@TT_GrenTeaBot`, the bot will always reply.
- **Logging** — all dialogs and errors are saved in the `logs` folder (can be disabled).
- **Flexible model customization** — easily change the Ollama model by editing the `MODEL` variable.
- **Auto-generation of key and prompt** — if the files are missing, the bot will create them automatically.
- **Formatting error handling** — attempts to send a response in HTML, then in Markdown; otherwise, it wraps it in a monospace block.
- **Support for multiple prompts** — you can prepare multiple versions (for example, for small models) and switch between them.

### Requirements
- Python 3.7+
- Ollama installed and running (https://ollama.com)
- Telegram Bot Token (obtain from @BotFather)
- ID of the group/channel where the bot will be added

### Installation and Configuration
1. **Clone the repository** (or simply save `main.py` and the prompt files).
2. Install dependencies:
```bash
pip install python-telegram-bot ollama
```