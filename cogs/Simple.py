# -*- coding: utf-8 -*-

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
    async def quiz(self, ctx):
        '''
        Asks a totally normal quiz question.
        '''
        scenes = [
            ("What Pokemon is this?", "slugma", "SLUGMA NUTS"),
            ("What Pokemon is this?", "gulpin", "GULPIN DEEZ NUTS"),
            ("What Pokemon is this?", "rookidee", "ROOKIDEEZ NUTS"),
            ("What Pokemon is this?", "machoke", "MACHOKE ON MY COCK"),
            ("What Pokemon is this?", "rhydon", "RHYDON DEEZ NUTS"),
            ("What is this gym leader's name?", "candice", "CANDICE DICK FIT IN YO MOUTH"),
            ("What is the mythical creature on the Welsh flag?", "dragon", "DRAGON DEEZ NUTS ON YOUR FACE"),
            ("What is the name of this sweet desert?", "pudding", "PUDDING DEEZ NUTS ON YOUR FACE"),
            ("What country has this flag?", "kenya", "KENYA FIT DEEZ NUTS IN YOUR MOUTH"),
            ("What is the name of this famous Canadian meal?", "poutine", "POUTINE DEEZ NUTS IN YOUR MOUTH"),
            ("Who is this?", "putin", "PUTIN DEEZ NUTS IN YOUR MOUTH"),
            ("What is the brand name of this product?", "vaseline", "VASE*LEAN* IN AND KISS DEEZ NUTS"),
            ("What is the name of this video game character?", "king dedede", "YOU'RE KING OF DEDEDEEZ NUTS"),
            ("What is Bank of America's short form?", "bofa", "BOFA DEEZ NUTS"),
            ("What popular Pop Band made songs like 'Believer', 'Radioactive' and 'Demons?'", "imagine dragons", "IMAGINE DRAGON DEEZ NUTS ACROSS YOUR FACE")
        ]

        n = random.choice(scenes)

        fp = str(n[1]).replace(" ", "_")

        fl = nextcord.File(os.path.join(DIR, f"cogs\\Media\\Deez\\{fp}.jpg"), filename = f"{fp}.jpg")
        em = nextcord.Embed(title = n[0], color=0xff0000)

        em.set_image(f"attachment://{fp}.jpg")

        await ctx.send(embed = em, file = fl)

        def check(msg: nextcord.Message):
            return msg.channel.id == ctx.channel.id 

        for _ in range(64): # time out after 64 messages
            message = await self.client.wait_for("message", check = check)
            msg = message.content.lower()

            if msg == n[1]:
                await ctx.send(f"{message.author.mention} {n[2]}")
                break

            elif msg == "d!quiz":
                break


    @commands.command()
    async def furry(self, ctx):
        '''
        Sends a random furry emoticon.
        '''
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

        await ctx.send(random.choice(responses))

    @commands.command(aliases = ["source", "git", "repo", "star"])
    async def github(self, ctx):
        '''
        Shows a link to the source code of this very bot.\n
        You can look at my insides!
        '''
        await Utils.generic_embed(ctx, title = "Code Repository: https://github.com/davefoxxo/DaveedBot/",
                                  desc = "Please consider giving DaveedBot a :star: on GitHub!\nI'd really appreaciate it c:")



    @commands.command(hidden=True)
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def ban(self, ctx):
        await Utils.generic_embed(ctx, title = "Ok? Who asked? Care?", desc = "now ᴘʟᴀʏɪɴɢ: Who asked (Feat: Nobody)\n ───────────⚪────── \n◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊")

    
    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def flip(self, ctx):
        '''
        Flips a coin. What did you expect it to do?
        '''
        responses = ["You got heads."] * 4 + ["You got tails."] * 4 + ["Oh? The coin landed on it's side!"]
        await ctx.send("Wait for it!")
        time.sleep(random.uniform(1,3))
        await ctx.send(random.choice(responses))


    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def dave(self, ctx):
        '''
        #DAVEONTOP #FEARTHEDAVE", desc = "Ok? mad? sad? gonna cry? bad? ez? LLL LOOL #dave LLLLL #daveONTOP #daveSkyWars CRY? #daveBEDWARS #davePIT #daveSB #daveAIRLINES EASY #daveLEGITLUNAR #daveLLL #daveDOTGG #daveGG mad? :) LLLL CRY ABOUT IT? LOL?   #daveLEADERBOARDS #daveUNTOUCHABLE NO CONTEST LOL #daveCANNOTBESTOPPED #daveBEST #PAYFORTRUCE SO SAD LL?? DUELED ME LOL? #daveEZ #daveGG DOGWATER LOL GG HE PARTIED ME LMAOOOOOO SIT DOWN #daveONTOP LLLLLLLLLLLLLLLLLL MAD???? :) :) :) :) MAD? CRY L DANCE LLL #dave LLL #dave L BOXED L MAD????????? :) SOMEONE'S MAD :) :) :) L :) <3 HOW CAN YOU BE SO MAD :) lololol Accept that #dave is superior. :) L mad :) ? :) L
        '''
        await Utils.generic_embed(ctx, title = "#DAVEONTOP #FEARTHEDAVE", desc = "Ok? mad? sad? gonna cry? bad? ez? LLL LOOL #dave LLLLL #daveONTOP #daveSkyWars CRY? #daveBEDWARS #davePIT #daveSB #daveAIRLINES EASY #daveLEGITLUNAR #daveLLL #daveDOTGG #daveGG mad? :) LLLL CRY ABOUT IT? LOL?   #daveLEADERBOARDS #daveUNTOUCHABLE NO CONTEST LOL #daveCANNOTBESTOPPED #daveBEST #PAYFORTRUCE SO SAD LL?? DUELED ME LOL? #daveEZ #daveGG DOGWATER LOL GG HE PARTIED ME LMAOOOOOO SIT DOWN #daveONTOP LLLLLLLLLLLLLLLLLL MAD???? :) :) :) :) MAD? CRY L DANCE LLL #dave LLL #dave L BOXED L MAD????????? :) SOMEONE'S MAD :) :) :) L :) <3 HOW CAN YOU BE SO MAD :) lololol Accept that #dave is superior. :) L mad :) ? :) L")


    @commands.command(aliases = ["rocketleague", "rocket"])
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def rl(self, ctx):
        '''
        Sends a random Rocket League quick chat.
        '''
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

        await ctx.send(descrip)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ratio(self, ctx, target: Member = None):
        '''
        Optional argument: `target`

        Send a ratio message in chat. Optionally ratio someone
        '''
        if target != None:
            msg = await ctx.send(f"{target.mention} ratio")
        else:
            msg = await ctx.send("ratio")

        await msg.add_reaction("👍")

    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def areyouonline(self, ctx):
        '''
        :3
        '''
        await Utils.generic_embed(ctx, title = "Nope!", desc = "DaveedBot is currently offline and unable to respond to ANY commands. :3")

    
    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def cry(self, ctx):
        '''
        Sends a random 'Cry About It' gif.
        '''
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
        '''
        Sends a random Lisek Emoji (Limote:tm:) from my collection.
        '''
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
                    '<:yeahLi2:919701564858445935>','<:partyLi:975520974827048960>','<:layLi:981651009279500378>','<:glueLi:1000226176712847391>','<:derpLi:1000225942586802277>']

        await ctx.send(random.choice(responses))

    @commands.command(hidden=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def order(self, ctx, *, thing):
        '''
        Required argument: `thing`

        Order something off Google.
        '''

        EASTER_EGGS = ["john cena"]

        if thing.lower() in EASTER_EGGS:
            fl = nextcord.File(os.path.join(DIR, "cogs\\Media\\trans.jpg"), filename="trans.jpg")
            em = nextcord.Embed(title = f"Order up! {thing}", color = 0xff0000)
            em.set_image("attachment://trans.jpg")

            await ctx.send(embed = em, file = fl)
            return

        for string in thing.lower().split(" "):
            if string in BLACKLIST:
                await ctx.send("You horny bastard.")
                return
        
        if thing.lower().replace(" ", "") in BLACKLIST:
            await ctx.send("You horny bastard.")
            return
            
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
                    
                except Exception:
                    await Utils.generic_error(ctx, f"Could not find a(n) {thing}.")

                try:
                    os.remove(pathjpg)
                except: pass
                try:
                    os.remove(pathpng)
                except: pass

                self.is_searching = False
                return

        await ctx.send("**HEY!** Wait just a tick <w>")


    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def fox(self, ctx):
        '''
        Get a random picture of a fox.
        '''
        em = nextcord.Embed(title = f"Fox!", color = 0xff0000)
        em.set_image(url = f"https://randomfox.ca/images/{random.randint(1, 123)}.jpg")

        await ctx.send(embed = em)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def null(self, ctx):
        await ctx.send("⠀")
        

def setup(client):
    client.add_cog(Simple(client))