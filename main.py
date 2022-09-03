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
async def start(ctx):
	await ctx.message.delete()
	await ctx.send('Ativado com sucesso, Auto Farm Myuu! | by **vinikkz**')
	global dmcs
	dmcs = True
	while dmcs:
			await ctx.send('.route 24')
			await asyncio.sleep(3)
			await ctx.send(random.randint(1,4))
			await asyncio.sleep(1.5)

@client.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Desativado com sucesso, Auto Farm Myuu! | by **vinikkz**')
	global dmcs
	dmcs = False 

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
