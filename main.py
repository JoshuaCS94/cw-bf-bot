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

    @bot.on(events.NewMessage(
        pattern='#everyone$'
    ))
    async def everyone(event):
        sender_id = event.from_id
        chat = await event.get_chat()
        all_members = await bot.get_participants(chat)

        users = filter(lambda p: p.id != sender_id and not p.bot, all_members)
        usernames = list(map(lambda u: f'@{u.username}', users))
        reply = "\n".join(usernames)

        await event.respond(reply)

    bot.run_until_disconnected()
