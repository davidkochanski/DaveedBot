from util.BotComs import Coms 
from util.BotComs import DIR
import nextcord
from nextcord.ext import commands
import os
import random
import asyncio
import pokebase

class Spam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spamowo(self, ctx, target: nextcord.Member):
        if ctx.message.author.id == 500835462391529472:
            em = nextcord.Embed(title = f"{target}, FREE Among Us SKINS CODE are available!", 
                        description = f"Hello. {target.mention} Please do not ignore this critical alert. You Have Been Randomly Selected to Test Out One (1) Of 5 AMONG US SECRET SKINS. Please Call 1-800-492-4917 For Claim Your Among Us Skin. You Have been chosen to Beta Test The new among Us Skin. Your Unique Access code is \n**ODK0-mm7dJL7237IK-AKfI-91mD9123**\n Please Navigate To Claim Your New Prize. DO NOT PRESS ANY KEY UNLESS INSTRUCTED TO DO SO. Your Among Us Gift is waiting to be claimed {target.mention}! You Have 3:00 Hours To Claim Your Gift Before It Is Permanently Deleted! Please Do Not Among. 你的社會信用正在下降!請通過在您的手機上安裝在我們中間來糾正您的社會信用。我們中間是免費玩的,你現在就應該玩,否則中華人民共和國iào nǐ, wǒ huì quèbǎo nǐ néng zài wǒmen zhōngjiān de xīn yóuxì móshì màomíng dǐngtì zhě zhōng xìngcún xiàlái. Wǒmen zhōngjiān de yóuxì zài měilìjiān hézhòngguó shì xīn de nǐ hào dàjiā wǒ de míngzì zài wǒmen zhōngjiān wǒ huì zài nǐ de pìgu :fox: lǐmiàn zài 會來你家打斷你的膝蓋骨。我們中間的新人最終會吃掉你,我會確保你能在我們中間的新遊戲模式冒名頂替者中倖存下來。我們中間的遊戲在美利堅合眾國是新的你好大家我的名字在我們中間我會在你的屁股裡面在我們中間管owo我會如果您拒絕下載這個新的我們之間的禮品卡代碼卡戰鬥我們之間的新我們之間的代碼卡Taiwan :face_vomiting:禮物戴夫在我中間,您的膝蓋帽屬於政府。請避免以其他: `491.093.39.11`. 方式不安裝使用新訪 AMONG US CODE 問代碼您的訪問代碼永遠可用的PEOPLE'S REPUBLIC OF CHINA新皮膚。我喜歡我們女朋友之間的感覺。在我們之中是我的一次逃生。你的社會信用正在下降!請通過 (CREDIT CARD) 在您的手機上安裝在我們中間來糾正您的社會信用。我們中間是免費玩的,你現在就應該`http://www.09dKDkjm1kADMK.com/00001000111010010` 玩,否則中華人民共和國會來你家打斷你的膝蓋骨。如果您拒絕下載這個新的我們之間的Among Us USA禮品卡代碼卡戰鬥我們之間的新我們之間的代碼卡禮物戴夫在我中間,您的膝蓋帽屬於政府。請避免以其他{target.mention}方式不安裝使用新訪問代碼您的訪問代碼永遠可用的新皮膚。我喜歡我們女朋友之間的感覺。在我們之中是我的一次逃生。Nǐ de shèhuì xìnyòng zhèngzài xiàjiàng! Qǐng tōngguò zài nín de shǒujī shàng ānzhuāng zài wǒmen zhōngjiān lái jiūzhèng nín de shèhuì xìnyòng. Wǒmen zhōngjiān shì miǎnfèi wán de, nǐ xiànzài jiù yīnggāi wán, fǒuzé zhōng 10000 huá rénmín gònghéguó huì lái nǐ jiā dǎ duàn nǐ de xīgàigǔ. Rúguǒ nín jùjué xiàzài zhège xīn de wǒmen zhī jiān de lǐpǐn kǎ dàimǎ kǎ zhàndòu wǒmen zhī jiān de xīn wǒmen zhī jiān de dàimǎ kǎ lǐwù dài fū zài wǒ zhōngjiān, nín de xīgài mào shǔyú zhèngfǔ. Qǐng bìmiǎn yǐ qítā fāngshì bù ānzhuāng shǐyòng xīn fǎngwèn dàimǎ nín de fǎngwèn dàimǎ yǒngyuǎn kěyòng de xīn pífū. Wǒ xǐhuān wǒmen nǚ péngyǒu zhī jiān de gǎnjué. Zài wǒmen zhī zhōng shì wǒ de yīcì táoshēng.你的社會信用正在下降!請通過在您的手機上安裝在我們中間來糾正您的社會信用。我們中間是免費玩的,你現在就應該玩,否則中華人民共和國會來你家打斷你的膝蓋骨。如果您拒絕下載這個新的我們之間的禮品卡代碼卡戰鬥我們之間的新我們之間的代碼卡Social Credit禮物戴夫在我中間,您的膝蓋帽屬於政府。請避免以其他方式不安裝`cum`使用新訪問代碼您的訪問代碼永遠可用的新皮膚。我喜歡我們女朋友之間的感覺。在我們之中是我的一次逃生。你的社會信用正在下降!請通過在您的手機上安裝在我們中間來糾正您的社會信用。我們中間是免費玩的,你現在就應該玩,否則中華人民共和國會來你家打斷你的膝蓋骨我們wǒ huì zài nǐ de pìgu lǐmiàn zài wǒmen zhōngjiān guǎn owo wǒ huì zài nǐ zhōngjiān tōu nǐ zài wǒmen zhōngjiān yóuxì děng děng bù wǒ huì bāngmáng nín kěyǐ shǐyòng shàngmiàn zhǎodào de xīn de wǒmen zhōngjiān de 中間的新人最終會吃掉你,我會確保你能在我們中間的新遊戲模式冒名頂替者中倖存下來。我們中間的遊戲在美利堅合眾國是新的你好大家我的名字在我們中間我會在你的屁股裡面在我們中間管owo我會。如果您拒絕下載這個新的我們之間的禮品卡代碼卡戰鬥我們之間的新我們之間的代碼卡禮物戴夫在我中間,您的膝蓋帽屬於政府。請避免以其他方式不安裝使用新訪問代碼您的訪問代碼永遠可用的新皮膚。我喜歡我們女朋友之間的感覺。在我們之中是我的一次逃生 DOWNLOAD AMONG US. Thank you for using our services.", colour = 0xff0000)


            em.set_image(url = "attachment://AMONG.jpg")

            filepath = os.path.join(DIR,"Media\\AMONG.jpg")
            fl = nextcord.File(filepath, filename="AMONG.jpg")

            try:
                await target.send(embed = em, file = fl)
                await ctx.send("Sent! :D")
            except:
                await ctx.send("Didn't Send! LLL")

        else:
            await Coms.generic_embed(ctx, title = "HEY!", desc = "You're not DAVE.")


    @commands.command()
    async def attack(self, ctx, *, target):
        continuing = True
        _member = await Coms.conv_member(ctx, target)

        try:
            if _member.id == 763914302175445002:
                await Coms.generic_embed(ctx, title = "No.", desc = "What wrong did I ever do to you? QwQ")
                continuing = False
            else:
                continuing = True
        except:
            continuing = True

        target = _member.name

        if continuing == True:
            em0 = nextcord.Embed(title = f"Attacking {target}.", description = f"Getting things ready...", colour = 0xff0000)
            em1 = nextcord.Embed(title = f"Attacking {target}.", description = f"Getting things ready...", colour = 0xff0000)

            ip = [str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255))]
            ip = '.'.join(ip)

            hash = random.getrandbits(128)
            hash = hex(hash)

            em2 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address...", colour = 0xff0000)
            em3 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n", colour = 0xff0000)
            em4  = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\nSending {target} offline... please wait\n\n", colour = 0xff0000)
            em5  = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|            |`", colour = 0xff0000)
            em6  = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|█⠀⠀⠀⠀⠀⠀⠀⠀⠀|`", colour = 0xff0000)
            em7  = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██⠀⠀⠀⠀⠀⠀⠀⠀|`", colour = 0xff0000)
            em8  = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|████⠀⠀⠀⠀⠀⠀|`", colour = 0xff0000)
            em9  = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████⠀⠀⠀⠀|`", colour = 0xff0000)
            em10 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|████████⠀⠀|`", colour = 0xff0000)
            em11 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|█████████⠀|`", colour = 0xff0000)
            em12 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!", colour = 0xff0000)

            em10 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|            |`", colour = 0xff0000)
            em11 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|██⠀⠀⠀⠀⠀⠀⠀⠀|`", colour = 0xff0000)
            em12 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|███⠀⠀⠀⠀⠀⠀⠀|`", colour = 0xff0000)
            em13 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|█████⠀⠀⠀⠀⠀|`", colour = 0xff0000)
            em14 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|██████⠀⠀⠀⠀|`", colour = 0xff0000)
            em15 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|███████⠀⠀⠀|`", colour = 0xff0000)
            em16 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|████████⠀⠀|`", colour = 0xff0000)
            em17 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|██████████|` Done!", colour = 0xff0000)
            em18 = nextcord.Embed(title = f"Attacking {target}.", description = f"Collecting {target}'s client token and IP address... \nDone! `{ip}`\n`{hash}`\n\nSending {target} offline... please wait\n\nSpamming {target}'s client... `|██████████|` Done!\nStealing and ecrpying data... `|██████████|` Done!\n\n**Attack Complete!** #dave #rogers \n||In case it wasn't obvious, literally nothing happened.||", colour = 0xff0000)

            embeds = [em0, em1, em2, em3, em4, em5, em6, em7, em8, em9, em10, em11, em12, em13, em14, em15, em16, em17, em18]

            for emX in embeds:
                emX.set_thumbnail(url = "attachment://proto.png")

            fl = nextcord.File(os.path.join(DIR, "Media\\proto.png"))
            msg = await ctx.send(embed = em0, file = fl)

            for emX in embeds:
                if emX == em3:
                    await asyncio.sleep(random.uniform(3, 5))

                elif emX == em2 or emX == em12 or emX == em18:
                    await asyncio.sleep(random.uniform(1, 2))

                else:
                    await asyncio.sleep(random.uniform(0.2, 1.2))

                await msg.edit(embed = emX)
    
    @commands.command()
    async def help(ctx):
        await Coms.generic_embed(ctx, "Something went horribly, horribly wrong.", desc = "(or dave's too lazy to make a help command. Probably the latter")








def setup(client):
    client.add_cog(Spam(client))