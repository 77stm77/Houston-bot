from .bot import HoustonBot


def main():
    """The main function in the application is run bot. """
    bot = HoustonBot()
    bot.run()


if __name__ == '__main__':
    main()
