from util.BotUtils import DIR, generate_filepath, generic_embed, read_av, conv_member
import discord
from discord import Interaction as Intr
from discord import Member, app_commands
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands.errors import BadBoolArgument
import os
from PIL import Image, ImageSequence
import requests


class Avatars(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="av", description="Get someone's avatar")
    async def av(self, intr: Intr, *, target: Member = None):
        '''
        Optional argument: `target`
        
        Returns the avatar of who you specified, or yourself if you didnt specify anyone.
        '''

        if target == None:
            target = intr.user
            
        embed = discord.Embed(title = f"Avatar of {target.name}", 
                                description = "" if target.id != 763914302175445002 else "Hey, that's me! :3",
                                colour = 0xff0000)
        embed.set_image(url = target.avatar.url)

        await intr.response.send_message(embed = embed)
        

    @app_commands.command(name="jar", description="Puts whoever you want, or any attached image into a jar!")

    async def jar(self, intr: Intr, *, target: Member = None, use_my_own_image: bool = False):
        '''
        Optional argument: `target`

        Puts whoever you want, or any attached image into a jar!
        '''
        ctx = await self.client.get_context(intr)


        # TODO this works, but make it cleaner and update all other commands

        def check(msg: discord.Message):
            return msg.channel.id == ctx.channel.id 

        if use_my_own_image:
            await intr.response.send_message("Please send your image now.", ephemeral=True)
            msg: discord.Message = await self.client.wait_for("message", check = check)
            av = Image.open((requests.get(msg.attachments[0].url, stream=True).raw)).resize((256,256))
    
        else:
            av = await read_av(ctx, target, 256, force_square = True)

            

        filepath, filename = await generate_filepath(ctx, target, "jar", "png")

        jar = Image.open(os.path.join(DIR, "cogs/Media/mtjar.png"))

        jar.paste(av,(230, 420))
        jar.save(filepath)
        fl = discord.File(filepath, filename = filename)

        if target is not None:
            title = "-w-" if target.id == 763914302175445002 else f"{target.name} in a jar!"
        else:
            title = ""

        em = discord.Embed(title = title, colour = 0xff0000)
        em.set_image(url = f"attachment://{filename}")
        if use_my_own_image:
            await intr.followup.send(embed = em, file = fl)
        else:
            await intr.response.send_message(embed = em, file = fl)






    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def pet(self, ctx: Context, *, target: Member = None):
        '''
        Optional argument: `target`

        Pet whoever you want, or any attached image, or even yourself!
        '''
        filepath, filename = await generate_filepath(ctx, target, "pet", "gif")

        gifHand = Image.open(fp = os.path.join(DIR, f'cogs/Media/petpet.gif'))
        av = await read_av(ctx, target, 512)

        allFrames = []
        for gifFrame in ImageSequence.Iterator(gifHand):
            newFrame = av.copy()
            gifFrame = gifFrame.convert("RGBA")
            newFrame.paste(gifFrame, mask = gifFrame)
            allFrames.append(newFrame)
        
        allFrames[0].save(filepath, save_all = True,append_images=allFrames[1:], duration=100, loop=0)

        fl = discord.File(filepath, filename = filename)

        if target is not None:
            title = f"{ctx.author.name} pets themselves!" if ctx.author == target else f"{ctx.author.name} pets {target.name}!"
        else:
            title = ""

        em = discord.Embed(title = title, colour = 0xff0000)

        em.set_image(url = f"attachment://{filename}")
        await ctx.send(embed = em, file = fl)




    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def speech(self, ctx: Context, *, target: Member = None):
        '''
        Optional argument: `target`

        Places a Speech Bubble overlay over any attached images, or the avatar of whoever you specified.
        '''
        filepath, filename = await generate_filepath(ctx, target, "speech", "gif")
        av = await read_av(ctx, target, 512)

        bubble = Image.open(os.path.join(DIR, f'cogs/Media/speech.png')).convert('L').resize(av.size)
        rim = Image.open(os.path.join(DIR, f'cogs/Media/speech_rim.png')).convert("RGBA").resize(av.size)

        av.paste(rim, (0,0), rim)
        av.putalpha(bubble)
        av.save(filepath)

        em = discord.Embed(title = "", colour = 0xff0000)
        em.set_image(url = f"attachment://{filename}")

        fl = discord.File(filepath, filename = filename)
        await ctx.send(file = fl, embed = em)


    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def pride(self, ctx: Context, flag: str, *, target: Member = None):
        '''
        Requred argument: `flag`
        Optional argument: `target`

        Overlays a pride flag of your choosing over an attached image, or the avatar of whoever you specified.
        '''
        flags = {
            "gay": ["gay", "homosexual"],
            "trans": ["trans", "transgender"],
            "bi": ["bi", "bisexual"],
            "pan": ["pan", "pansexual"],
            "enby": ["enby", "nonbinary", "non binary", "nb"],
            "asexual": ["asexual", "ace", "ase"],
            "genderfluid": ["genderfluid", "fluid"],
            "ally": ["ally", "pride", "progress", "lgbt", "lgbtq", "lgtbq+"],
            "agender": ["agender"],
            "lesbian": ["lesbian"],
            "queer": ["queer", "genderqueer"],
            "aro": ["aro", "aromantic"],
            "poly": ["poly", "polyamoury", "polyamory"],
            "intersex": ["intersex", "inter", "intersexual"]
        }
        
        if flag.lower() == "list":
            await ctx.send(flags)
            return

        filepath, filename = await generate_filepath(ctx, target, "pride", "png")
        av = await read_av(ctx, target, 512, force_square = True)
        av.convert("RGBA")


        flag_filename = None

        for key in flags:
            for i in range(len(flags[key])):
                if flag.lower() == flags[key][i]:
                    flag_filename = flags[key][0]
                    break
        
        if flag_filename is not None:
            flagimg = Image.open(os.path.join(DIR, f'cogs/Media/Pride/{flag_filename}.png')).convert("RGBA").resize(av.size)
            av.paste(flagimg, (0,0), flagimg)
            av.save(filepath)

            fl = discord.File(filepath, filename = filename)
            em = discord.Embed(title = f"", colour = 0xff0000)

            em.set_image(url = f"attachment://{filename}")

            await ctx.send(file = fl, embed = em)
        else:
            await generic_embed(ctx, "Missing or inappropriate argument!",
                                      desc = "Try d!pride `[flag]` `[name]`")



    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def ascii(self, ctx: Context, arg = None, size: int = 21, inv = False):
        '''
        Optional argument: `target`
        Optional argument: `size`, default 21x21
        Optional argument: `inv`, default False

        Converts an image or an avatar of a person into ASCII art!
        `size` will change the dimentions of the image. Don't go too big!
        `inv` will invert the output. Use a boolean. (true / false)
        '''
        if size > 30 or size < 1:
            await ctx.send("`size` must be at most 30 and at least 1... are you trying to kill me or something?")
            return

        try:
            inv = bool(inv)
        except BadBoolArgument:
            await ctx.send("`invert` flag must be a boolean value (try True / False)")
            return

        arg = await conv_member(ctx, arg)
        av = await read_av(ctx, arg, size)

        img = av.convert("L")
        pixel_list = list(img.getdata())

        string = ""
        counter = 0

        chars = ['$','8','#','b','w','0','X','u',')','}','-','<','l',',',".",' ']

        if inv:
            chars.reverse()

        for i in pixel_list:
            string += chars[i // 16]
            string += ' '

            counter += 1
            if counter == size:
                counter = 0
                string += '\n'

        await ctx.send(f"```{string}```")

    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def sub(self, ctx: Context, *, target: Member = None):
        '''
        Optional argument: `target`

        Overlays an attachment or the avatar of the member specified onto a Subway logo.
        '''
        filepath, filename = await generate_filepath(ctx, target, "sub", "jpg")

        template = Image.open(os.path.join(DIR, "cogs\Media\subway_template.jpg"))
        av = await read_av(ctx, target, 256, force_square=True)

        template.paste(av, (74, 118))
        template.save(filepath)
        fl = discord.File(filepath, filename = filename)

        em = discord.Embed(color = 0xff0000)
        em.set_image(url = f"attachment://{filename}")

        await ctx.send(file = fl, embed = em)

    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def dom(self, ctx: Context, *, target: Member = None):
        '''
        Optional argument: `target`

        Overlays an attachment or the avatar of the member specified onto a Dominos Pizza logo.
        '''
        filepath, filename = await generate_filepath(ctx, target, "dom", "jpg")

        template = Image.open(os.path.join(DIR, "cogs\Media\dominos_template.jpg"))
        av = await read_av(ctx, target, 256, force_square=True)

        template.paste(av, (195, 118))
        template.save(filepath)
        fl = discord.File(filepath, filename = filename)

        em = discord.Embed(color = 0xff0000)
        em.set_image(url = f"attachment://{filename}")

        await ctx.send(file = fl, embed = em)

async def setup(client):
    await client.add_cog(Avatars(client))
