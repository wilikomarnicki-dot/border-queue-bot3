import os
import time
import random
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("BOT_TOKEN is missing")
    exit(1)

bot = Bot(token=TOKEN)

CHAT_ID = None
LAST_QUEUE = None


def get_queue_length():
    return random.randint(0, 1200)


def init_chat_id():
    global CHAT_ID
    updates = bot.get_updates()
    if not updates:
        print("No messages yet. Send 'hi' to the bot.")
        return False

    CHAT_ID = updates[-1].message.chat_id
    print(f"CHAT_ID = {CHAT_ID}")
    return True


def main():
    global LAST_QUEUE

    if not init_chat_id():
        return

    bot.send_message(
        chat_id=CHAT_ID,
        text="🤖 Бот запущено і він працює"
    )

    while True:
        queue = get_queue_length()

        if LAST_QUEUE is None:
            LAST_QUEUE = queue

        if queue > LAST_QUEUE + 50:
            bot.send_message(
                chat_id=CHAT_ID,
                text=f"🚛 Черга зростає!\nБуло: {LAST_QUEUE}\nСтало: {queue}"
            )
            LAST_QUEUE = queue

        time.sleep(300)


if name == "__main__":
    main()
