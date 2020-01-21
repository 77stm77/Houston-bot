# Houston-bot

**Это своего рода ИИ которая может вести разговор на основе сообщений в телеграмм-чате https://t.me/true_pitonist_chat. Бот создан на языке программирования Python, используя библиотеку telebot.
 Само ИИ создана тоже на Python, используя библиотеку TensorFlow.**
  
**Бот использует алгоритм машинного обучения LSTM.** 

**Создано группой https://t.me/true_pitonist_chat. Владелец является https://t.me/Inojelis.**

### Для нормальной работы бота нужно задать глобавльные переменные
```
    TOKEN = os.getenv('TOKEN')
    DIALOG_TOKEN = os.getenv('DIALOG_TOKEN')
    NAME = os.getenv('NAME', 'HoustonBot')
    LANG = os.getenv('LANG', 'ru')
    WELCOME_TEXT = os.getenv('WELCOME_TEXT', 'Привет, давай пообщаемся?')
    ANSWER = os.getenv('ANSWER', 'Я Вас не совсем понял!')
```
**TOKEN** - телеграмм токен
**DIALOG_TOKEN** - сервис https://dialogflow.com



