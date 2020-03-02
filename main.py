from InstaLytics import InstaLytics
from sys import argv


try:
    bot = InstaLytics(argv[2])

    filename = argv[3]

    if bot.userExists():

        bot.getBrowser()

        bot.scrollToBottom()
        # links = bot.get_all_posts()

        # bot.getData(links)
        # bot.saveCsv(filename)

    else:
        print("User does not exist")
        bot.closeSession()


except IndexError:
    print("No user specified with -u option")