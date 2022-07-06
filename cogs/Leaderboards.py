from turtle import pos
from util.BotUtils import Utils
from util.BotUtils import nextcord
import nextcord
from nextcord.ext import commands
from util.ListUtils import POKEMON, COUNTRIES
import random
import json

class Leaderboards(commands.Cog):
    def __init__(self, client):
        self.client = client


       


    @commands.command(aliases = ["lb", "leaderboards"])
    async def leaderboard(self, ctx, lb):
        
        # TODO wip.

        if lb == "mon":
            with open("cogs\\Leaderboards\\mon.json", "r") as fl:
                lb_mon = json.load(fl)

            top_users = {k: v for k, v in sorted(lb_mon.items(), key=lambda item: item[1], reverse=True)}
            print(top_users)

            desc = "__Name | All-time Mons Guessed | Unique Mons Guessed__\n"
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

            await Utils.generic_embed(ctx, title = "Mon Leaderboards", desc = desc)






        elif lb == "flag":
            with open("cogs\\Leaderboards\\flag.json", "r") as fl:
                lb_flag = json.load(fl)

            top_users = {k: v for k, v in sorted(lb_flag.items(), key=lambda item: item[1], reverse=True)}
            print(top_users)

            desc = "__Name | All-time Flags Guessed | Unique Flags Guessed__\n"
            for pos, user in enumerate(top_users):
                if pos == 10: # top 10 scores
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

            await Utils.generic_embed(ctx, title = "Flag Leaderboards", desc = desc)

        else:
            await Utils.generic_error(ctx, f"'{lb}' is not a valid leaderboard.")


def setup(client):
    client.add_cog(Leaderboards(client))