import discord
import os
import datetime
from discord.ext import commands

client = commands.Bot(command_prefix="!")

with open("config.yml") as file:
	TOKEN = file.read()

@client.event
async def on_ready():
	print("Hey, yo ! I'm ready :p")

@client.command()
async def ping(ctx):
	await ctx.channel.send(":ping_pong: pong ! ({}ms)".format(round(client.latency * 1000)))

client.run(TOKEN)