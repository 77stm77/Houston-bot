import json

import apiai

from config import BaseConfig


class BotHandlers(BaseConfig):
    """Handler bot. """

    def start(self, bot, update):
        """Starting message. """
        bot.send_message(chat_id=update.message.chat_id, text=self.welcome_text)

    def message(self, bot, update):
        """Dialog message. """
        request = apiai.ApiAI(self.dialog_token).text_request()
        request.lang = self.lang
        request.session_id = self.name
        request.query = update.message.text
        response_json = json.loads(request.getresponse().read().decode('utf-8'))
        response = response_json['result']['fulfillment']['speech']

        if response:
            bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=self.answer)
