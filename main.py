token = "Я_ХЗ_КАКОЙ_У_ВАС_ТОКЕН"
from os import system
system('pip3 install discord')
system('pip3 install discord_webhook')
system('pip3 install discord.py -U')
# system('pip install --upgrade discord-components')
system('pip3 install Button')
# system('pip install -upgrade pip')
system('pip3 install Cybernator')
system('pip3 install psutil')
import subprocess
try:
  subprocess.call("clear") # linux/mac
except:
  subprocess.call("cls", shell=True)

import discord
import asyncio
import logging
import json
import requests
import datetime
from discord import utils
from discord.ext import commands
import discord.utils
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord_components import DiscordComponents, Button, ButtonStyle
from Cybernator import Paginator
from urllib.error import HTTPError

intents = intents = discord.Intents.all()
bot = commands.Bot(command_prefix=settings['prefix'],
                       intents=discord.Intents.all(),
                       case_insensitive=True)

@bot.event
async def on_ready():


    print("███████████████████████████████")
    print("ЗАПУСК БОТА")
    print("БОТ: {0.user}".format(bot))
    print(f"PING: {round(bot.latency * 1000)}ms")

    owner = bot.get_user(id_autor_discord)
    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Game('Перезапуск бота'))
    await owner.send("**█████████████████████████████████████████████**")
    x = discord.Embed(title='**Запуск бота!**', colour=colors['write'])
    x.add_field(name='Бот:', value="**{0.user}**".format(bot), inline=False)
    x.add_field(name='Пинг:',
                value=f"```{round(bot.latency * 1000)}ms```",
                inline=True)
    x.add_field(name='ID:', value="```{0.user.id}```".format(bot), inline=True)
    x.add_field(name='TOKEN:', value=f"\n```{token}```", inline=False)
    x.timestamp = datetime.datetime.utcnow()
    await owner.send(embed=x)
@bot.comand()
...


@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Пинг бота",
        description=f"Пинг бота — {round(bot.latency * 1000)}ms",
        color=colors['write'])
    embed.set_footer(
        text="Information requested by: \n{}".format(ctx.author.display_name))
    await ctx.reply(embed=embed)

[ВАШИ КОМАНДЫ]



bot.run(token)
