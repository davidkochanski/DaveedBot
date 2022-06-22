from calendar import c
from util.BotComs import Coms 
from util.BotComs import DIR
import nextcord
from nextcord import Member
from nextcord.ext import commands
import os
import PIL
from PIL import Image, ImageSequence
from io import BytesIO


class Avatars(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def av(self, ctx, target: Member = None):
        if target == None:
            target = ctx.author
        embed = nextcord.Embed(title = f"Avatar of {target.name}", 
                                description = "" if target.id != 763914302175445002 else "Hey, that's me! :3",
                                colour = 0xff0000)
        embed.set_image(url = target.avatar_url_as(size = 512))

        await ctx.send(embed = embed)
    @av.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await Coms.generic_error(ctx)


    @commands.command()
    async def jar(self, ctx, target: Member = None):
        filepath, filename = await Coms.generate_filepath(ctx, target, "jar", "png")

        jar = Image.open(os.path.join(DIR, "Media\\mtjar.png"))
        av = await Coms.read_av(ctx, target, 256)

        jar.paste(av,(230, 420))
        jar.save(filepath)

        fl = nextcord.File(filepath, filename = filename)
        em = nextcord.Embed(title = f"{target.name} in a jar!" if target.id != 763914302175445002 else "-w-",
                           colour = 0xff0000)

        em.set_image(url = f"attachment://{filename}")
        await ctx.send(embed = em, file = fl)
    @jar.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await Coms.generic_error(ctx)



    @commands.command()
    async def pet(self, ctx, target: Member = None):
        filepath, filename = await Coms.generate_filepath(ctx, target, "pet", "gif")

        gifHand = Image.open(fp = os.path.join(DIR, f'Media\\petpet.gif'))
        av = await Coms.read_av(ctx, target, 512)

        allFrames = []
        for gifFrame in ImageSequence.Iterator(gifHand):
            newFrame = av.copy()
            gifFrame = gifFrame.convert("RGBA")
            newFrame.paste(gifFrame, mask = gifFrame)
            allFrames.append(newFrame)
        
        allFrames[0].save(filepath, save_all = True,append_images=allFrames[1:], duration=100, loop=0)

        fl = nextcord.File(filepath, filename = filename)
        em = nextcord.Embed(title = f"{ctx.author.name} pets {target.name}!", colour = 0xff0000)

        em.set_image(url = f"attachment://{filename}")
        await ctx.send(embed = em, file = fl)
    @pet.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await Coms.generic_error(ctx)



    @commands.command()
    async def speech(self, ctx, target: Member = None):
        filepath, filename = await Coms.generate_filepath(ctx, target, "speech", "gif")
        av = await Coms.read_av(ctx, target, 512)

        bubble = Image.open(os.path.join(DIR, f'Media\\speech.png')).convert('L').resize(av.size)
        rim = Image.open(os.path.join(DIR, f'Media\\speech_rim.png')).convert("RGBA").resize(av.size)

        av.putalpha(bubble)
        av.paste(rim, (0,0), rim)
        av.save(filepath)

        em = nextcord.Embed(title = "", colour = 0xff0000)
        em.set_image(url = f"attachment://{filename}")

        fl = nextcord.File(filepath, filename = filename)
        await ctx.send(file = fl, embed = em)
    @speech.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await Coms.generic_error(ctx)


    @commands.command()
    async def pride(self, ctx, flag: str = "Gay", target: Member = None, ):
        filepath, filename = await Coms.generate_filepath(ctx, target, "pride", "png")
        av = await Coms.read_av(ctx, target, 512)
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
            flagimg = Image.open(os.path.join(DIR, f'Media\\Pride\\{flag_filename}.png')).convert("RGBA").resize(av.size)
            av.paste(flagimg, (0,0), flagimg)
            av.save(filepath)

            fl = nextcord.File(filepath, filename = filename)
            em = nextcord.Embed(title = f"", colour = 0xff0000)

            em.set_image(url = f"attachment://{filename}")

            await ctx.send(file = fl, embed = em)
        else:
            await Coms.generic_embed(ctx, "Missing or inappropriate argument!",
                               desc = "Try d!pride `[flag]` `[name]`")

    @pride.error
    async def info_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await Coms.generic_error(ctx)


    @commands.command()
    async def ascii(self, ctx, target: Member = None, inv: bool = False):

        av = await Coms.read_av(ctx, target, 21)


        img = av.convert("L")

        pixel_list = list(img.getdata())

        string = ""
        counter = 0
        
        if not inv:
            for i in pixel_list:
                if i > 239:
                    string += '  '
                elif i > 223:
                    string += '. '
                elif i > 191:
                    string += '- '
                elif i > 159:
                    string += ': '
                elif i > 127:
                    string += '; '
                elif i > 95:
                    string += 'o '
                elif i > 63:
                    string += 'X '
                elif i > 31:
                    string += '# '
                else:
                    string += '@ '

                counter += 1

                if counter == 21:
                    counter = 0
                    string += '\n'

        else:
            for i in pixel_list:
                if i > 239:
                    string += '@ '
                elif i > 223:
                    string += '# '
                elif i > 191:
                    string += 'X '
                elif i > 159:
                    string += 'o '
                elif i > 127:
                    string += '; '
                elif i > 95:
                    string += ': '
                elif i > 63:
                    string += '- '
                elif i > 31:
                    string += '. '
                else:
                    string += '  '

                counter += 1

                if counter == 21:
                    counter = 0
                    string += '\n'


        

            

        print(string)
        
        await ctx.send(f"```{string}```")








def setup(client):
    client.add_cog(Avatars(client))
