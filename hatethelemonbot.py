import random
import asyncio
import time
import json
import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='/')
client.remove_command('help')

def read_token():
    with open("bottoken.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

@client.event
async def on_ready():
    activity = discord.Game(name="/help  for commands")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print ('bot is ready')

token = read_token()
#def stfu_counter():
 #   await client.wait_until_ready()
  #  global messages

  #  while not client.is_closed():
@client.command()
async def clear(ctx, amount=1):
    if amount >= 51:
        await ctx.channel.send("This is too much. Limit is 50 messages")
    else:
        await ctx.channel.purge(limit=amount+1)

client.counter = 0
stfu_count = "stfucounter.json"

@client.command()
async def stfupic(message):
    image = random.randint(1, 3)
    if image == 1:
        await message.channel.send("https://imgur.com/5HcNa1Y")
    if image == 2:
        await message.channel.send("https://imgur.com/UaVHXQt")
    if image == 3:
        await message.channel.send("https://imgur.com/a/glPkCqm")

@client.command()
async def stfu(message):
    beNice = random.randint(1, 500)
    if beNice != 420:
        await message.channel.send("Shut the fuck up Ieman")
    else:
        await message.channel.send("Maybe we don't need to tell Ieman to "
                                   "shut up. He has done a lot of things, like "
                                   "his music, his own bot, and gathered many people "
                                   "together to this very server. If anything, he "
                                   "deserves to be praised for his accomplishments")

@client.command()
async def cmd(message):
    await message.channel.send("This command changed to /help")

@client.command()
async def copey(message):
    await message.channel.send("Ang stop that and shut the fuck up you sexy little cunt")
    #await message.channel.send("Ang stop that and shut the fuck up you unsexy little cunt")

@client.command()
async def test(message):
    await message.channel.send("Bot is working")

#@client.command()
#async def kelp(ctx):
#    helpMenu = discord.Embed(
#        colour=discord.Colour.orange()
#    )
#    helpMenu.set_author(name='Help')
#    helpMenu.add_field(name='/stfu', value='Tells Ieman to stfu')
#    await ctx.message.channel(embed=helpMenu)

@client.command()
async def help(ctx, args='normal'):
    if args == 'normal':
        await ctx.channel.send("Use '/' as the prefix for these commands\n\n"
                                   "`stfu` - Tell Ieman to stfu\n"
                                   "`weak` - Insult Ieman's strength\n"
                                   "`simp` - Call Ieman a simp\n"
                                   "`cry` - Lets Ieman cry\n"
                                    "`stfupic` - An anime girl tells Ieman to stfu\n\n"
                                   "Extra commands: (use /help [`command`])\n"
                               "`utility`\n`kill`")
    elif args == 'utility':
        await ctx.channel.send("clear - purge messages (limited to 50)")
    elif args == 'kill':
        await ctx.channel.send("The kill feature tells Ieman to shut up every time he says something\n\n"
                                    "killon - Turns on the kill feature\n"
                                    "killoff - Turns off the kill feature")


@client.command()
async def weak(message):
    weakInsult = random.randint(1,3)
    if weakInsult == 1:
        await message.channel.send("lmao you weak af Ieman")
    elif weakInsult == 2:
        await message.channel.send("Ieman you weak ass pussy")
    elif weakInsult == 3:
        await message.channel.send("Look at you, Ieman. Weak boy")


@client.command()
async def killon(message):
    client.counter = 1
    await message.channel.send("The kill feature is now on. No mercy, Ieman")

@client.command()
async def killoff(message):
    client.counter = 0
    await message.channel.send("The kill feature is now off. Maybe peace was an option")

@client.command()
async def cry(message):
    await message.channel.send("https://imgur.com/RcGjuUY")

@client.command()
async def simp(ctx, args=''):
    simpInsult = random.randint(1,200)
    if args=='longshlong':
        await ctx.channel.purge(limit=1)
        await ctx.channel.send('This command code has been disabled')
        simpInsult=99.5
    if simpInsult >= 101:
        await ctx.channel.send("Haha Ieman is a simp")
    elif simpInsult <= 99:
        await ctx.channel.send("Ieman simps for all girls fuckin simp")
    elif simpInsult == 100:
        await ctx.channel.send("Ieman simps for Ang no cap")


@client.event
async def on_message(message):
    if client.counter == 1:
        dumb_lemon: List[str] = ["hateomen#8692"] # slav#8325 hateomen#8692
        if str(message.author) in dumb_lemon:
            await message.channel.send("shut the fuck up Ieman")
    await client.process_commands(message)

client.run(token)



