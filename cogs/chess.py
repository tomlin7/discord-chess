from discord.ext import commands

from cogs.libs.board import init_board


class Chess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def board(self, ctx):
        await ctx.send(init_board())


def setup(bot):
    bot.add_cog(Chess(bot))
