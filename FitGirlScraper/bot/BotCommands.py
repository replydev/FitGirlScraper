from FitGirlScraper.scraper.scraper import Scraper
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
import config


def get_string(args):
    output = ''
    for s in args:
        output += s + ' '
    return output


def start(update, context):
    update.message.reply_text("Type \"/search game name\" to find some games...")


def search(query):
    scraper = Scraper(query)
    elements = scraper.get_elements()
    if len(elements) == 0:
        return None
    return elements


def inline_query(update, context):
    query = update.inline_query.query
    elements = search(query)
    results = []
    if elements is None:
        results.append(InlineQueryResultArticle(
            id=uuid4(),
            title="No results..",
            input_message_content=InputTextMessageContent(
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ")))

        update.inline_query.answer(results)
        return
    count = 0
    for elements in elements:
        if count > config.KEYBOARD_RESULTS:
            break
        results.append(InlineQueryResultArticle(id=count, title=elements.get_title(),
                                                input_message_content=InputTextMessageContent(elements.get_magnet())))
        count += 1
    update.inline_query.answer(results)


def keyboard_markup(update, context):
    elements = search(get_string(context.args))
    if elements is None:
        update.message.reply_text("No results...")
        return
    keyboard = []
    count = 0
    for element in elements:
        if count > config.KEYBOARD_RESULTS:
            break
        keyboard.append([InlineKeyboardButton(element.get_title(), callback_data=element.get_magnet())])
        count += 1
    final_keyboard = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please choose some results", reply_markup=final_keyboard)


def callback(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=query.data)
