from telethon import TelegramClient, events
import asyncio
import datetime
import pytz
from data.config import *

# Telegram Client'ni yaratish
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


# Rejalashtirilgan xabar yuborish
async def send_daily_message():
    while True:
        # Bugungi vaqtni olish
        now = datetime.datetime.now(pytz.timezone('Asia/Tashkent'))

        # Xabar yuborish vaqti
        if now.hour == 7 and now.minute == 0 and now.second == 0:
            # Xabar MATNI
            message = f"Bugungi kun: {now.strftime('%d.%m.%Y')}\nHayrli kun!"

            # Xabar yuborish
            await client.send_message(GROUP_ID, message)

            # Vaqt tugaganidan so'ng xabar yuborish
            await asyncio.sleep(24 * 60 * 60)  # 1 kun hisobi olingan


# !help komandasini orqali yuborilgan xabarni olish
@client.on(events.NewMessage(chats=GROUP_ID, pattern=r"^!help(.+)?"))
async def send_to_channel_handler(event):
    # Xabar matnini olish
    message_text = event.text

    # Yangi xabar yuborish
    full_message = f"📢 Yangi xabar:\n\n{message_text}"

    # Kanalga xabar yuborish
    try:
        await client.send_message(CHANNEL_ID, full_message)
        await event.reply("✅ Tez orada javob beriladi.")
    except Exception as e:
        await event.reply(f"❌ Xabar yuborishda xatolik yuz berdi: {str(e)}")


# Botni ishga tushiruvchi funksiya
async def main():
    await client.start()
    # Event handler'ni qo'shamiz
    client.add_event_handler(send_to_channel_handler)

    # Rejalashtirilgan xabar yuborishni qo'shish
    asyncio.create_task(send_daily_message())

    # Botni ishga tushurish
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
