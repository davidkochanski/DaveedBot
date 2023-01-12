import discord
from discord import app_commands
from discord import Interaction as Intr
from discord.ext import commands
from discord.ext.commands import Context
from util.BotUtils import generic_embed, conv_member, scenify_, create_embed, printl
import random
import json
from discord import ui

class Actions2(commands.Cog):
    def __init__(self, client):
        self.client = client


    async def scenify(self, intr: Intr, cmd: str, target) -> tuple[discord.Embed, discord.File]:
        with open(f"cogs/Media/Actions.json", "r") as fl:
            actions = json.load(fl)

        ctx = await self.client.get_context(intr)
        
        target = await conv_member(ctx, target, to_name=True)

        if actions[cmd]["is_self"] != "":
            if target == intr.user.mention or target == intr.user.name:

                return await create_embed(intr, title = actions[cmd]["is_self"].replace("{n}", intr.user.name).replace("{t}", target))
        
        if actions[cmd]["special_cases"] != []:
            for tups in actions[cmd]["special_cases"]:
                if target == tups[0]:
                    return await create_embed(intr, title = tups[1].replace("{n}", intr.user.name).replace("{t}", target))

        return await create_embed(intr, title = actions[cmd]["texts"][random.randint(0, len(actions[cmd]["texts"])-1)].replace("{n}", intr.user.name).replace("{t}", target))


    actions = ["tf", "boop", "nuzzle", "hug", "vore", "yiff", "stomp", "kiss"]

    @app_commands.command(name="actionadd", description="Add a prompt to on action command (boop, hug, etc.)")
    @app_commands.choices(command = [app_commands.Choice(name=element, value=element) for element in actions])
    @app_commands.describe(message = "Use {n} for the user, {t} for the target.")
    async def actionadd(self, intr: Intr, command: str, message: str): 
        if "{n}" not in message:
            await intr.response.send_message("Your message string does not contain `{n}`!")

        elif "{t}" not in message:
            await intr.response.send_message("Your message string does not contain `{t}`!")
        
        elif len(message) > 200:
            await intr.response.send_message("Messages be at most 200 characters long.")

        else:
            with open(f"cogs/Media/Actions.json", "r") as fl:
                action_dict = json.load(fl)

            action_dict[command]["texts"].extend([message])

            if len(action_dict[command]['texts']) >= 25:
                await intr.response.send_message("Max amount of responses for this command has been reached.")
                return

            with open(f"cogs/Media/Actions.json", "w") as fl:
                json.dump(action_dict, fl)
                await intr.response.send_message(f"Successfully added your prompt `{message}` to `/{command}`!")

                printl(f"{intr.user.name} added '{message}' to /{command}.")



    @app_commands.command(name="actionrm", description="Remove a prompt to on action command (boop, hug, etc.)")
    @app_commands.choices(command = [app_commands.Choice(name=element, value=element) for element in actions])
    async def actionrm(self, intr: Intr, command: str): 
        with open(f"cogs/Media/Actions.json", "r") as fl:
            action_dict = json.load(fl)


        select = ui.Select(placeholder = f"Select which message from {command}",
                            options=[discord.SelectOption(label=prompt, value=idx) if len(prompt) < 100 else discord.SelectOption(label=prompt[0:97]+"...", value=idx) for idx, prompt in enumerate(action_dict[command]["texts"])],
                            max_values=1,
                            min_values=1
        )


        async def select_callback(callback_intr: Intr):
            if callback_intr.user.id != intr.user.id:
                await callback_intr.response.send_message("Not you!", ephemeral=True)
                return

            removed = action_dict[command]["texts"].pop(int(select.values[0]))

            with open(f"cogs/Media/Actions.json", "w") as fl:
                json.dump(action_dict, fl)

            printl(f"{intr.user.name} removed '{removed}' from /{command}.")

            await callback_intr.response.edit_message(content=f"Done. *Mistake? Just use /actionadd to add it back*", view=None)
            await callback_intr.followup.send(content=f"Successfully removed `{removed}` prompt from `/{command}`.")

        select.callback = select_callback

        vw = ui.View()
        vw.add_item(select)
        await intr.response.send_message(view=vw)
        
            


        

    @app_commands.command(name="tf", description="Transform someone into anything you want!")
    async def tf(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "tf", target)
        await intr.response.send_message(embed=em, file=fl)


    @app_commands.command(name="boop", description="BOOP!")
    async def boop(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        BOOP!
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "boop", target)
        await intr.response.send_message(embed=em, file=fl)


    @app_commands.command(name="nuzzle", description="Nuzzle anyone you want! You might need a PARLYZHEAL afterwards..")
    async def nuzzle(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Nuzzle anyone you want!
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "nuzzle", target)
        await intr.response.send_message(embed=em, file=fl)


    @app_commands.command(name="hug", description="Hug someone tightly!")
    async def hug(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Hug someone tightly!
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "hug", target)
        await intr.response.send_message(embed=em, file=fl)

    
    @app_commands.command(name="vore", description="Vore someone- wait what happens if you vore yourself?")
    async def vore(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Vore someone~ wait what happens if you vore yourself?
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "vore", target)
        await intr.response.send_message(embed=em, file=fl)


    @app_commands.command(name="yiff", description="Yiff someone.")
    async def yiff(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Yiff someone.
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "yiff", target)
        await intr.response.send_message(embed=em, file=fl)

    
    @app_commands.command(name="stomp", description="stomp")
    async def stomp(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Stomp on someone.
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "stomp", target)
        await intr.response.send_message(embed=em, file=fl)

    # paralyze heal


    @app_commands.command(name="kiss", description="Kiss someone!")
    async def kiss(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Kiss someone!
        '''
        target = target if target is not None else intr.user.name
        em, fl = await self.scenify(intr, "kiss", target)
        await intr.response.send_message(embed=em, file=fl)

    @app_commands.command(name="target", description="Inflate someone. Use at your own risk")
    async def inflate(self, intr: Intr, target: str = None):
        '''
        Optional argument: `target`

        Inflate someone. Use at your own risk
        '''
        target = target if target is not None else intr.user.name
        em, fl = await create_embed(intr, title=f"{intr.user.name} inflates {target}, making them big and round! \nhttps://www.youtube.com/watch?v=NP-UxkYeLV0")
        await intr.response.send_message(embed=em, file=fl)




async def setup(client):
    await client.add_cog(Actions2(client))