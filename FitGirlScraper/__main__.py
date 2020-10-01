from FitGirlScraper.bot.BotCommands import start,keyboard_markup,callback,inline_query
from FitGirlScraper.bot.Bot import Bot
import config


def main():
    bot = Bot(config.BOT_TOKEN)
    bot.add_command("start",start)
    bot.add_command("search",keyboard_markup)
    bot.add_callback(callback)
    bot.add_inline_query_handler(inline_query)
    bot.start()
    
if __name__ == "__main__":
    main()