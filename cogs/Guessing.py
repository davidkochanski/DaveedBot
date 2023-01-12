from io import BytesIO
from util.BotUtils import DIR, handle_guesses, display_leaderboard, generic_embed, generic_error, printl
import discord
from discord import app_commands
from discord import Interaction as Intr
from discord.ext import commands
from util.ListUtils import POKEMON, COUNTRIES
import random
import requests
from PIL import Image
import os

class Guessing(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.boards = ["mon", "flag", "fur"]
    
    @app_commands.command(name="leaderboard", description="lb")
    @app_commands.choices(leaderboard=[app_commands.Choice(name="mon", value="mon"),
                                    app_commands.Choice(name="flag", value="flag"),
                                    app_commands.Choice(name="fur", value="fur")])
    async def leaderboard(self, intr: Intr, leaderboard: app_commands.Choice[str]):
        '''
        Required argument: `leaderboard`

        Displays the leaderboard for a specific guessing game on DaveedBot.
        Your name and score will be highlighted!
        
        '''
        lb = leaderboard.value
        await display_leaderboard(await self.client.get_context(intr), lb)

    

    @app_commands.command(name="mon", description="Guess a random Pokemon! (/hint /len for hints; /idk to give up)")
    async def mon(self, intr: Intr):
        '''
        Sends a random Pokemon. Try to guess it!
        Access the leaderboards using `d!lb mon`

        While guessing:
        Use `d!hint` to get a hint about the current Pokemon.
        Use `d!len` to get how many letters long the Pokemon's name is.
        Use `d!idk` to reveal the mon.
        '''
        ctx = await self.client.get_context(intr)
        mon = random.randint(1, 898)

        name = POKEMON[mon-1].lower()
        namesplit = name.split("-")[0]
        namespace = name.replace("-", " ")

        url = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png".format(mon))
        img = Image.open(BytesIO(url.content))
        img.save(os.path.join(DIR, "cogs/save/mon.png"))
        printl(name)

        file = discord.File(os.path.join(DIR, "cogs/save/mon.png"))
        embed = discord.Embed(title = "Guess that Mon!", colour = 0xff0000)
        embed.set_image(url = f"attachment://mon.png")

        await ctx.send(embed = embed, file = file)

        await handle_guesses(ctx, self.client, "mon", [name, namesplit, namespace], excluded_guesses = ["tapu", "mr", "mime"])

    @app_commands.command(name="flag", description="Guess a random country's flag! (/hint /len for hints; /idk to give up)")
    async def flag(self, intr: Intr):
        '''
        Sends a random country flag. Try to guess it!
        Access the leaderboards using `d!lb flag`

        While guessing:
        Use `d!hint` to get a hint about the current flag.
        Use `d!len` to get how many letters long the country's name is.
        Use `d!idk` to reveal the country.
        '''
        ctx = await self.client.get_context(intr)
        flag = random.choice(COUNTRIES).lower()
        namefirst = flag.split(" ")[0]
        namespace = flag.replace(" ", "")
        print(flag)

        url = requests.get("https://countryflagsapi.com/png/{}".format(flag.replace(" ", "%20")))
        img = Image.open(BytesIO(url.content))
        img.save(os.path.join(DIR, "cogs/save/NICE_TRY_LUCA.png"))

        file = discord.File(os.path.join(DIR, "cogs/save/NICE_TRY_LUCA.png"))
        embed = discord.Embed(title = "Guess that flag!", colour = 0xff0000)
        embed.set_image(url = "attachment://NICE_TRY_LUCA.png")

        await ctx.send(embed = embed, file = file)

        await handle_guesses(ctx, self.client, "flag", [flag, namefirst, namespace], excluded_guesses=["saint", "united", "the"])

    @app_commands.command(name="fur", description="Guess a random furry! (/hint /len for hints; /idk to give up)")
    async def fur(self, intr: Intr):
        furs = [
            ["beta eta delota", "beta", "betaetadelota"],
            ["majira strawberry", "majira", "majirastrawberry"],
            ["pocari roo", "pocari"],
            ["chipflake", "chip"],
            ["foofi", "furryfoofi"],
            ["nos hyena", "nos"],
            ["odin wolf", "odin"],
            ["ash coyote", "ash"],
            ["stormi folf", "stormi"],
            ["adler the eagle", "adler", "adler eagle"],
            ["yonkagor", "yon"],
            ["davefoxxo", "dave"],
            ["wicc"],
            ["fluke husky", "fluke", "flukehusky"],
            ["neon woof", "neon", "neonwoof"],
            ["jt wusky", "jt"],
            ["blue folf", "blue", "bluefolf"],
            
        ] 
        # TODO fleurfurr
        # oddonesout
        # odin wolf
        ctx = await self.client.get_context(intr)
        idx = random.randint(0, len(furs) - 1)
        print(furs[idx][0])

        fl = discord.File(os.path.join(DIR, f"cogs/Media/Furs/{idx}.jpg"), filename = f"{idx}.jpg")
        em = discord.Embed(title = "Guess that Popufur!", color = 0xff0000)
        em.set_image(url = f"attachment://{idx}.jpg")

        await ctx.send(embed = em, file = fl)

        await handle_guesses(ctx, self.client, name="fur", correct_guesses=furs[idx])



    # Dummy commands
    @commands.command(hidden=True)
    async def idk(self, ctx): pass

    @commands.command(hidden=True)
    async def hint(self, ctx): pass

    @commands.command(hidden=True)
    async def len(self, ctx): pass

async def setup(client):
    await client.add_cog(Guessing(client))