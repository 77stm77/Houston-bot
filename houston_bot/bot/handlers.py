import json

import apiai

from houston_bot.bot.config import Config


class BotHandlers(Config):
    """Handler bot. """

    @classmethod
    def start(cls, bot, update):
        """Starting message. """
        bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')

    def message(self, bot, update):
        """Dialog message. """
        request = apiai.ApiAI(self.DIALOG_TOKEN).text_request()
        request.lang = self.LANG
        request.session_id = self.NAME
        request.query = update.message.text
        print(update.message.text)
        response_json = json.loads(request.getresponse().read().decode('utf-8'))
        response = response_json['result']['fulfillment']['speech']

        if response:
            print(response)
            bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
