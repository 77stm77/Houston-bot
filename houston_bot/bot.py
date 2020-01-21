from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import BotHandlers


class HoustonBot(BotHandlers):
    """Bot AI Houston. """

    def run(self):
        """Run Bot Dialog."""
        updater = Updater(token=self.token)
        start_command_handler = CommandHandler('start', self.start)
        text_message_handler = MessageHandler(Filters.text, self.message)
        updater.dispatcher.add_handler(start_command_handler)
        updater.dispatcher.add_handler(text_message_handler)
        updater.start_polling(clean=True)
        updater.idle()
