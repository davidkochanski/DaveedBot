'''
Copyright (c) 2023 David Kochanski

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, goitcopy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

# Created by davefoxxo ^w^
import asyncio
import discord
from datetime import datetime
from discord import Interaction as Intr
from discord.ext import commands
from discord import app_commands, ui
import os
from util.BotUtils import DIR, printl, generic_embed, generic_error
from util.ListUtils import DO_NOT_LOAD, POKEMON
from util.SuperSecretSettings import TOKEN
from typing import List
import colorama
from colorama import Fore

async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = commands.Bot(command_prefix = "/",
                          intents = intents, 
                          activity = discord.Activity(type=discord.ActivityType.playing, name="a game on my visor"), 
                          status = discord.Status.online)
    client.remove_command("help")
    

    printl("DIR: " + DIR)

    @client.event
    async def on_ready():
        printl(f"Syncing slash commands...")

        try:
            synced = await client.tree.sync()
            printl(f"Successfully synced {len(synced)} slash commands.\n")

        except Exception as e:
            printl("Something went wrong.")
            printl(e)


        printl("OwO LOADED OK \n===================================")

    @client.event
    async def on_error(ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await generic_error(ctx, error)

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("**HEY!** Slow down a bit! >w>")

        elif isinstance(error, commands.BadArgument):
            await generic_error(ctx, error)

        elif isinstance(error, commands.CommandNotFound):
            await generic_error(ctx, f"{str(error)}, did you make a typo?")

        printl(error)


    @client.event
    async def on_interaction(intr: Intr):
        colorama.init()
        now = datetime.now().strftime("%b %d %Y %H:%M:%S")

        print(f"{Fore.GREEN}[{now}]{Fore.WHITE} {intr.user.name} ({intr.user.id}) used /{intr.command.name} in: {intr.channel.guild} -> #{intr.channel.name}.", end="\n")



    @client.tree.command(name="test", description="This is a slash command")
    async def test(intr: Intr, *, message: str = ""):
        await intr.response.send_message(f"OwO {message}!~", ephemeral = True)



    class TheMenu(ui.View):
        def __init__(self):
            super().__init__()
            self.value = None


        @discord.ui.button(label="one", style=discord.ButtonStyle.blurple)
        async def one(self, intr: Intr, button: ui.Button):
            await intr.response.send_message("OwO")


            


    @client.tree.command(name="testing", description="IHUFAWIUFIHUJAWF")
    async def testing(intr: Intr):
        view = TheMenu()

        await intr.response.send_message("Hey!", view=view)
    



    class TheModal(ui.Modal, title='Modal'):
        name = ui.TextInput(label='Name')
        answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

        async def on_submit(self, interaction: discord.Interaction):
            await interaction.response.send_message(f'Thanks for your response, {self.name}!\n`{self.answer}`')


    @client.tree.command(name="name", description="Fancy new modal feature test")
    async def name(intr: Intr):
        await intr.response.send_modal(TheModal())




    async with client:
        printl("Loading cogs...")
        try:
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py") and filename not in DO_NOT_LOAD:
                    await client.load_extension(f"cogs.{filename[:-3]}")
                    printl(f"Loaded cogs.{filename[:-3]}!")

            printl(f"Successfully loaded {len(set(client.walk_commands()))} legacy commands.\n")

            printl("Starting client...")
            await client.start(TOKEN)

            
        except Exception as e:
            printl("Something went wrong.")
            printl(e)

    

if __name__ == "__main__":
    asyncio.run(main())
