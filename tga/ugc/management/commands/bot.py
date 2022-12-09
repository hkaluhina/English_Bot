from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from tga.ugc.models import Message
from tga.ugc.models import Profile


def log_errors(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:

            error_message = f' Произошла онибка: {e}'
            print(error_message)
            raise e

        return inner


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        #1 -- Правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )
        print(bot.get_me())

        #2 -- Обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        message.handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()