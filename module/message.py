# -*- coding: utf-8 -*-
from io import BytesIO
from os import path, listdir
from json import load
from random import randint
from logging import getLogger

from discord import errors
from discord import File
from discord.abc import PrivateChannel

from module.cache import set_cache, get_cache


logger = getLogger()


async def on_message(message):
    if not message.author.bot and not isinstance(message.channel, PrivateChannel):
        for word in load(fp=open(path.join("words", "words.json"))):
            if word in message.content.lower():
                s = listdir(path.join("img_storage"))
                image_id = s[randint(0, len(s) - 1)]

                image = get_cache(image_id)
                if image is None:
                    image = open(path.join("img_storage", image_id), mode="rb").read()
                    set_cache(image_id, image)

                try:
                    e = await message.channel.send(
                        file=File(fp=BytesIO(image), filename=f"{image_id}.png")
                    )
                except errors.Forbidden:
                    await message.channel.send("[Attach Files] is required for this bot!")
                    return

                try:
                    await e.add_reaction("❌")
                except errors.Forbidden:
                    await e.channel.send("[Add Reactions] and [Read Message History] is required for this bot!")
                return
