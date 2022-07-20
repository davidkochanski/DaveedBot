'''
Copyright (c) 2022 David Kochanski

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

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("**HEY!** Slow down a bit! >w>")

        elif isinstance(error, commands.BadArgument):
            await Utils.generic_error(ctx, error)

        print("{}: {}".format(error.__class__.__name__, error))
        

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename not in DO_NOT_LOAD:
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cogs.{filename[:-3]}!")

    client.run(TOKEN)
    

if __name__ == "__main__":
    main()
