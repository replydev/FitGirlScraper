from FitGirlScraper.scraper.scraper import Scraper
from telegram import InlineKeyboardButton,InlineKeyboardMarkup

def get_string(args):
    output = ''
    for s in args:
        output += s + ' '
    return output

def start(update,context):
    update.message.reply_text("Type \"/search game name\" to find some games...")


def search(update,context):
    scraper = Scraper(get_string(context.args))
    elements = scraper.get_elements()
    if len(elements) == 0:
        update.message.reply_text("No results...")
        return

    keyboard = []
    count = 0
    for element in elements:
        if count > 5:
            break
        keyboard.append([InlineKeyboardButton(element.get_title(),callback_data=element.get_magnet())])
        count += 1
    final_keyboard = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please choose some results",reply_markup=final_keyboard)

def callback(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=query.data)