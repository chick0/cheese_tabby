# -*- coding: utf-8 -*-
from os import path, listdir
from random import randint

from discord import File
from discord.errors import Forbidden
from discord.ext import commands

from module.url import get_link


class Command(commands.Cog, name="Command for @everyone"):
    @commands.command(help="Check connected guilds")
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def guilds(self, ctx: commands.context):
        await ctx.reply(
            "```\n"
            f" - Connected to ( {len(ctx.bot.guilds)} ) guilds,\n"
            f"   with using ( {ctx.bot.shard_count} ) shards!"
            "```"
        )

    @commands.command(help="Send invite link to you")
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def invite(self, ctx: commands.context):
        try:
            await ctx.author.send(
                "> Link is here\n"
                f"{get_link(bot=ctx.bot)}"
            )
        except Forbidden:
            await ctx.reply(f"`{get_link(bot=ctx.bot)}`")

    @commands.command(help="Send Cat image! (random or custom)")
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def send(self, ctx: commands.context, image_id: str = None):
        if image_id is None:
            s = listdir(path.join("img_storage"))
            image_id = s[randint(0, len(s) - 1)]

        if path.exists(path.join("img_storage", image_id)):
            try:
                await ctx.reply(
                    file=File(fp=open(path.join("img_storage", image_id), mode="rb"),
                              filename=f"{image_id}.png")
                )
            except Forbidden:
                await ctx.reply("[Attach Files] is required for this bot!")

        else:
            await ctx.reply(
                "```\n"
                " 404\n"
                " - Image not found!!!\n"
                "```"
            )
