# -*- coding: utf-8 -*-
from os import path, listdir
from random import randint

from discord import File
from discord import errors
from discord.ext import commands


class Command(commands.Cog, name="Command for @everyone"):
    @commands.command(help="Check connected guilds")
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def guilds(self, ctx: commands.context):
        await ctx.send(
            "```\n"
            f" - Connected to ( {len(ctx.bot.guilds)} ) guilds!\n"
            "```"
        )

    @commands.command(help="Send Cat image! (random or custom)")
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def send(self, ctx: commands.context, image_id: str = None):
        if image_id is None:
            s = listdir(path.join("img_storage"))
            image_id = s[randint(0, len(s) - 1)]

        if path.exists(path.join("img_storage", image_id)):
            try:
                await ctx.send(
                    file=File(fp=open(path.join("img_storage", image_id), mode="rb"),
                              filename=f"{image_id}.png")
                )
            except errors.Forbidden:
                await ctx.send("[Attach Files] is required for this bot!")

        else:
            await ctx.send(
                "```\n"
                " 404\n"
                " - Image not found!!!\n"
                "```"
            )
