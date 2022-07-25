from util.BotUtils import Utils
from util.BotUtils import DIR
import nextcord
from nextcord import Member
from nextcord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def help(self, ctx, cmd):
        desc = ""
        for c in self.client.walk_commands():

            if str(c) == cmd:
                if c.help is None:
                    desc += "Huh.\nNo help found for this command yet... Strange....."
                else:
                    desc += c.help

                await Utils.generic_embed(ctx, title=f"help - d!{cmd}", desc = desc)
                break

        else:
            await Utils.generic_error(ctx, f"No command found named {cmd}.")

def setup(client):
    client.add_cog(Help(client))