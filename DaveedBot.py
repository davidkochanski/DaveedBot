# -*- coding: utf-8 -*-
# Created by davefoxxo ^w^

import nextcord
from nextcord.ext import commands
import os
from util.BotComs import Coms
from util.BotComs import DIR
from util.SuperSecretSettings import TOKEN



def main():
    client = commands.Bot(command_prefix = "d!", activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="d!help :3"), status = nextcord.Status.online)
    client.remove_command("help")

    print("DIR: " + DIR)

    @client.event
    async def on_ready():
        print("OwO!", end="\n\n")

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await Coms.generic_embed(ctx, title = "Oh no...", desc = "Missing or Inappropriate arguments!\n\nMaybe try again? TwT", colour = 0xffff00)

    DO_NOT_LOAD = []

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename not in DO_NOT_LOAD:
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cogs.{filename[:-3]}!")

    client.run(TOKEN) #!! EXCLUSIVE
    

if __name__ == "__main__":
    main()