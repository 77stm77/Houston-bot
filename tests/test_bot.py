from unittest import TestCase
from unittest.mock import patch

from houston_bot.bot import HoustonBot


class TestHoustonBot(TestCase):
    """Testing bot class. """

    def setUp(self) -> None:
        """Init dependency. """
        self.test_class = HoustonBot()
        self.test_class.TOKEN = 'jgjg123123'

    def tearDown(self) -> None:
        """Clean up. """
        del self.test_class

    @patch('houston_bot.bot.Filters')
    @patch('houston_bot.bot.MessageHandler')
    @patch('houston_bot.bot.CommandHandler')
    @patch('houston_bot.bot.Updater')
    def test_run(self, updater, command_handler, message_handler, filters):
        """Testing run method. """
        res = self.test_class.run()

        self.assertEqual(res, None)

        self.assertTrue(updater.called)
        updater.assert_called_with(token='jgjg123123')

        self.assertTrue(command_handler.called)
        command_handler.assert_called_with('start', self.test_class.start)

        self.assertTrue(message_handler.called)
        message_handler.assert_called_with(filters.text, self.test_class.message)

        self.assertTrue(updater.return_value.dispatcher.add_handler.called)
        self.assertEqual(updater.return_value.dispatcher.add_handler.call_count, 2)
        self.assertTrue(updater.return_value.start_polling.called)
        self.assertTrue(updater.return_value.idle.called)

