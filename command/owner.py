# -*- coding: utf-8 -*-

from discord.ext import commands


class Command(commands.Cog, name="for Bot OWNER"):
    @commands.command(help="Shutdown the bot")
    @commands.is_owner()
    async def close(self, ctx: commands.context):
        await ctx.send(":wave:")
        await ctx.bot.close()
