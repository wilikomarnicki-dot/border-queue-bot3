
import time
from telegram import Bot

# 🔴 ВСТАВ СЮДИ СВІЙ TOKEN
TOKEN = 8434689670:AAH0SL6xOqeNK-LbWguXpgyixRZnFSRuPYQ
CHAT_ID = None  # заповниться автоматично

bot = Bot(token=TOKEN)

LAST_QUEUE = None

def get_queue_length():
    """
    🔧 ТУТ ПОТІМ МОЖНА ПІДКЛЮЧИТИ РЕАЛЬНЕ API
    Поки що — приклад (рандом / заглушка)
    """
    import random
    return random.randint(0, 1200)

def main():
    global LAST_QUEUE, CHAT_ID

    updates = bot.get_updates()
    if updates:
        CHAT_ID = updates[-1].message.chat_id

    if CHAT_ID is None:
        print("❗ Напиши боту будь-яке повідомлення")
        return

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

        time.sleep(300)  # перевірка кожні 5 хв

if name == "__main__":
    
