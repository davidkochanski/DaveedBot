from util.BotUtils import DIR, generic_embed, generic_error
import discord
from discord import Member
from discord.ext import commands
import numpy as np
import os


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def help(self, ctx, cmd = None):
        '''
        Why would you need help using the help command?
        '''
        if cmd == None:
            comms = []
            for c in self.client.walk_commands():
                if not c.hidden:
                    comms.append("\n" + str(c).replace("_", ""))

            three_coms = np.array_split(comms, 3)
            em = discord.Embed(title = "Welcome to DaveedBot:tm:!", description = "The command prefix is `d!`. Use `d!help [cmd]` to get more info on any other command! \n List of all commands:\n", color = 0xff0000)
            em.add_field(name = ":fox:", value = "".join(three_coms[0]))
            em.add_field(name = ":fox:", value = "".join(three_coms[1]))
            em.add_field(name = ":fox:", value = "".join(three_coms[2]))

            filepath = os.path.join(DIR,"cogs/Media/proto.png")
            fl = discord.File(filepath, filename = "proto.png")

            em.set_thumbnail(url = "attachment://{}".format("proto.png"))
            em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))

            await ctx.send(embed = em, file = fl)
            return

        desc = ""
        for c in self.client.walk_commands():

            if str(c) == cmd:
                if c.help is None:
                    desc += "Huh.\nNo help found for this command yet... Strange....."
                else:
                    desc += c.help

                await generic_embed(ctx, title=f"help - d!{cmd}", desc = desc)
                break

        else:
            await generic_error(ctx, f"No command found named {cmd}.")

async def setup(client):
    await client.add_cog(Help(client))