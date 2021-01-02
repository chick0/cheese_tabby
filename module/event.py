# -*- coding: utf-8 -*-
from os import path, listdir
from json import load
from random import randint
from logging import getLogger

from discord import errors
from discord import File
from discord.abc import PrivateChannel
from discord import RawReactionActionEvent
from discord import Status, Activity, ActivityType

from config import config

logger = getLogger()


async def on_ready(bot):
    def get_status(option: str):
        if option == "idle":
            return Status.idle
        elif option == "dnd":
            return Status.dnd
        elif option == "offline":
            return Status.offline
        else:
            return Status.online

    def get_type(option: str):
        if option == "streaming":
            return ActivityType.streaming
        elif option == "listening":
            return ActivityType.listening
        elif option == "watching":
            return ActivityType.watching
        else:
            return ActivityType.playing

    logger.info("-" * 50)
    logger.info(f" - BOT Login : {bot.user}")
    logger.info(f" - Connected to ( {len(bot.guilds)} ) guilds!")
    logger.info("-" * 50)

    await bot.change_presence(
        status=get_status(config["status"]["status"]),
        activity=Activity(
            type=get_type(config["status"]["activity"]),
            name=config["status"]["name"]
        )
    )


async def on_command(ctx):
    logger.info(f"[{ctx.author.id}]{ctx.author} use [{ctx.message.content}]")


async def on_command_error(ctx, error):
    if error.__class__.__name__ in ["CommandOnCooldown", "NotOwner"]:
        await ctx.send(f"```\n"
                       f" - {error}\n"
                       f"```<@{ctx.author.id}>")
        return

    if error.__class__.__name__ in ["CommandNotFound", "CheckFailure"]:
        return

    logger.info(f"[{ctx.author.id}]{ctx.author} meet the error!")
    logger.error(f"{error.__class__.__name__}: {error}")


async def on_message(message):
    if not message.author.bot and not isinstance(message.channel, PrivateChannel):
        for word in load(fp=open(path.join("words", "words.json"))):
            if word in message.content.lower():
                logger.info(f"'{message.author}' Called the Cat! Used Word: {word} '{message.content}'")

                s = listdir(path.join("img_storage"))
                image_id = s[randint(0, len(s) - 1)]

                try:
                    e = await message.channel.send(
                        file=File(fp=open(path.join("img_storage", image_id), mode="rb"),
                                  filename=f"{image_id}.png")
                    )
                except errors.Forbidden:
                    await message.channel.send("[Attach Files] is required for this bot!")
                    return

                try:
                    await e.add_reaction("❌")
                except errors.Forbidden:
                    await e.channel.send("[Add Reactions] and [Read Message History] is required for this bot!")


async def on_raw_reaction_add(payload: RawReactionActionEvent, bot):
    channel = await bot.fetch_channel(
        channel_id=payload.channel_id
    )

    message = await channel.fetch_message(
        id=payload.message_id
    )

    if message.author.id == bot.user.id and payload.user_id != bot.user.id:
        if payload.emoji.name == "❌":
            try:
                await message.delete()
            except (errors.HTTPException, Exception):
                pass
