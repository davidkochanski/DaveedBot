import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MemberConverter, MemberNotFound, Context
import random
import os
from PIL import Image, ImageOps
import requests
import json

class Utils:
    global DIR
    DIR = os.path.dirname(__file__)[:-5]

    async def generic_embed(ctx: Context, title: str, *, desc:str = None, colour = 0xff0000, name = None):
        
        if desc != None:
            em = nextcord.Embed(title = title,
                            description = desc + "\n ",
                            colour = colour)
        else:
            em = nextcord.Embed(title = title,
                            colour = colour)
        
        filepath = os.path.join(DIR,"cogs\\Media\\proto.png")
        fl = nextcord.File(filepath, filename = "proto.png")

        em.set_thumbnail(url = "attachment://{}".format("proto.png"))
        em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))
        
        if name != None:
            em.set_author(name = name)
        
        await ctx.send(embed = em, file = fl)


    async def generic_error(ctx: Context, error: Exception = None):
        face = ["TwT", ">w>", "<w<", ".w.", "-w-", "~w~", "XwX", "=w=", ";w;", "\_w\_", "\*w\*", "@w@", "QwQ", "qwq"]

        em = nextcord.Embed(title = "Oh no!",
                        description = "Something went wrong! {}\n\n`{}`".format(random.choice(face), error),
                        colour = 0xffff00)

        filepath = os.path.join(DIR,"cogs\\Media\\proto.png")
        fl = nextcord.File(filepath, filename = "proto.png")
                
        em.set_thumbnail(url = "attachment://{}".format("proto.png"))
        em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))
        
        await ctx.send(embed = em, file = fl)



    async def conv_member(ctx: Context, string: str, to_name:bool = False):
        '''
        Attempts to convert String to Member object.

        Returns
        -------
        The original input if member conversion is unsuccessful;
        - The member is not found, or
        - Something that is not a string is passed.

        A nextcord.member.Member type object if member conversion is successful.
        '''
        try:
            converter = MemberConverter()
            member = await converter.convert(ctx, string)

        except MemberNotFound:
            return string

        except TypeError:
            return string

        return member.name if to_name else member



    async def is_member(ctx: Context, target) -> bool:
        try:
            converter = MemberConverter()
            await converter.convert(ctx, target)
            return True

        except MemberNotFound:
            return False

        except TypeError:
            return False


    async def scenify(ctx: Context, target, texts: list, is_self: str=None, special_cases: list(tuple())=None) -> None:
        '''Displays a Discord embed.

        First checking for if user passed theirselves as the argument, then check if user passed some special case as the argument,
        and finally defaulting to a random selection from a list of responses.

        Note
        ----
        In all texts, use "{n}" in place of author, and "{t}" in place of target.
        
        Parameters
        ----------
        ctx : Context
            Nextcord context object
        target
            The name that the user called when using an action command.
        texts : list
            list of texts, that one of which will be randomly selected if none of the other conditions is satisfied.
        is_self : str
            a singluar string that is displayed if the user calls the target to be themselves.
        special_cases : list(tuple()) 
            a list of tuples, where the first item in the tuple is the name that has to be inputted for the special case override the message, and the second item is the message that will be displayed instead.
        '''
        name = await Utils.conv_member(ctx, target, to_name=True)
        if is_self is not None:
            if name == ctx.author.mention or name == ctx.author.name:

                await Utils.generic_embed(ctx, title = is_self.replace("{n}", ctx.author.name).replace("{t}", name))
                return
        
        if special_cases is not None:
            for tups in special_cases:
                if target == tups[0]:
                    await Utils.generic_embed(ctx, title = tups[1].replace("{n}", ctx.author.name).replace("{t}", name))
                    return
        await Utils.generic_embed(ctx, title = texts[random.randint(0, len(texts)-1)].replace("{n}", ctx.author.name).replace("{t}", name))



    async def generate_filepath(ctx: Context, target, name: str, ext: str) -> tuple[str]:
        '''Generates a filepath given a name, extention, and the local directory.

        Parameters
        ----------
        ctx : Context
            Nextcord context object
        target
            The name that the user called when using an action command.
        name : str
            The intended file name.
        ext : str
            The file extension. (png, gif, et cetera)

        Returns
        -------
        tuple[str]
            Where the index 0 is the full directory of the saved file,
            and the index 1 is just the file name and extension
        '''
        if target == None:
            target = ctx.author

        if target.name.isascii() and not " " in target.name:
            myfile = "{}_{}".format(name, target.name)
        else:
            myfile = "{}_{}".format(name, target.id)

        return os.path.join(DIR, f'cogs\\Save\\{name}\\{myfile}.{ext}'), f"{myfile}.{ext}"



    async def read_av(ctx: Context, target, size:int = 512, *, force_avatar:bool = False, force_square:bool = False, force_first_frame:bool = False):
        '''
            Attempts to read a client's attachment image, or if none exist, their Discord profile picture

            Parameters
            ----------
            ctx : Context
                Nextcord context object
            target
                The name that the user called when using an action command.
            size : int (default 512)
                How many pixels the image will be resized to.
            force_avatar : bool
                optionally always ignore the user's attachments and instead take their avatar.
            force_square : bool
                optionally force the aspect ratio of the returned image to be 1:1 instead of maintaining aspect ratio given.
            
            Returns
            -------
            PIL png, jpeg, or gif object.
            
        '''
            
        ALLOWED_TYPES = ["image/gif", "image/jpeg", "image/png"]

        if ctx.message.attachments and ctx.message.attachments[0].content_type in ALLOWED_TYPES and not force_avatar:
            if ctx.message.attachments[0].content_type == "image/gif":
                img = Image.open((requests.get(ctx.message.attachments[0].url, stream=True).raw))
                img.seek(0) # First frame of GIF
                return img.resize((size, size)).convert("RGBA") if force_square else ImageOps.contain(img, (size, size))

            else:
                img = Image.open((requests.get(ctx.message.attachments[0].url, stream=True).raw))
                return img.resize((size, size)) if force_square else ImageOps.contain(img, (size, size))

        # No attachments in message that are valid
        else:
            if not isinstance(target, nextcord.member.Member) or target is None:
                target = ctx.message.author
            
            img = Image.open(requests.get(target.avatar.url, stream=True).raw)
            return img.resize((size, size)) if force_square else ImageOps.contain(img, (size, size))


    async def handle_guesses(ctx: Context, client: nextcord.client, name: str, correct_guesses: tuple[str], *excluded_guesses: tuple[str]) -> None:
        '''
        Handles user messages input for guessing games in this bot.

        Pass the context object and the client object to be able to read and send stuff
        name: name of command that is being handled
        correct_guesses: tuple that contains all correct guesses for the generated guessable
        excluded_guesses: optionally guesses that are on blacklist from triggering a correct response
        '''
        for _ in range(64): # time out after 64 messages
            message = await client.wait_for("message")
            msg = message.content.lower()
            if msg in correct_guesses and msg not in excluded_guesses:
                await Utils.generic_embed(ctx, title = f"Correct! {correct_guesses[0].title()}", desc = f"{message.author.name} got it!")


                with open(f"cogs\\Leaderboards\\{name}.json", "r") as fl:
                    lb_file = json.load(fl)

                user_key = str(message.author.id)

                if not user_key in lb_file:
                    lb_file[user_key] = [0, []]


                lb_file[user_key][0] += 1 # alltime_points

                alltime_seen = lb_file[user_key][1]
                if correct_guesses[0] not in alltime_seen:
                    alltime_seen.append(correct_guesses[0])
                
                with open(f"cogs\\Leaderboards\\{name}.json", "w") as fl:
                    json.dump(lb_file, fl)


                break
            elif msg == "d!idk":
                await Utils.generic_embed(ctx, title = f"It's ||{correct_guesses[0].title()}!||")
                break
            elif msg == "d!hint":
                await Utils.generic_embed(ctx, title = f"It starts with the letter '{correct_guesses[0][0]}'")
            elif msg == "d!len":
                await Utils.generic_embed(ctx, title = f"It's name is {len(correct_guesses[0])} letters long")
            elif msg == f"d!{name}":
                # New instance of command called
                break


    async def display_leaderboard(ctx: Context, name: str):
        with open(f"cogs\\Leaderboards\\{name}.json", "r") as fl:
            lb_mon = json.load(fl)

        top_users = {k: v for k, v in sorted(lb_mon.items(), key=lambda item: item[1], reverse=True)}
        print(top_users)

        desc = f"Name **|** All-time {name.title()}s Guessed **|** Unique {name.title()}s Guessed__\n"
        for pos, user in enumerate(top_users):
            if pos == 10:
                break

            if pos == 0:
                desc += ":first_place: "
            elif pos == 1:
                desc += ":second_place: "
            elif pos == 2:
                desc += ":third_place: "
            else:
                desc += ":military_medal: "

            desc += f'{pos+1}. <@!{user}> | {top_users[user][0]} | {len(top_users[user][1])}\n'

        await Utils.generic_embed(ctx, title = f"{name.title()} Leaderboards", desc = desc)
        




    