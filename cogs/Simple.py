# -*- coding: utf-8 -*-

from util.BotUtils import generic_embed, generic_error, printl, create_embed
from util.BotUtils import DIR
import discord
from discord import app_commands
from discord import Interaction as Intr
from discord import Member
from discord.ext import commands
import random
import time
import os
from icrawler.builtin import GoogleImageCrawler
from PIL import Image
import pyqrcode
import png

class Simple(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.is_searching = False

    @app_commands.command(name="qr", description="Make a qr code")
    async def qr(self, intr: Intr, link: str = None):

        url = pyqrcode.create(link)

        url.png(os.path.join(DIR, "cogs/Save/qr.png"), scale = 4)

        img = discord.File(os.path.join(DIR, "cogs/Save/qr.png"))

        await intr.response.send_message("Here is your qr code.", file=img)


    

    @app_commands.command(name="quiz", description="Asks a totally normal quiz question.")
    async def quiz(self, intr: Intr):
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
        ctx = await self.client.get_context(intr)

        n = random.choice(scenes)
        fp = str(n[1]).replace(" ", "_")

        fl = discord.File(os.path.join(DIR, f"cogs/Media/Deez/{fp}.jpg"), filename = f"{fp}.jpg")
        em = discord.Embed(title = n[0], color=0xff0000)

        em.set_image(url = f"attachment://{fp}.jpg")

        await intr.response.send_message(embed = em, file = fl)

        def check(msg: discord.Message):
            return msg.channel.id == ctx.channel.id 

        for _ in range(64): # time out after 64 messages
            message: discord.Message = await self.client.wait_for("message", check = check)
            msg = message.content.lower()

            if msg == n[1]:
                await intr.followup.send(f"{message.author.mention} {n[2]}")
                break

            elif msg == "d!quiz":
                break


    @app_commands.command(name="furry", description="Sends a random furry emoticon.")
    async def furry(self, intr: Intr):
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

        await intr.response.send_message(random.choice(responses))

    @app_commands.command(name="github", description="Shows a link to the source code of this very bot. You can look at my insides!")
    async def github(self, intr: Intr):
        '''
        Shows a link to the source code of this very bot.\n
        You can look at my insides!
        '''
        em = await create_embed(await self.client.get_context(intr), title = "Code Repository: https://github.com/davefoxxo/DaveedBot/",
                                  desc = "Please consider giving DaveedBot a :star: on GitHub!\nI'd really appreaciate it c:")

        await intr.response.send_message(embed=em)



    @app_commands.command(name="ban", description="Ban someone from a guild. Works for everyone regardless of server permission! Have fun!!!")
    async def ban(self, intr: Intr):
        em = await create_embed(await self.client.get_context(intr), title = "Ok? Who asked? Care?", desc = "now ᴘʟᴀʏɪɴɢ: Who asked (Feat: Nobody)\n ───────────⚪────── \n◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊")

        await intr.response.send_message(embed=em)
        
        

    
    @app_commands.command(name="flip", description="Flips a coin. What did you expect it to do?")
    async def flip(self, intr: Intr):
        '''
        Flips a coin. What did you expect it to do?
        '''
        responses = ["You got heads."] * 4 + ["You got tails."] * 4 + ["Oh? The coin landed on it's side!"]
        await intr.response.send_message("Wait for it!")
        time.sleep(random.uniform(1,3))
        await intr.followup.send(random.choice(responses))


    @app_commands.command(name="dave", description=":3")
    async def dave(self, intr: Intr):
        '''
        #DAVEONTOP #FEARTHEDAVE", desc = "Ok? mad? sad? gonna cry? bad? ez? LLL LOOL #dave LLLLL #daveONTOP #daveSkyWars CRY? #daveBEDWARS #davePIT #daveSB #daveAIRLINES EASY #daveLEGITLUNAR #daveLLL #daveDOTGG #daveGG mad? :) LLLL CRY ABOUT IT? LOL?   #daveLEADERBOARDS #daveUNTOUCHABLE NO CONTEST LOL #daveCANNOTBESTOPPED #daveBEST #PAYFORTRUCE SO SAD LL?? DUELED ME LOL? #daveEZ #daveGG DOGWATER LOL GG HE PARTIED ME LMAOOOOOO SIT DOWN #daveONTOP LLLLLLLLLLLLLLLLLL MAD???? :) :) :) :) MAD? CRY L DANCE LLL #dave LLL #dave L BOXED L MAD????????? :) SOMEONE'S MAD :) :) :) L :) <3 HOW CAN YOU BE SO MAD :) lololol Accept that #dave is superior. :) L mad :) ? :) L
        '''
        em = await create_embed(await self.client.get_context(intr), title = "#DAVEONTOP #FEARTHEDAVE", desc = "Ok? mad? sad? gonna cry? bad? ez? LLL LOOL #dave LLLLL #daveONTOP #daveSkyWars CRY? #daveBEDWARS #davePIT #daveSB #daveAIRLINES EASY #daveLEGITLUNAR #daveLLL #daveDOTGG #daveGG mad? :) LLLL CRY ABOUT IT? LOL?   #daveLEADERBOARDS #daveUNTOUCHABLE NO CONTEST LOL #daveCANNOTBESTOPPED #daveBEST #PAYFORTRUCE SO SAD LL?? DUELED ME LOL? #daveEZ #daveGG DOGWATER LOL GG HE PARTIED ME LMAOOOOOO SIT DOWN #daveONTOP LLLLLLLLLLLLLLLLLL MAD???? :) :) :) :) MAD? CRY L DANCE LLL #dave LLL #dave L BOXED L MAD????????? :) SOMEONE'S MAD :) :) :) L :) <3 HOW CAN YOU BE SO MAD :) lololol Accept that #dave is superior. :) L mad :) ? :) L")

        await intr.response.send_message(embed = em)


    @app_commands.command(name="rocketleague", description="Sends a random Rocket League quick chat.")
    async def rocketleague(self, intr: Intr):
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

        await intr.response.send_message(descrip)

    @app_commands.command(name="ratio", description="ratio")
    async def ratio(self, intr: Intr, *, target: Member = None):
        '''
        Optional argument: `target`

        Send a ratio message in chat. Optionally ratio someone
        '''
        if target != None:
            msg = await intr.response.send_message(f"{target.mention} ratio")
        else:
            msg = await intr.response.send_message("ratio")

        await msg.add_reaction("👍")

    @app_commands.command(name="areyouonline")
    async def areyouonline(self, intr: Intr):
        '''
        :3
        '''
        em = await create_embed(await self.client.get_context(intr), title = "Nope!", desc = "DaveedBot is currently offline and unable to respond to ANY commands. :3")
        await intr.response.send_message(embed=em)

    
    @app_commands.command(name="cry", description="Sends a random Cry About It gif.")
    async def cry(self, intr: Intr):
        '''
        Sends a random 'Cry About It' gif.
        '''
        scene = random.randint(1,24)

        crypath = os.path.join(DIR, "cogs/Media/Cry/cryaboutit{}.gif".format(scene))
        cryfile = "cryaboutit{}.gif".format(scene)
        
        file = discord.File(crypath, filename = cryfile)
        embed = discord.Embed(title = "Cry about it", colour = 0xff0000)
        embed.set_image(url = "attachment://{}".format(cryfile))

        await intr.response.send_message(file = file, embed = embed)



    @app_commands.command(name="limote", description="Sends a random Lisek Emoji (limote:tm:).")
    async def limote(self, intr: Intr):
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

        await intr.response.send_message(random.choice(responses))

    @app_commands.command(name="fox", description="Summon a fox.")
    async def fox(self, intr: Intr):
        '''
        Get a random picture of a fox.
        '''
        em = discord.Embed(title = f"Fox!", color = 0xff0000)
        em.set_image(url = f"https://randomfox.ca/images/{random.randint(1, 123)}.jpg")

        await intr.response.send_message(embed = em)


    @app_commands.command(name="null", description="...")
    async def null(self, intr: Intr):
        await intr.response.send_message("⠀", ephemeral=True)

        

async def setup(client):
    await client.add_cog(Simple(client))