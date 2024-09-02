import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True
count = 0
path = r"path to your datapack file"
filepath = path + "pack.mcmeta"
bot = commands.Bot(command_prefix="$", intents=intents)

@commands.command()
async def give(ctx, arg):
    '''
    : give the item enter in parameter in game
    '''
    global count
    print("give executed")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("{\"pack\":{\"description\":\"⫽{fonction:event1,parameter: "+str(arg)+",count:"+str(count)+"}⫻\",\"pack_format\":8}}")
    count += 1
    await ctx.send(f'{ctx.author.mention} has used the give command!')
    
@commands.command()
async def summon(ctx, arg):
    '''
    : summon a entity in a range of 10 block around every player
    '''
    global count
    print("summon executed")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("{\"pack\":{\"description\":\"⫽{fonction:event2,parameter: "+str(arg)+",count:"+str(count)+"}⫻\",\"pack_format\":8}}")
    count += 1
    await ctx.send(f'{ctx.author.mention} has used the summon command!')

@commands.command()
async def batman(ctx):
    '''
    : summon a entity in a range of 10 block around every player
    '''
    global count
    print("batman executed")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("{\"pack\":{\"description\":\"⫽{fonction:event3,parameter: "+str(' none')+",count:"+str(count)+"}⫻\",\"pack_format\":8}}")
    count += 1
    await ctx.send(f'{ctx.author.mention} has used the batman command!')

@commands.command()
async def mlg(ctx, arg):
    '''
    : summon a entity in a range of 10 block around every player
    '''
    global count
    print("batman executed")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("{\"pack\":{\"description\":\"⫽{fonction:event4,parameter: "+str(arg)+",count:"+str(count)+"}⫻\",\"pack_format\":8}}")
    count += 1
    await ctx.send(f'{ctx.author.mention} has used the mlg command!')
    
@commands.command()
async def getfucked(ctx, arg = 'dirt'):
    '''
    : summon a entity in a range of 10 block around every player
    '''
    global count
    print("getfucked executed")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("{\"pack\":{\"description\":\"⫽{fonction:event5,parameter: "+str(arg)+",count:"+str(count)+"}⫻\",\"pack_format\":8}}")
    count += 1
    await ctx.send(f'{ctx.author.mention} has used the mlg command!')


bot.add_command(give)
bot.add_command(summon)
bot.add_command(batman)
bot.add_command(mlg)
bot.add_command(getfucked)


bot.run('discord bot token')

