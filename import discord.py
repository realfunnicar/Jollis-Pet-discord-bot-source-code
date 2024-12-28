import discord
import time
import random
import asyncio
from discord.ext import commands

## TO DO
## make my own hi message for the bot
## make the aboutthecoder output a bit longer ✔️

## note to self: restart vs code if it says a message twice



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def slurspam(ctx: commands.Context, number_of_messages: int):
    for i in range(number_of_messages):
        choices = ('nigger', 'nigga', 'fuck', 'shit', 'cock', 'ass', 'whore', 'slut', 'bitch', 'penis', 'dick', 'asshole', 'motherfucker')
        await ctx.send(random.choice(choices))

@bot.command()
async def spam(ctx: commands.Context, number_of_messages: int):
    for i in range(number_of_messages):
        await ctx.send("SPAMMMM")

@bot.command()
async def diceroll(ctx: commands.Context, number_of_sides: int):
    result = random.randint(1, number_of_sides)
    await ctx.send(f"you rolled {result} on a dice with {number_of_sides} sides, damn")

@bot.command()
async def annoy(ctx: commands.Context, member: discord.Member, inputu: str, number_of_messages: int):
    dm_channel = await member.create_dm()
    if number_of_messages == 1:
        await ctx.send(f"dming <@{member.id}> {number_of_messages} time")
    elif number_of_messages != 1:
        await ctx.send(f"dming <@{member.id}> {number_of_messages} times")
    for i in range(number_of_messages):
        await dm_channel.send(inputu)

@bot.command()
async def cmds(ctx: commands.Context):
    await ctx.send("slurspam: spams random slurs or swears, commandamount: tells you how many commands there are, credits: the credits silly, abandonedideas: tells you some abandoned ideas. theres nothing abandoned yet so its pretty useless rn, newestcmd: tells you the newest command, coderaddress: gives you walter white's address, esex: esex, version: pretty self explanatory, whoisthebotsgod: pings me, consume: makes kirby inhale you, sitefinder: sends name.com, linuxmint: sends the linux mint website, ltg: tells you to kys, cmds: shows this list, top3scariestjumpscares: sends some jumpscare links, annoy: dms a person a phrase as many times as you want, diceroll: rolls a dice with as many sides as you want, ping: mentions how unfunny pong is when its after !ping and shows you the bot latency")

@bot.command()
async def ltg(ctx: commands.Context):
    await ctx.send("||you should kill yourself, NOW. and give someone else a bit of this ozone layer thats trapped in this blue trash bubble so we can breathe.||")

@bot.command()
async def newestcmd(ctx: commands.Context):
    await ctx.send("the newest command is slurspam")

@bot.command()
async def commandamount(ctx: commands.Context):
    await ctx.send("there are 18 commands")

@bot.command()
async def aboutthecoder(ctx: commands.Context):
    await ctx.send("the coder is some silly autistic guy who one day had the idea to code and it was the 27th of december 2024 aedt when i spawned please help me he is probably actively coding me as we speak and uhhh *cough cough cough* yeah thats prett- COUGH COUGH -y much it")

@bot.command()
async def pinf(ctx: commands.Context):
    await ctx.send("hahahaha you spelt ping wrong loser!!!!")

@bot.command()
async def credits(ctx: commands.Context):
    await ctx.send("thanks to tophgif for giving me some ideas and actually helping me with half of this code, especially the annoy command that one was the hardest. he also helped me fix some bugs. my work for today is done -funni/nu yearz car, 11:23 PM 27/12/24 AEDT")

@bot.command()
async def esex(ctx: commands.Context):
    await ctx.send("deeper daddy or whatever i havent experienced it and the coder hasnt")
    asyncio.sleep(2.5)
    await ctx.send("hes a bit of an introvert in real life, he should speak to people ngl")

@bot.command()
async def gayorstraight(ctx: commands.Context):
    await ctx.send("im canonically straight according to the official code which is happening right here right now, and the guys who created me are both straight")

@bot.command()
async def sitefinder(ctx: commands.Context):
    await ctx.send("https://name.com")

@bot.command()
async def coderaddress(ctx: commands.Context):
    await ctx.send("308 Negra Arroyo Lane, Albuquerque, New Mexico 87104")

@bot.command()
async def waltuh(ctx: commands.Context):
    await ctx.send("waltuh")

@bot.command()
async def abandonedideas(ctx: commands.Context):
    await ctx.send("there havent been any abandoned ideas... YET")

@bot.command()
async def version(ctx: commands.Context):
    await ctx.send("version 1.10.1")

@bot.command()
async def whoisthebotsgod(ctx: commands.Context):
    await ctx.send("<@1176029438153064518>")

@bot.command()
async def consume(ctx: commands.Context):
    await ctx.send("*kirby inhale sound*")

@bot.command()
async def top3scariestjumpscares(ctx: commands.Context):
    await ctx.send("1: https://www.youtube.com/watch?v=OLpqB59vV0M, 2: https://only-fans.uk/ryanstoyreview, 3: https://tenor.com/view/congregation-jumpscare-gif-15004478797119541730")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"pong hahahaha!!! ok this is unfunny, anyways {bot.latency}")

@bot.command()
async def linuxmint(ctx: commands.Context):
    await ctx.send("https://linuxmint.com")


bot.run("your bots token")