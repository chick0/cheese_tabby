# -*- coding: utf-8 -*-
from time import sleep
from logging import getLogger

import aiohttp
from discord.ext import commands, tasks

from config import config

logger = getLogger()


class Task(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.endpoint = "https://top.gg/api/bots/stats"
        self.headers = {
            'User-Agent': f"PythonBot aiohttp/{aiohttp.__version__}",
            'Content-Type': 'application/json',
            'Authorization': config["token"]["top.gg"]
        }

        self.post_count.start()

    @tasks.loop(minutes=30)
    async def post_count(self):
        await self.bot.wait_until_ready()
        payload = {
            'server_count': len(self.bot.guilds)
        }
        if self.bot.shard_count is not None:
            payload['shard_count'] = self.bot.shard_count

        logger.info("Send 'Server Count' data to 'top.gg'")
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url=self.endpoint, json=payload) as response:
                logger.info(f"'Top.gg' response: [{response.status}] {await response.text()}")
