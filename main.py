#rip embed
import discord
import json
import random
import time
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
import os
import requests
import string

configFile = {"isGrinding": False,"isTeamChecking": False,"currentRouteGrinding": None,"currentMoveRunning": None}

try:
    if os.stat("config.json").st_size == 0:
        with open("config.json", "w") as f:
            json.dump(configFile, f, indent=2)
        print("Successfully Write the config!")
except:
    with open("config.json", "a+") as f:
        json.dump(configFile, f, indent=2)
    print("Successfully Write the config!")

with open("config.json", "r") as f:
    config = json.load(f)

def setItem(keyName, keyValue):
  global config
  global f
  try:
    config[keyName] = keyValue
    with open(json_file, 'w') as json_file:
      json.dump(config, f, indent=2)
  except:
    print(Fore.RED + "Failed to edit key!")

keep_alive()

#-----SETUP-----#
prefix = '='
#use the .env feature to hide your token
token = ("OTAxNTgxMjU2MjgwNjQ1Njgy.GuvP0X.WXCbIlMLd4sJOKmSCo0Z3NA_ml0LvdvxQhttB4")
bot = commands.Bot(command_prefix=prefix, help_command=None, case_insensitive=True, self_bot=True)

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send(f"""
**Lista de Comandos:**
**{prefix}help** - Ajuda Comando
**{prefix}start** - Inicia o bot!
**{prefix}stop** - Para o bot!
**{prefix}evtrain** - Ajuda a treina Ev's
""")

@bot.command()
async def start(ctx):
	await ctx.message.delete()
	await ctx.send('Ativado com sucesso, Auto Farm Myuu! | by **vinikkz**')
	global dmcs
	dmcs = True
	while dmcs:
			await ctx.send('.route 25')
			await asyncio.sleep(2)
			await ctx.send(random.randint(2, 4))
			await asyncio.sleep(1.5)
	
@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Desativado com sucesso, Auto Farm Myuu! | by **vinikkz**')
	global dmcs
	dmcs = False 
  
@bot.command()
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

@bot.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.watching, name="Ur mom")
  await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
  
  print(f'''
{Fore.BLUE}
███╗░░░███╗██╗░░░██╗██╗░░░██╗██╗░░░██╗
████╗░████║╚██╗░██╔╝██║░░░██║██║░░░██║
██╔████╔██║░╚████╔╝░██║░░░██║██║░░░██║
██║╚██╔╝██║░░╚██╔╝░░██║░░░██║██║░░░██║
██║░╚═╝░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░░░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░
░██████╗░██████╗░██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝░██╔══██╗██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██████╔╝██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║░░╚██╗██╔══██╗██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║██║░╚███║██████╔╝███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
''')

try:
  bot.run(token, bot=False)
except:
  print("Invaild Token!")