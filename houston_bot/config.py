import os


class BaseConfig:
    """Base configure Bot."""

    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.dialog_token = os.getenv('DIALOG_TOKEN')
        self.name = os.getenv('NAME', 'HoustonBot')
        self.lang = os.getenv('LANG', 'ru')
        self.welcome_text = os.getenv('WELCOME_TEXT', 'Привет, давай пообщаемся?')
        self.answer = os.getenv('ANSWER', 'Я Вас не совсем понял!')

    def switch_lang(self, lang):
        """Change language."""
        self.lang = lang

    def switch_welcome_text(self, text):
        """Change welcome text."""
        self.welcome_text = text
