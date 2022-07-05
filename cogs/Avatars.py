from util.BotUtils import Utils 
from util.BotUtils import DIR
import nextcord
from nextcord import Member
from nextcord.ext import commands
from nextcord.ext.commands import Context
from nextcord.ext.commands.errors import BadBoolArgument
import os
from PIL import Image, ImageSequence


class Avatars(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def av(self, ctx: Context, target: Member = None):
        if target == None:
            target = ctx.author
        embed = nextcord.Embed(title = f"Avatar of {target.name}", 
                                description = "" if target.id != 763914302175445002 else "Hey, that's me! :3",
                                colour = 0xff0000)
        embed.set_image(url = target.avatar.url)

        await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def jar(self, ctx: Context, target: Member = None):
        filepath, filename = await Utils.generate_filepath(ctx, target, "jar", "png")

        jar = Image.open(os.path.join(DIR, "cogs\\Media\\mtjar.png"))
        av = await Utils.read_av(ctx, target, 256, force_square = True)

        jar.paste(av,(230, 420))
        jar.save(filepath)
        fl = nextcord.File(filepath, filename = filename)

        # TODO Maybe make this into a method safe_target_title()
        if target is not None:
            title = "-w-" if target.id == 763914302175445002 else f"{target.name} in a jar!"
        else:
            title = ""

        em = nextcord.Embed(title = title, colour = 0xff0000)
        em.set_image(url = f"attachment://{filename}")
        await ctx.send(embed = em, file = fl)


    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def pet(self, ctx: Context, target: Member = None):
        filepath, filename = await Utils.generate_filepath(ctx, target, "pet", "gif")

        gifHand = Image.open(fp = os.path.join(DIR, f'cogs\\Media\\petpet.gif'))
        av = await Utils.read_av(ctx, target, 512)

        allFrames = []
        for gifFrame in ImageSequence.Iterator(gifHand):
            newFrame = av.copy()
            gifFrame = gifFrame.convert("RGBA")
            newFrame.paste(gifFrame, mask = gifFrame)
            allFrames.append(newFrame)
        
        allFrames[0].save(filepath, save_all = True,append_images=allFrames[1:], duration=100, loop=0)

        fl = nextcord.File(filepath, filename = filename)

        if target is not None:
            title = f"{ctx.author.name} pets themselves!" if ctx.author == target else f"{ctx.author.name} pets {target.name}!"
        else:
            title = ""

        em = nextcord.Embed(title = title, colour = 0xff0000)

        em.set_image(url = f"attachment://{filename}")
        await ctx.send(embed = em, file = fl)




    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def speech(self, ctx: Context, target: Member = None):
        filepath, filename = await Utils.generate_filepath(ctx, target, "speech", "gif")
        av = await Utils.read_av(ctx, target, 512)

        bubble = Image.open(os.path.join(DIR, f'cogs\\Media\\speech.png')).convert('L').resize(av.size)
        rim = Image.open(os.path.join(DIR, f'cogs\\Media\\speech_rim.png')).convert("RGBA").resize(av.size)

        av.paste(rim, (0,0), rim)
        av.putalpha(bubble)
        av.save(filepath)

        em = nextcord.Embed(title = "", colour = 0xff0000)
        em.set_image(url = f"attachment://{filename}")

        fl = nextcord.File(filepath, filename = filename)
        await ctx.send(file = fl, embed = em)


    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def pride(self, ctx: Context, flag: str, target: Member = None):
        filepath, filename = await Utils.generate_filepath(ctx, target, "pride", "png")
        av = await Utils.read_av(ctx, target, 512)
        print(type(av))
        av.convert("RGBA")
        flags = {
            "gay": ["gay", "homosexual"],
            "trans": ["trans", "transgender"],
            "bi": ["bi", "bisexual"],
            "pan": ["pan", "pansexual"],
            "enby": ["enby", "nonbinary", "non binary"],
            "asexual": ["asexual", "ace"],
            "genderfluid": ["genderfluid", "fluid"],
            "ally": ["ally", "pride"],
            "agender": ["agender"],
            "lesbian": ["lesbian"],
            "queer": ["queer", "genderqueer"],
            "aro": ["aro", "aromantic"],
            "poly": ["poly", "polyamoury", "polyamory"],
            "intersex": ["intersex", "inter", "intersexual"]
        }

        flag_filename = None

        for key in flags:
            for i in range(len(flags[key])):
                if flag.lower() == flags[key][i]:
                    flag_filename = flags[key][0]
                    break
        
        if flag_filename is not None:
            flagimg = Image.open(os.path.join(DIR, f'cogs\\Media\\Pride\\{flag_filename}.png')).convert("RGBA").resize(av.size)
            av.paste(flagimg, (0,0), flagimg)
            av.save(filepath)

            fl = nextcord.File(filepath, filename = filename)
            em = nextcord.Embed(title = f"", colour = 0xff0000)

            em.set_image(url = f"attachment://{filename}")

            await ctx.send(file = fl, embed = em)
        else:
            await Utils.generic_embed(ctx, "Missing or inappropriate argument!",
                                      desc = "Try d!pride `[flag]` `[name]`")



    @commands.command()
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def ascii(self, ctx: Context, arg = None, size: int = 21, inv = False):
        if size > 30 or size < 1:
            await ctx.send("`size` must be at most 30 and at least 1... are you trying to kill me or something?")
            return

        try:
            inv = bool(inv)
        except BadBoolArgument:
            await ctx.send("`invert` flag must be a boolean value (try True/False)")
            return

        arg = await Utils.conv_member(ctx, arg)
        av = await Utils.read_av(ctx, arg, size)

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


def setup(client):
    client.add_cog(Avatars(client))
