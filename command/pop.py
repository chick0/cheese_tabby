# -*- coding: utf-8 -*-
from os import path

from discord import File
from discord.abc import PrivateChannel
from discord.ext import commands


def is_public(ctx: commands.context):
    return not isinstance(
        ctx.message.channel,
        PrivateChannel
    )


class Command(commands.Cog, name="Pop Cat Commend"):
    @commands.command(help="pop pop pop......")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.check(is_public)
    async def pop(self, ctx: commands.context):
        await ctx.reply(
            file=File(fp=open(path.join("src", "pop.gif"), mode="rb"))
        )

    @commands.command(help="(pop...)")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.check(is_public)
    async def shutup(self, ctx: commands.context):
        await ctx.send(
            file=File(fp=open(path.join("src", "pop_close.png"), mode="rb"))
        )
