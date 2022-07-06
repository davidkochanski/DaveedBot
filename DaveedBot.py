# Created by davefoxxo ^w^

import nextcord
from nextcord.ext import commands
import os
from util.BotUtils import Utils, DIR
from util.ListUtils import DO_NOT_LOAD
from util.SuperSecretSettings import TOKEN, TOKEN2

def main():
    intents = nextcord.Intents.default()
    intents.message_content = True

    client = commands.Bot(command_prefix = "d!",
                          intents = intents, 
                          activity = nextcord.Activity(type=nextcord.ActivityType.playing, name="a game on my visor"), 
                          status = nextcord.Status.online)
    client.remove_command("help")

    print("DIR: " + DIR)

    @client.event
    async def on_ready():
        print("OwO!", end="\n\n")

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await Utils.generic_error(ctx, error)

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("**HEY!** Slow down a bit! >w>")

        if isinstance(error, commands.BadArgument):
            await Utils.generic_error(ctx, error)

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename not in DO_NOT_LOAD:
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cogs.{filename[:-3]}!")

    client.run(TOKEN)
    

if __name__ == "__main__":
    main()