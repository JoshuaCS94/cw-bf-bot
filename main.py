import os

from telethon import TelegramClient, events

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

with TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) as bot:
    print('Connected')

    @bot.on(events.NewMessage(
        pattern='/hello$'
    ))
    async def start(event):
        await event.reply('Hello there, %s!' % event.sender.first_name)

    bot.run_until_disconnected()
