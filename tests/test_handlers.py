from unittest import TestCase
from unittest.mock import MagicMock, patch

from houston_bot.handlers import BotHandlers


class TestBotHandlers(TestCase):
    """Testing handler bot. """

    def setUp(self) -> None:
        """Init dependency. """
        self.test_class = BotHandlers()
        self.bot = MagicMock()
        self.update = MagicMock()
        self.update.message.chat_id = 123
        self.test_class.WELCOME_TEXT = 'welcome'
        self.test_class.LANG = 'RU-ru'
        self.test_class.NAME = 'TestHoustonBot'
        self.test_class.DIALOG_TOKEN = '123ljlj234'
        self.test_class.ANSWER = 'not answer'
        self.update.message.text = 'message text'

    def tearDown(self) -> None:
        """Clean up. """
        del self.test_class
        del self.bot
        del self.update

    def test_start(self):
        """Testing start handler bot. """
        res = self.test_class.start(self.bot, self.update)
        self.assertEqual(res, None)
        self.assertTrue(self.bot.send_message.called)
        self.bot.send_message.assert_called_with(chat_id=123, text='welcome')

    @patch('houston_bot.handlers.json')
    @patch('houston_bot.handlers.apiai')
    def test_message_with_response(self, apiai, json):
        """Testing handler bot message response dialog. """
        json.loads.return_value = {
            'result': {
                'fulfillment': {
                    'speech': 'response_text_test'
                }
            }
        }

        res = self.test_class.message(self.bot, self.update)

        self.assertTrue(apiai.ApiAI.called)
        self.assertTrue(json.loads.called)

        apiai.ApiAI.assert_called_with('123ljlj234')

        self.assertTrue(self.bot.send_message.called)
        self.bot.send_message.assert_called_with(chat_id=123, text='response_text_test')

        self.assertEqual(res, None)

    @patch('houston_bot.handlers.json')
    @patch('houston_bot.handlers.apiai')
    def test_message_with_none_response(self, apiai, json):
        """Testing handler bot message none response. """
        json.loads.return_value = {
            'result': {
                'fulfillment': {
                    'speech': None
                }
            }
        }

        res = self.test_class.message(self.bot, self.update)

        self.assertTrue(apiai.ApiAI.called)
        self.assertTrue(json.loads.called)

        apiai.ApiAI.assert_called_with('123ljlj234')

        self.assertTrue(self.bot.send_message.called)
        self.bot.send_message.assert_called_with(chat_id=123, text='not answer')

        self.assertEqual(res, None)
