from aiohttp import web
from .route import routes
from asyncio import sleep 
from datetime import datetime
from database.users_chats_db import db
from info import LOG_CHANNEL, URL   # Removed PREMIUM_LOGS
import aiohttp
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


# ❌ Removed check_expired_premium() function  
# ❌ Removed premium expiration message  
# ❌ Removed premium logs  
# ❌ Removed premium database actions


async def keep_alive():
    """Keep bot alive by sending periodic pings."""
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.sleep(298)
            try:
                async with session.get(URL) as resp:
                    if resp.status != 200:
                        logging.warning(f"⚠️ Ping Error! Status: {resp.status}")
            except Exception as e:
                logging.error(f"❌ Ping Failed: {e}")
