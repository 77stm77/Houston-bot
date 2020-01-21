from unittest import TestCase
from unittest.mock import patch

from houston_bot.main import main


class TestMain(TestCase):
    """Testing main func in app."""

    def setUp(self) -> None:
        """Init dependency."""
        self.test_main = main

    def tearDown(self) -> None:
        """Clean up."""
        del self.test_main

    @patch('houston_bot.main.HoustonBot.run')
    def test_main_bot_run(self, bot):
        """Testing instance bot."""
        res = self.test_main()

        self.assertTrue(bot.called)
        self.assertEqual(res, None)
