import discord
from discord.ext import commands
import asyncio
import random
import os

prefix = "-"

client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)
token = (os.environ['TOKEN'])

@client.event
async def on_ready():
    activity = discord.Game(name="", type=4)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    

print('''THANKS FOR USING THIS SELF BOT IS READY USE -help TO KNOW ALL COMMANDS 

selfbot is ready!
''')

@client.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send(f"""
**Lista de Comandos:**
**{prefix}help** - Ajuda comandos!
**{prefix}start** - Inicia o bot!
**{prefix}stop** - Para o bot!
**{prefix}evtrain** - Ajuda a treina Ev's
""")
  
@client.command()
async def start(ctx, route: int, move: int):

    if not 1 <= int(route) <= 25:
      async def on_command_error(ctx, error):
        await ctx.send('Selecione a route de 1 a 25!', delete_after=3)
        await ctx.send(f'Usar: {prefix}start route move', delete_after=10)
        return

    if not 1 <= int(move) <= 4:
        await ctx.send('Selecione o atack de 1 a 4!', delete_after=3)
        await ctx.send(f'Usar: {prefix}start route move', delete_after=10)
        return
    await ctx.send('Successfully enabled Auto Myuu Grinder!')
    global dmcs
    dmcs = True
    while dmcs:
        await ctx.send(f'.route {route}')
        await asyncio.sleep(3)
        await ctx.send(move)
        await asyncio.sleep(1.5)


@client.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Desativado com sucesso, Auto Farm Myuu! | by **vinikkz**')
	global dmcs
	dmcs = False 

@client.command()
async def eggsecretvini(ctx):
    await ctx.message.delete()
    await ctx.send('Successfully Enabled Auto Myuu')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():

            await asyncio.sleep(4)
            await ctx.send('.get egg')
            await asyncio.sleep(4)
            await ctx.send('.mypkinfo gastly')
            await asyncio.sleep(4)
            await ctx.send('.boxswap 2 gastly')
            await asyncio.sleep(1800)

@client.command()
async def evtrain(ctx):
	await ctx.message.delete()
	await ctx.send("""
**
OS ITENS USADOS PARA TREINO DE EV **
** OS ITENS PARA BAIXAR EV**
**->** Pomeg Berry (-10 HP EVs)
**->** Kelpsy Berry (-10 Attack EVs)
**->** Qualot Berry (-10 Defense EVs)
**->** Hondew Berry (-10 Special Attack EVs)
**->** Grepa Berry (-10 Special Defense EVs)
**->** Tamato Berry (-10 Speed EVs)
**OS ITENS PARA MÁXIMO EV A PARTIR DE 0**
**->** Power weight +8 HP ev
**->** Power belt +8 def ev 
**->** Power bracer +8 atk ev 
**->** Power anklet +8 spe ev 
**->** Power band +8 spd ev 
**->** Power lens +8 spa ev
  """)

client.run(token, bot=False)
