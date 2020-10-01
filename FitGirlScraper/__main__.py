from FitGirlScraper.bot.BotCommands import start,search,callback
from FitGirlScraper.bot.Bot import Bot
import config


def main():
    bot = Bot(config.BOT_TOKEN)

    bot.add_command("start",start)
    bot.add_command("search",search)
    bot.add_callback(callback)

    bot.start()
    

if __name__ == "__main__":
    main()