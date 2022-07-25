# -*- coding: utf-8 -*-import

from util.BotUtils import Utils
from util.BotUtils import DIR
import nextcord
from nextcord import Member
from nextcord.ext import commands
import random
import time
import os
from icrawler.builtin import GoogleImageCrawler
from PIL import Image

from util.ListUtils import BLACKLIST

class Simple(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.is_searching = False

    @commands.command()
    async def furry(self, ctx):
        responses = ["OwO", "owo", "OWO", "**OwO**", "oWo",
                    "UwU", "uwu", "UWU", "**UwU**", "uWu",
                    "^w^", "^W^", ">w<", "~^w^~", ">W<",
                    "TwT", ">w>", "<w<", ".w.", "O//w//O",
                    ">//w//<", ";w;", "\*w\*", "ewe", "@w@",
                    ":3", ">:3", ":3c", ";3", ">:3", ">:3c",
                    "OvO", "UvU", "。O ω O 。", "◕w◕",
                    ":>", "c:", "X3", "x3", "X3c",
                    "!w!", "?w?", "0w0", "$w$", "XwX",
                    "\`w\`", "OmO", "VwV", "twt", "'w'",
                    "This is a SECRET MESSAGE! You got lucky!"]

        await Utils.generic_embed(ctx, title = f"{random.choice(responses)}", desc = "", colour = 0xff0000)

    @commands.command(aliases = ["source", "git", "github", "repo", "star"])
    async def git_hub(self, ctx):
        await Utils.generic_embed(ctx, title = "Code Repository: https://github.com/davefoxxo/DaveedBot/",
                                  desc = "Please consider giving DaveedBot a :star: on GitHub!\nI'd really appreaciate it c:")



    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def ban(self, ctx):
        await Utils.generic_embed(ctx, title = "Ok? Who asked? Care?", desc = "now ᴘʟᴀʏɪɴɢ: Who asked (Feat: Nobody)\n ───────────⚪────── \n◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊")

    
    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def flip(self, ctx):
        responses = ["You got heads."] * 4 + ["You got tails."] * 4 + ["Oh? The coin landed on it's side!"]
        await ctx.send("Wait for it!")
        time.sleep(random.uniform(1,3))
        await ctx.send(random.choice(responses))


    @commands.command(aliases = ["dave", "daveontop"])
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def dave_(self, ctx):
        await Utils.generic_embed(ctx, title = "#DAVEONTOP #FEARTHEDAVE", desc = "Ok? mad? sad? gonna cry? bad? ez? LLL LOOL #dave LLLLL #daveONTOP #daveSkyWars CRY? #daveBEDWARS #davePIT #daveSB #daveAIRLINES EASY #daveLEGITLUNAR #daveLLL #daveDOTGG #daveGG mad? :) LLLL CRY ABOUT IT? LOL?   #daveLEADERBOARDS #daveUNTOUCHABLE NO CONTEST LOL #daveCANNOTBESTOPPED #daveBEST #PAYFORTRUCE SO SAD LL?? DUELED ME LOL? #daveEZ #daveGG DOGWATER LOL GG HE PARTIED ME LMAOOOOOO SIT DOWN #daveONTOP LLLLLLLLLLLLLLLLLL MAD???? :) :) :) :) MAD? CRY L DANCE LLL #dave LLL #dave L BOXED L MAD????????? :) SOMEONE'S MAD :) :) :) L :) <3 HOW CAN YOU BE SO MAD :) lololol Accept that #dave is superior. :) L mad :) ? :) L")


    @commands.command(aliases = ["rl", "rocketleague", "rocket"])
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def rl_(self, ctx):
        scene = random.randint(1,8)

        responces = ["$#@%!", "All yours.", "Bumping!", "Calculated.", "Centering!", "Close one!", "Defending...", "Faking.", "Go for it!", "Great clear!",
                    "Great pass!", "Holy cow!", "I got it!", "In position.", "Incoming!", "My bad...", "My fault.", "Need boost!", "Nice block!", "Nice bump!",
                    "Nice demo!", "Nice one!", "Nice shot!", "No problem.", "No way!", "Noooo!", "OMG!", "Okay.", "On your left.", "On your right.", "Oops!",
                    "Passing!", "Savage!", "Siiiick!", "Sorry!", "Take the shot!", "Thanks!", "What a play!", "What a save!", "Whew.", "Whoops...", "Wow!",
                    "gg", "Well played.", "That was fun!", "Rematch!", "One. More. Game.", "What a game!", "Nice moves.", "Everybody dance!",
                    "Good luck!", "Have fun!", "Get ready.", "This is Rocket League!", "Let's do this!", "Here. We. Go.", "Nice cars!", "I'll do my best."]

        if scene == 7:
            descrip = f"**[TEAM]** {random.choice(responces)}"
        elif scene == 8:
            descrip = f"**[PARTY]** {random.choice(responces)}"
        else:
            descrip = f"{random.choice(responces)}"

        await Utils.generic_embed(ctx, title = descrip, desc = "", colour = 0xff0000)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ratio(self, ctx, target: Member = None):
        if target != None:
            msg = await ctx.send(f"{target.mention} ratio")
        else:
            msg = await ctx.send("ratio")

        await msg.add_reaction("👍")

    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def areyouonline(self, ctx):
        await Utils.generic_embed(ctx, title = "Nope!", desc = "DaveedBot is currently offline and unable to respond to ANY commands. :3")

    
    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def cry(self, ctx):
        scene = random.randint(1,24)

        crypath = os.path.join(DIR, "cogs\\Media\\Cry\\cryaboutit{}.gif".format(scene))
        cryfile = "cryaboutit{}.gif".format(scene)
        
        file = nextcord.File(crypath, filename = cryfile)
        embed = nextcord.Embed(title = "Cry about it", colour = 0xff0000)
        embed.set_image(url = "attachment://{}".format(cryfile))

        await ctx.send(file = file, embed = embed)


    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def limote(self, ctx):
        responses =['<:16bitsLi:919701730189541438>','<:64bitsLi:919701724581732383>','<:8bitsLi:919701736183185460>','<:blepLi:919701617530519562>',
                    '<:blushLi:928664465602400288>','<:boopLi:919701635582795836>','<:bruhLi:919701823504412692>','<:chadLi:919701594956771438>',
                    '<:chadLi2:919701603974512730>','<a:cubeLi:951279611050868786>','<:foxLi:939621573525143642>','<:highLi:949465143249600522>',
                    '<:joyLi:919701719280152576>','<:legLi:931575000991944775>','<:legLi2:931575020373827676>','<a:lookLi:919701917150613595>',
                    '<:loveLi:919701701244633089>','<a:loveShakeLi:951278953778257930>','<:mcLi:919701874431627264>','<:naeLi:919701677970427934>',
                    '<:naeLi2:919701686539419658>','<a:naenaeLi:919701800947449906>','<a:naenaeCubeLi:951279654168313877>','<:pawLi:919701642260131841>',
                    '<:pawLi2:930824596419141712>','<:pawLi3:940391903168462908>','<a:petLi:919701904655806535>','<:sarLi:963936139411095562>',
                    '<:sarLi2:963936532010520626>','<:scrunkLi:943706412930969630>','<:sitLi:919701712946745365>','<:sleepyPawsLi:931573923177459752>',
                    '<a:spinLi:919701933017665636>','<:unoLi:920051493653078066>','<:vrBlepLi:935341746093686844>','<:vrSadLi:935341730172133486>',
                    '<:vrSmugLi:959627074467942450>','<:wheezeLi:933887689172852758>','<:wheezeLi2:933887721137668167>','<:yeahLi:919701553978421278>',
                    '<:yeahLi2:919701564858445935>']

        await ctx.send(random.choice(responses))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def order(self, ctx, *, thing):
        if thing in BLACKLIST:
            await ctx.send("You horny bastard.")

        else:
            if not self.is_searching:
                self.is_searching = True
                async with ctx.typing():
                    path = os.path.join(DIR, "cogs\\Save\\order")
                    try:
                        google_crawler = GoogleImageCrawler(parser_threads=1, downloader_threads=1, storage = {'root_dir': path})
                        google_crawler.crawl(keyword=thing, max_num=1)

                        pathjpg = os.path.join(path, "000001.jpg")
                        pathpng = os.path.join(path, "000001.png")

                        try:
                            img = Image.open(pathjpg).convert("RGB")
                            img.save(pathpng)
                        except: pass

                        fl = nextcord.File(pathpng, filename="000001.png")
                        em = nextcord.Embed(title = f"Order up! {thing}", color = 0xff0000)

                        em.set_image("attachment://000001.png")

                        await ctx.send(embed = em, file = fl)
                        
                    except Exception as e:
                        await Utils.generic_error(ctx, f"Could not find a(n) {thing}.")

                    try:
                        os.remove(pathjpg)
                    except: pass
                    try:
                        os.remove(pathpng)
                    except: pass
                    self.is_searching = False
            else:
                await ctx.send("**HEY!** Wait just a tick <w>")


def setup(client):
    client.add_cog(Simple(client))