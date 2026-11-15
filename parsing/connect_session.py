import os
from pathlib import Path
from dotenv import load_dotenv
from telethon import TelegramClient

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / '.env')

api_id = int(os.getenv('TG_API_ID'))
api_hash = os.getenv('TG_API_HASH')
chat_id = int(os.getenv('TG_CHAT_ID', '0'))

session = str(ROOT / 'data' / os.getenv('TG_SESSION', 'tg_pars'))


async def return_connect_telethon():
    client = TelegramClient(session, api_id, api_hash, system_version="4.16.30-vxCUSTOM")
    await client.start()

    return client


async def return_disconnect_telethon(client):
    try:
        await client.disconnect()
    except Exception as ex:
        print(f"Failed\n{ex}")
