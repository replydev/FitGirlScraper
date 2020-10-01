from telegram.ext import CommandHandler,Updater,CallbackQueryHandler

class Bot:
    def __init__(self,botToken):
        self.updater = Updater(token=botToken,use_context=True)

    def add_command(self,command_text,method):
        self.updater.dispatcher.add_handler(CommandHandler(command_text,method))

    def add_callback(self,method):
        self.updater.dispatcher.add_handler(CallbackQueryHandler(method))


    def start(self):
        self.updater.start_polling()