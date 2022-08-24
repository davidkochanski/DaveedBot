from io import BytesIO
from util.BotUtils import Utils, DIR
import nextcord
from nextcord.ext import commands
from util.ListUtils import POKEMON, COUNTRIES
import random
import requests
from PIL import Image
import os

class Guessing(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.boards = ["mon", "flag", "fur"]
    
    @commands.command(aliases = ["leaderboard", "leaderboards"])
    async def lb(self, ctx, leaderboard):
        '''
        Required argument: `leaderboard`

        Displays the leaderboard for a specific guessing game on DaveedBot.
        Your name and score will be highlighted!
        
        '''
        if leaderboard in self.boards:
            await Utils.display_leaderboard(ctx, leaderboard)

        else:
            await Utils.generic_error(ctx, f"'{leaderboard}' is not a valid leaderboard.")

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def mon(self, ctx):
        '''
        Sends a random Pokemon. Try to guess it!
        Access the leaderboards using `d!lb mon`

        While guessing:
        Use `d!hint` to get a hint about the current Pokemon.
        Use `d!len` to get how many letters long the Pokemon's name is.
        Use `d!idk` to reveal the mon.
        '''

        mon = random.randint(1, 898)

        name = POKEMON[mon-1].lower()
        namesplit = name.split("-")[0]
        namespace = name.replace("-", " ")

        url = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png".format(mon))
        img = Image.open(BytesIO(url.content))
        img.save(os.path.join(DIR, "cogs/save/mon.png"))
        print(name)

        file = nextcord.File(os.path.join(DIR, "cogs/save/mon.png"))
        embed = nextcord.Embed(title = "Guess that Mon!", colour = 0xff0000)
        embed.set_image(url = f"attachment://mon.png")

        await ctx.send(embed = embed, file = file)

        await Utils.handle_guesses(ctx, self.client, "mon", [name, namesplit, namespace], excluded_guesses = ["tapu", "mr", "mime"])

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def flag(self, ctx):
        '''
        Sends a random country flag. Try to guess it!
        Access the leaderboards using `d!lb flag`

        While guessing:
        Use `d!hint` to get a hint about the current flag.
        Use `d!len` to get how many letters long the country's name is.
        Use `d!idk` to reveal the country.
        '''
        flag = random.choice(COUNTRIES).lower()
        namefirst = flag.split(" ")[0]
        namespace = flag.replace(" ", "")
        print(flag)

        url = requests.get("https://countryflagsapi.com/png/{}".format(flag.replace(" ", "%20")))
        img = Image.open(BytesIO(url.content))
        img.save(os.path.join(DIR, "cogs/save/NICE_TRY_LUCA.png"))

        file = nextcord.File(os.path.join(DIR, "cogs/save/NICE_TRY_LUCA.png"))
        embed = nextcord.Embed(title = "Guess that flag!", colour = 0xff0000)
        embed.set_image(url = "attachment://NICE_TRY_LUCA.png")

        await ctx.send(embed = embed, file = file)

        await Utils.handle_guesses(ctx, self.client, "flag", [flag, namefirst, namespace], excluded_guesses=["saint", "united", "the"])

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def fur(self, ctx):
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
            ["neon woof", "neon"],
            ["jt wusky", "jt"],
            ["blue folf", "blue", "bluefolf"],
            
        ]

        idx = random.randint(0, len(furs) - 1)
        print(furs[idx][0])

        fl = nextcord.File(os.path.join(DIR, f"cogs/Media/Furs/{idx}.jpg"), filename = f"{idx}.jpg")
        em = nextcord.Embed(title = "Guess that Popufur!", color = 0xff0000)
        em.set_image(url = f"attachment://{idx}.jpg")

        await ctx.send(embed = em, file = fl)

        await Utils.handle_guesses(ctx, self.client, "fur", furs[idx])



    # Dummy commands
    @commands.command(hidden=True)
    async def idk(self, ctx): pass

    @commands.command(hidden=True)
    async def hint(self, ctx): pass

    @commands.command(hidden=True)
    async def len(self, ctx): pass

def setup(client):
    client.add_cog(Guessing(client))