import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio
import sys
import os
import asyncpg

intents = discord.Intents().all()
client = commands.Bot(command_prefix=".", intents=intents, help_command=None, case_insensitive=True)
guild = discord.Guild



def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@client.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Follow @Pinkyhax on Instagram! | Type .h for Help! Hail Legend Pinkyhax"))


@client.command()
@has_permissions(administrator=True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)



@client.command()
@has_permissions(administrator=True)
async def restart(ctx):
    message = await ctx.send("Restarting... Allow up to 5 seconds")
    await ctx.message.delete()
    restart_program()

@client.command()
@has_permissions(administrator=True)
async def msg(ctx, *, args = None):
    await client.wait_until_ready()
    if args == None:
        message_content = "Please wait, we will be with you shortly!"
    
    else:
        message_content = "".join(args)

        em = discord.Embed(title="Pinkys Support Bot", description="{}".format(message_content))
        await ctx.send(embed=em)
        await ctx.message.delete()


    
client.run("ODA0NzQ4NjgyNTczNTEyNzM1.YBQ2nQ.YayPPdJqeYzwZ-ZeZNQkdJNxlFQ")