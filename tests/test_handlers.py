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
        self.test_class.welcome_text = 'welcome'
        self.test_class.lang = 'RU-ru'
        self.test_class.name = 'TestHoustonBot'
        self.test_class.dialog_token = '123ljlj234'
        self.test_class.answer = 'not answer'
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
        self.assertEqual(apiai.ApiAI.return_value.text_request.call_count, 1)
        self.assertEqual(apiai.ApiAI.return_value.text_request.return_value.query, self.update.message.text)

        self.assertEqual(apiai.ApiAI.return_value.text_request.return_value.session_id, self.test_class.name)
        self.assertEqual(apiai.ApiAI.return_value.text_request.return_value.lang, self.test_class.lang)

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
