from util.BotUtils import Utils
from nextcord.ext import commands

class Actions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    async def tf(self, ctx, *, target):
        '''
        Optional argument: `target`

        Transform someone into anything you want!
        '''
        await Utils.scenify(ctx, target,["{n} transforms into {t}! They seem to love their new form~ uwu",
                                        "{n} screeches in pain, before slowly transforming into {t} o.O",
                                        "{n} drinks a mystical potion, and then transformes into {t}! OwO",
                                        "{n} collides with some funky goo, transforming them into {t}! O.O",
                                        "{n} gets a glowing fluid injected into them, and then they transformed into {t}!! OwO",
                                        "{n} steps through a magical ring, which transforms them into {t}! OwO"],
                                            
                                        "You're already {n}, dummy!",

                                        [("Puro", "{n} tfs into Puro. Oh dear lord.")])

    @commands.command()
    async def boop(self, ctx, *, target):
        '''
        Optional argument: `target`

        BOOP!
        '''
        await Utils.scenify(ctx, target,["{n} boops {t} right on the snoot! UwU",
                                        "{n} tried to boop {t}, but instead {t} booped them first! OwO",
                                        "{n}  booped {t}, and {t} booped them right back! ^w^"],

                                        "{n} boops themselves. This event causes a nuclear reaction equivilant to the power of 621 megatons of TNT. Over 800m people were instantly killed in the Boop Disaster. All is lost. All because {n} wanted to boop themselves.")

    @commands.command()
    async def nuzzle(self, ctx, *, target):
        '''
        Optional argument: `target`

        Nuzzle anyone you want!
        '''
        await Utils.scenify(ctx, target,["{n} nuzzles {t}! It does 20 base damage, and paralyzes them! owO"],
        
                                        "{n} nuzzles themselves! It does 20 base damage, and paralyzes themself! owO")

    @commands.command()
    async def hug(self, ctx, *, target):
        '''
        Optional argument: `target`

        Hug someone tightly!
        '''
        await Utils.scenify(ctx, target,["{n} hugs {t} tightly! UwU~",
                                        "{n} hugs {t}, whispering \"I love you so much, {t}\" ^w^",
                                        "{n} quietly wraps their arms around {t} OuO",
                                        "{n} wraps their arms tight around {t}, smushing them in love and appreciation :3",
                                        "Before {n} even finished opening their arms, {t} jumps into {n}'s loving arms!"],

                                        "{n} hugs themselves! They look kind of lonely...")
    
    @commands.command(hidden=True)
    async def vore(self, ctx, *, target):
        '''
        Optional argument: `target`

        Vore someone~ wait what happens if you vore yourself?
        '''
        await Utils.scenify(ctx, target,["{n} vores {t} cutely! Yum :yum:",
                                        "{n} vores {t} aggressively! ÒwÓ~",
                                        "{n} opens their maw as much as they can, and then devoures {t} in one bite!",
                                        "{n} throws {t} into their maw, eating them! O.O"],

                                        "{n} vores themselves. They disappear into nothing o.O")

    @commands.command(hidden=True)
    async def yiff(self, ctx, *, target):
        '''
        Optional argument: `target`

        Yiff someone.
        '''
        await Utils.scenify(ctx, target,["{n} yiffs {t}! o.O"],
                                        
                                        "{n} yiffs... themselves? wh- how?")
    
    @commands.command(hidden=True)
    async def stomp(self, ctx, *, target):
        '''
        Optional argument: `target`

        Stomp on someone.
        '''
        await Utils.scenify(ctx, target,["{n} stomps {t} into the ground! UwU",
                                        "The macro {n} stomps the micro {t} into the ground! owo",
                                        "The huge {n} lifts their paw up into the sky above tiny {t}, before stomping their pawb/hoof/talon/peet/other straight into {t}~",
                                        "{n} stepped on {t} without even noticing! {t} doesn't seem to mind though X3",
                                        "{t} looks up at {n}'s massive, squishy, adorable pawbs/hooves/talons/peets/other, which are accelerating directly at them~. {n} feels {t} in between their toes as they stepped on {t}~",
                                        "{n} rapidly stomps {t} dozens of times! O>O",
                                        "{n} shoves their pawbs/hooves/talons/peets/other down {t}'s throat!"],

                                        "{n} tried to stomp themself, but instead created a black hole that devoured the observable universe. Oops!")

    @commands.command()
    async def inflate(self, ctx, *, target):
        '''
        Optional argument: `target`

        Inflate someone. Use at your own risk
        '''
        await Utils.scenify(ctx, target,["{n} inflates {t}, making them big and round! \nhttps://youtu.be/NP-UxkYeLV0"],

                                        "{n} inflates themselves!! I knew carring that pump everywhere everyday would be worth it! \nhttps://youtu.be/NP-UxkYeLV0")


    @commands.command(hidden=True)
    async def kiss(self, ctx, *, target):
        '''
        Optional argument: `target`

        Kiss someone!
        '''
        await Utils.scenify(ctx, target,["{n} grabs {t} close, and kisses them right on the snoot! UwU",
                                        "{n} gives {t} a little kiss! cuties~",
                                        "{n} tightly hugs {t}, before kissing them~ >///<"],

                                        "{n} kisses themselves! Self love is important after all OuO:+1:")


def setup(client):
    client.add_cog(Actions(client))