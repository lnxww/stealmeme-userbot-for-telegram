
from telethon import TelegramClient
import asyncio
import random
from datetime import datetime

# ===== CONFIGURATION =====
api_id = 123456            # << Your API ID
api_hash = 'your_api_hash' # << Your API HASH

source_channels = [
    'memopolis',
    'rub_memes',
    'daily_kek',
    'cat_jokes'
]  # Channels to steal memes from

target_channel = 'my_meme_channel'  # Channel to post memes to

# ===== TELETHON CLIENT =====
client = TelegramClient('session_name', api_id, api_hash)

# ===== TIME-BASED RANDOM INTERVAL FUNCTION =====
def get_random_interval():
    hour = datetime.now().hour
    if 6 <= hour <= 11:
        return random.randint(600, 900)      # 10–15 minutes
    elif 12 <= hour <= 17:
        return random.randint(2100, 3300)    # 35–55 minutes
    elif 18 <= hour <= 22:
        return random.randint(2700, 3300)    # 45–55 minutes
    else:
        return random.randint(3300, 6000)    # 55–100 minutes

# ===== MAIN TASK LOOP =====
async def steal_random_meme():
    while True:
        print("\n===== NEW TASK =====")
        channel = random.choice(source_channels)
        print(f"[{datetime.now()}] Selected channel: @{channel}")

        try:
            messages = [msg async for msg in client.iter_messages(channel, limit=20)]
            image_messages = [
                msg for msg in messages
                if (
                    msg.photo
                    or (msg.file and msg.file.mime_type and msg.file.mime_type.startswith("image"))
                )
            ]

            if image_messages:
                msg = random.choice(image_messages)
                await client.send_file(target_channel, msg.media)  # ← Sends only image, no caption
                print(f"[{datetime.now()}] Meme sent to @{target_channel}")
            else:
                print(f"[{datetime.now()}] No image found in @{channel}")

        except Exception as e:
            print(f"[{datetime.now()}] Error with @{channel}: {e}")

        interval = get_random_interval()
        print(f"[{datetime.now()}] Sleeping for {interval // 60} minutes")
        print("===== WAITING... =====")
        await asyncio.sleep(interval)

# ===== STARTUP =====
async def main():
    await client.start()
    print("===== STARTUP =====")
    print("MemeGrabber is running...")
    await steal_random_meme()

client.loop.run_until_complete(main())
