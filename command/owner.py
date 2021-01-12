# -*- coding: utf-8 -*-

from discord.ext import commands


class Command(commands.Cog, name="for bot owner"):
    @commands.command(help="Shutdown the bot", hidden=True)
    @commands.is_owner()
    async def close(self, ctx: commands.context):
        await ctx.reply(":wave:")
        await ctx.bot.close()
