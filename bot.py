import discord
import os
from discord.ext import commands
import json
import asyncio
import random

lient = commands.Bot(command_prefix="*")
client.remove_command('help')

@client.event
async def on_ready():
	print('Logged in', client.user.name)
	print('Version - 1.0.0')
	print('Creator - PrabaRock7#3945')
	print('Release Version - v01')
	print('ᎷᎨᏝᎾ')
	await client.change_presence(status=discord.Status.online, activity=discord.Game(name="*help | MiloBot™"))

@client.event
async def on_member_join(member):
	print(f"{member} has joined the server.")
	
@client.event
async def on_member_remove(member):
	print(f"{member} has left the server.")
	
@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")
	
@client.command()
async def help(ctx):
	
	embed = discord.Embed(title="List Of Commands", colour=discord.Colour(0xff0000))	
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	embed.set_footer(text=f"Command Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
	
	embed.add_field(name="**Fun**", value="*hello, *ping")
	embed.add_field(name="**Bot Related Commands**", value="*botinfo, *botsource,  *botsupportserver")
	embed.add_field(name="**Mathematics**", value="*square, *bitcoin")
	embed.add_field(name="**Moderation**", value="*clear, *kick, *ban, *unban, *avatar, *useravatar")
	await ctx.send(embed=embed)
	
@client.command()
async def hello(ctx):
	await ctx.send("Hello!" + ", " + ctx.message.author.mention)
	
@client.command()
async def ping(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=ctx.message.created_at)
	embed.set_author(name="Ping")
	embed.add_field(name=f"*Pong*", value=f"**:ping_pong: {round(client.latency * 1000)}ms**")
	embed.set_footer(text=f"Req By {ctx.author}", icon_url=ctx.author.avatar_url)
	await ctx.send(embed=embed)
	
@client.command()
async def botinfo(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ffff), description="Milo Bot info")
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	
	embed.add_field(name="Bot Info", value=f"Hello {ctx.author}, thanks for showing intrest to get info about me :grin:. Im Coded using Python. For list of commnads please type -help. My Owner is <@589647651939549206>. Im a simple bot i don't have advanced commands, that's a fault.")
	embed.add_field(name="External Links", value="[Patreon](https://patreon.com/PrabaRock7), [Ko-Fi](https://ko-fi.com/prabarock7)")
	await ctx.send(embed=embed)
	
@client.command()
async def botsupportserver(ctx):
	
	embed = discord.Embed(title="Support server")
	embed.add_field(name="Server Link", value="Touch the below link to join the server")
	await ctx.send(content="https://discord.gg/FeD6RUs", embed=embed)
	
@client.command()
async def avatar(ctx):
	show_avatar = discord.Embed(
	
	         color = discord.Color.blue()
	)
	show_avatar.set_image(url="{}".format(ctx.author.avatar_url))
	await ctx.send(embed=show_avatar)
	
@client.command()
async def useravatar(ctx, member : discord.Member):
	show_avatar = discord.Embed(
	
	         color = discord.Color.dark_blue()
	)
	show_avatar.set_image(url="{}".format(member.avatar_url))
	await ctx.send(embed=show_avatar)
	
@useravatar.error
async def useravatar_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Please specify a **member** to show his/her *avatar* {ctx.author.mention}")

@client.command()
async def botsource(ctx):
	await ctx.send("https://github.com/PrabaRock/Milo-Bot")
	
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
  
client.run(os.getenv("TOKEN"))
