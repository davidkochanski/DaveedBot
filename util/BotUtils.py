import discord
from discord import app_commands
from discord import interactions as Intr
from discord.ext import commands
from discord.ext.commands import MemberConverter, MemberNotFound, Context
import random
import os
from PIL import Image, ImageOps
import requests
import json
from datetime import datetime 
import colorama
from colorama import Fore
import traceback

def printl(s, end="\n") -> None:
    colorama.init()
    now = datetime.now().strftime("%b %d %Y %H:%M:%S")

    if isinstance(s, Exception):
        print(f"{Fore.RED}[{now}]{Fore.WHITE}", end="\n")
        traceback.print_exc()
        print()

    else:
        print(f"{Fore.GREEN}[{now}]{Fore.WHITE} {s}", end=end)




global DIR
DIR = os.path.dirname(__file__)[:-5]

async def generic_embed(ctx: Context, title: str, *, desc: str = None, colour = 0xff0000, name = None):
    '''Sends a generic Discord embed.

    Comes with DaveedBot's logo as a thumbnail, colour setting (default red), and footer styling.

    Note
    ----
    Include await before calling the generic_embed method.
    
    Parameters
    ----------
    ctx : `Context`
        discord context object
    title : `str`
        Title of the embed.
    desc : `str`, optional
        Description of the embed.
    color : `int`, default 0xff0000 (red)
        Set colour of embed.
    name : `str`, default None
        Set the name of embed by the footer.
    '''
    if desc != None:
        em = discord.Embed(title = title,
                        description = desc + "\n ",
                        colour = colour)
    else:
        em = discord.Embed(title = title,
                        colour = colour)
    
    filepath = os.path.join(DIR,"cogs/Media/proto.png")
    fl = discord.File(filepath, filename = "proto.png")

    em.set_thumbnail(url = "attachment://{}".format("proto.png"))
    em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))
    
    if name != None:
        em.set_author(name = name)
    
    await ctx.send(embed = em, file = fl)

async def create_embed(intr: Intr, title: str, *, desc: str = None, colour = 0xff0000, name = None) -> tuple[discord.Embed, discord.File]:
    '''Sends a generic Discord embed.

    Comes with DaveedBot's logo as a thumbnail, colour setting (default red), and footer styling.

    Note
    ----
    Include await before calling the generic_embed method.
    
    Parameters
    ----------
    ctx : `Context`
        discord context object
    title : `str`
        Title of the embed.
    desc : `str`, optional
        Description of the embed.
    color : `int`, default 0xff0000 (red)
        Set colour of embed.
    name : `str`, default None
        Set the name of embed by the footer.
    '''
    if desc != None:
        em = discord.Embed(title = title,
                        description = desc + "\n ",
                        colour = colour)
    else:
        em = discord.Embed(title = title,
                        colour = colour)
    
    filepath = os.path.join(DIR,"cogs/Media/proto.png")
    fl = discord.File(filepath, filename = "proto.png")

    em.set_thumbnail(url = "attachment://{}".format("proto.png"))
    em.set_footer(text = "DaveedBot™ | {}".format(intr.user.name))
    
    if name != None:
        em.set_author(name = name)
    
    return em, fl




async def generic_error(ctx: Context, error: Exception = None):
    '''Sends a Discord embed, with the error text included.

    Parameters
    ----------
    ctx : `Context`
        discord context object
    error : `Exception`
        exception object. Will be used as a string
    '''
    face = ["TwT", ">w>", "<w<", ".w.", "-w-", "~w~", "XwX", "=w=", ";w;", "\_w\_", "\*w\*", "@w@", "QwQ", "qwq"]

    em = discord.Embed(title = "Oh no!",
                    description = "Something went wrong! {}\n\n`{}`".format(random.choice(face), error),
                    colour = 0xffff00)

    filepath = os.path.join(DIR,"cogs/Media/proto.png")
    fl = discord.File(filepath, filename = "proto.png")
            
    em.set_thumbnail(url = "attachment://{}".format("proto.png"))
    em.set_footer(text = "DaveedBot™ | {}".format(ctx.author))
    
    await ctx.send(embed = em, file = fl)



async def conv_member(ctxintr, string, to_name:bool = False):
    '''
    Attempts to convert String to Member object.

    Returns
    -------
    The original input if member conversion is unsuccessful;
    - The member is not found, or
    - Something that is not a string is passed.

    A discord.member.Member type object if member conversion is successful.

    
    '''
    
    try:
        converter = MemberConverter()
        member = await converter.convert(ctxintr, str(string))

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


