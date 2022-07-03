from util.BotUtils import Utils
from util.BotUtils import nextcord
import nextcord
from nextcord.ext import commands
from util.ListUtils import POKEMON, COUNTRIES
import random

class Guessing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mon(self, ctx):
        async with ctx.typing():
            mon = random.randint(1, 898)

            name = POKEMON[mon-1].lower()
            namesplit = name.split("-")[0]
            namespace = name.replace("-", " ")

            embed = nextcord.Embed(title = "Guess that Mon!", colour = 0xff0000)
            embed.set_image(url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png".format(mon))

            await ctx.send(embed = embed)

        await Utils.handle_guesses(ctx, self.client, "mon", (name, namesplit, namespace), ("tapu", "mr", "mime"))

    @commands.command()
    async def flag(self, ctx):
        async with ctx.typing():
            flag = random.choice(COUNTRIES).lower()
            namefirst = flag.split(" ")[0]
            namespace = flag.replace(" ", "")

            embed = nextcord.Embed(title = "Guess that flag!", colour = 0xff0000)
            embed.set_image(url = "https://countryflagsapi.com/png/{}".format(flag))

            await ctx.send(embed = embed)

        await Utils.handle_guesses(ctx, self.client, "flag", (flag, namefirst, namespace) , ("saint"))

def setup(client):
    client.add_cog(Guessing(client))