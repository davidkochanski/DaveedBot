from types import MemberDescriptorType
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MemberConverter, MemberNotFound
import random
import os
from PIL import Image
import requests


class Coms:
    global DIR
    DIR = os.path.dirname(__file__)[:-5]

    async def generic_embed(ctx, title, *, desc = None, colour = 0xff0000, name = None):
        if desc != None:
            em = nextcord.Embed(title = title,
                            description = desc + "\n ",
                            colour = colour)
        else:
            em = nextcord.Embed(title = title,
                            colour = colour)
        
        filepath = os.path.join(DIR,"..\\cogs\\Media\\proto.png")
        fl = nextcord.File(filepath, filename = "proto.png")

        em.set_thumbnail(url = "attachment://{}".format("proto.png"))
        em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))
        
        if name != None:
            em.set_author(name = name)
        
        await ctx.send(embed = em, file = fl)


    async def generic_error(ctx):
        face = ["TwT", ">w>", "<w<", ".w.", "-w-", "~w~", "XwX", "=w=", ";w;", "\_w\_", "\*w\*", "@w@", "QwQ", "qwq"]

        em = nextcord.Embed(title = "Oh no!",
                        description = "Something went wrong! {}".format(random.choice(face)),
                        colour = 0xffff00)

        filepath = os.path.join(DIR,"..\\cogs\\Media\\proto.png")
        fl = nextcord.File(filepath, filename = "proto.png")
                
        em.set_thumbnail(url = "attachment://{}".format("proto.png"))
        em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))
        
        await ctx.send(embed = em, file = fl)



    async def conv_member(ctx, string):
        '''
        Attempts to convert String to Member object.
        '''
        try:
            converter = MemberConverter()
            member = await converter.convert(ctx, string)

        except MemberNotFound:
            return string

        except TypeError:
            return string

        return member



    async def is_member(ctx, target) -> bool:
        try:
            converter = MemberConverter()
            await converter.convert(ctx, target)
            return True

        except MemberNotFound:
            return False

        except TypeError:
            return False


    async def scenify(ctx, target, texts: list, is_self: str=None, special_cases: list(tuple())=None):
        target = await Coms.conv_member_name(ctx, target)
        if is_self is not None:
            if target == ctx.author.mention or target == ctx.author.name:
                await Coms.generic_embed(ctx, title = is_self.replace("{n}", ctx.author.name).replace("{t}", target))
                return
            
        if special_cases is not None:
            for tups in special_cases:
                if target == tups[0]:
                    await Coms.generic_embed(ctx, title = tups[1].replace("{n}", ctx.author.name).replace("{t}", target))
                    return
        
        await Coms.generic_embed(ctx, title = texts[random.randint(0, len(texts)-1)].replace("{n}", ctx.author.name).replace("{t}", target))



    async def generate_filepath(ctx, target, name: str, ext: str):
        if target == None:
            target = ctx.author

        if target.name.isascii() and not " " in target.name:
            myfile = "{}_{}".format(name, target.name)
        else:
            myfile = "{}_{}".format(name, target.id)

        return os.path.join(DIR, f'cogs\\Save\\{name}\\{myfile}.{ext}'), f"{myfile}.{ext}"



    async def read_av(ctx, target, size:int = 512, *, force_avatar:bool = False):
            
        ALLOWED_TYPES = ["image/gif", "image/jpeg", "image/png"]

        if ctx.message.attachments and ctx.message.attachments[0].content_type in ALLOWED_TYPES and not force_avatar:
            if ctx.message.attachments[0].content_type == "image/gif":
                img = Image.open((requests.get(ctx.message.attachments[0].url, stream=True).raw))
                img.seek(0)
                return img.resize((size, size)).convert("RGBA")
            
            else:
                img = Image.open((requests.get(ctx.message.attachments[0].url, stream=True).raw))
                return img.resize((size, size))

        # No attachments in message that are valid
        else:
            if not isinstance(target, nextcord.member.Member) or target is None:
                target = ctx.message.author
            
            img = Image.open(requests.get(target.avatar.url, stream=True).raw)
            return img.resize((size, size))
        




    