async def scenify_(ctx: Context, target, texts: list, is_self: str=None, special_cases: list(tuple())=None) -> None:
    '''DEPRECIATED
    
    Displays a Discord embed.

    First checking for if user passed theirselves as the argument, then check if user passed some special case as the argument,
    and finally defaulting to a random selection from a list of responses.

    Note
    ----
    In all texts, use "{n}" in place of author, and "{t}" in place of target.
    
    Parameters
    ----------
    ctx : `Context`
        discord context object
    target
        The name that the user called when using an action command.
    texts : `list`
        list of texts, that one of which will be randomly selected if none of the other conditions is satisfied.
    is_self : `str`
        a singluar string that is displayed if the user calls the target to be themselves.
    special_cases : `list` of `tuples`, of `strs`.
        a list of tuples, where the first item in the tuple is the name that has to be inputted for the special case override the message, and the second item is the message that will be displayed instead.
    '''
    name = await conv_member(ctx, target, to_name=True)
    if is_self is not None:
        if name == ctx.author.mention or name == ctx.author.name:

            await generic_embed(ctx, title = is_self.replace("{n}", ctx.author.name).replace("{t}", name))
            return
    
    if special_cases is not None:
        for tups in special_cases:
            if target == tups[0]:
                await generic_embed(ctx, title = tups[1].replace("{n}", ctx.author.name).replace("{t}", name))
                return
    await generic_embed(ctx, title = texts[random.randint(0, len(texts)-1)].replace("{n}", ctx.author.name).replace("{t}", name))



async def generate_filepath(ctx: Context, target, name: str, ext: str) -> tuple[str]:
    '''Generates a filepath given a name, extention, and the local directory.

    Parameters
    ----------
    ctx : `Context`
        discord context object
    target
        The name that the user called when using an action command.
    name : `str`
        The intended file name.
    ext : `str`
        The file extension. (png, gif, et cetera)

    Returns
    -------
    `tuple` of `str`
        Where the index 0 is the full directory of the saved file,
        and the index 1 is just the file name and extension
    '''
    if target == None:
        target = ctx.author

    if target.name.isascii() and not " " in target.name:
        myfile = "{}_{}".format(name, target.name)
    else:
        myfile = "{}_{}".format(name, target.id)

    return os.path.join(DIR, f'cogs/Save/{name}/{myfile}.{ext}'), f"{myfile}.{ext}"



async def read_av(ctx: Context, target, size:int = 512, *, force_avatar:bool = False, force_square:bool = False, force_first_frame:bool = False):
    '''
    Attempts to read a client's attachment image, or if none exist, their Discord profile picture

    Parameters
    ----------
    ctx : `Context`
        discord context object
    target
        The name that the user called when using an action command.
    size : `int` (default 512)
        How many pixels the image will be resized to.
    force_avatar : `bool`, optional
        always ignore the user's attachments and instead take their avatar.
    force_square : `bool`, optional
        force the aspect ratio of the returned image to be 1:1 instead of maintaining aspect ratio given.
    force_first_frame : `bool`, optional
        force the first frame of a GIF to be taken.
    
    Returns
    -------
    PIL png, jpeg, or gif object.
        
    '''
        
    ALLOWED_TYPES = ["image/gif", "image/jpeg", "image/png"]

    if ctx.message.attachments and ctx.message.attachments[0].content_type in ALLOWED_TYPES and not force_avatar:
        if ctx.message.attachments[0].content_type == "image/gif":
            img = Image.open((requests.get(ctx.message.attachments[0].url, stream=True).raw))
            if force_first_frame: 
                img.seek(0) # First frame of GIF
            return img.resize((size, size)).convert("RGBA") if force_square else ImageOps.contain(img, (size, size)).convert("RGBA")

        else:
            img = Image.open((requests.get(ctx.message.attachments[0].url, stream=True).raw))
            return img.resize((size, size)) if force_square else ImageOps.contain(img, (size, size))

    # No attachments in message that are valid
    else:
        if not isinstance(target, discord.member.Member) or target is None:
            target = ctx.message.author
        
        img = Image.open(requests.get(target.avatar.url, stream=True).raw)
        return img.resize((size, size)) if force_square else ImageOps.contain(img, (size, size))


