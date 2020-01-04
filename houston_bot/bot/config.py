import os


class Config:
    """Base configure Bot. """
    TOKEN = os.getenv('TOKEN')
    DIALOG_TOKEN = os.getenv('DIALOG_TOKEN')
    NAME = os.getenv('NAME', 'HoustonBot')
    LANG = os.getenv('LANG', 'ru')