async def handle_guesses(ctx: Context, client: discord.client, name: str, correct_guesses: list[str], excluded_guesses: list[str] = None) -> None:
    '''
    Handles user messages input for guessing games in this bot.

    Parameters
    ----------
    ctx : `Context`
        discord context object
    client : `discord.client`
        discord context client
    name : `str`
        name of the guessing game
    correct_guesses : `list` of `str`
        tuple that contains all correct guesses for the generated guessable
    excluded_guesses : `list` of `str`, optional
        optionally guesses that are on blacklist from triggering a correct response
    '''
    def check(msg: discord.Message):
        return msg.channel.id == ctx.channel.id 

    if excluded_guesses is None: excluded_guesses = []

    for _ in range(64): # time out after 64 messages
        message: discord.Message = await client.wait_for("message", check = check)
        msg = message.content.lower()
        if msg in correct_guesses and msg not in excluded_guesses:

            await generic_embed(ctx, title = f"Correct! {correct_guesses[0].title()}", desc = f"{message.author.name} got it!")

            with open(f"cogs/Leaderboards/{name}.json", "r") as fl:
                lb_file = json.load(fl)

            user_key = str(message.author.id)
            user_name = str(await conv_member(ctx, message.author.id))

            if not user_key in lb_file:
                lb_file[user_key] = [0, user_name, []] # Create instance of user score if it does not exist

            lb_file[user_key][1] = user_name
            lb_file[user_key][0] += 1 # alltime_points

            alltime_seen = lb_file[user_key][2]
            if correct_guesses[0] not in alltime_seen:
                alltime_seen.append(correct_guesses[0])
            
            with open(f"cogs/Leaderboards/{name}.json", "w") as fl:
                json.dump(lb_file, fl)
            break

        elif msg == "d!idk":
            await generic_embed(ctx, title = f"It's ||{correct_guesses[0].title()}!||")
            break
        elif msg == "d!hint":
            await generic_embed(ctx, title = f"It starts with the letter '{correct_guesses[0][0]}'")
        elif msg == "d!len":
            await generic_embed(ctx, title = f"It's name is {len(correct_guesses[0])} letters long")
        elif msg == f"d!{name}":
            # New instance of command called
            break
        else:
            correct = correct_guesses[0]
            if abs(len(correct) - len(msg)) <= 1:
                wrong = 0
                for i in range(min(len(correct), len(msg))):
                    if correct[i] != msg[i]: wrong += 1

                if wrong <= 1:
                    await ctx.send(f"{message.author} CLOSE!")




async def display_leaderboard(ctx: Context, name: str):
    '''Displays a Discord Embed.

    Loads the appropriate leaderboard from a JSON file, and then shows the ten highest rated players.
    Highlights the user's name. If user's name isn't present, append their name after the top ten.

    Note
    ----
    `name` should also be the name of the command, and also the name of the leaderboard record's file.

    Parameters
    ----------
    ctx : `Context`
        discord context object
    name : `str`
        Name of the leaderboard.
    '''
    with open(f"cogs/Leaderboards/{name}.json", "r") as fl: lb_mon = json.load(fl)
    not_top_ten = True
    top_users = {k: v for k, v in sorted(lb_mon.items(), key=lambda item: item[1], reverse=True)}

    desc = f"Name **|** All-time {name.title()}s Guessed **|** Unique {name.title()}s Guessed\n"
    for pos, user in enumerate(top_users):
        if pos == 10: break
            
        if pos == 0: desc +=   ":first_place: "
        elif pos == 1: desc += ":second_place: "
        elif pos == 2: desc += ":third_place: "
        else: desc += ":military_medal: "

        if user == str(ctx.author.id): 
            desc += "__"
            not_top_ten = False

        desc += f'{pos+1}. **{top_users[user][1][:-5]}**{top_users[user][1][-5:]} | `{top_users[user][0]}` | `{len(top_users[user][2])}`'

        desc += "__ :arrow_left:\n" if user == str(ctx.author.id) else "\n"


    if not_top_ten:
        desc += "...\n"

        for pos, user in enumerate(top_users):
            if user == str(ctx.author.id):
                desc += f'__{pos+1}. **{top_users[user][1][:-5]}**{top_users[user][1][-5:]} | `{top_users[user][0]}` | `{len(top_users[user][2])}`__ :arrow_left:'
                break
            
        else:
            desc += f'__∞. **{str(ctx.author)[:-5]}**{str(ctx.author)[-5:]} | `0` | `0`__ :arrow_left:\n'
            desc += f"You haven't played any games yet!"

    await generic_embed(ctx, title = f"{name.title()} Leaderboards", desc = desc)
