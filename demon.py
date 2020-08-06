

# Demon

# Only works with the demon-api which includes
# JS inspired, sorry if it's messy
# Created by matt

API_URL = 'http://localhost/api'


import subprocess
import keyboard
import colorama
import datetime
import requests
import discord
import ctypes
import random
import string
import mouse
import time
import json
import yaml
import re
import os

from discord.ext import commands, tasks
from subprocess import check_output
from colorama import init, Fore
from time import sleep
from os import sys, system, path

colorama.init()


# DEMON INIT


class DemonInit:
    def logo(self):
        print(f'''

{demonUtil.space}{Fore.RED}██████{Fore.LIGHTBLACK_EX}╗ {Fore.RED}███████{Fore.LIGHTBLACK_EX}╗{Fore.RED}███{Fore.LIGHTBLACK_EX}╗   {Fore.RED}███{Fore.LIGHTBLACK_EX}╗ {Fore.RED}██████{Fore.LIGHTBLACK_EX}╗ {Fore.RED}███{Fore.LIGHTBLACK_EX}╗   {Fore.RED}██{Fore.LIGHTBLACK_EX}╗
{demonUtil.space}{Fore.RED}██{Fore.LIGHTBLACK_EX}╔══{Fore.RED}██{Fore.LIGHTBLACK_EX}╗{Fore.RED}██{Fore.LIGHTBLACK_EX}╔════╝{Fore.RED}████{Fore.LIGHTBLACK_EX}╗ {Fore.RED}████{Fore.LIGHTBLACK_EX}║{Fore.RED}██{Fore.LIGHTBLACK_EX}╔═══{Fore.RED}██{Fore.LIGHTBLACK_EX}╗{Fore.RED}████{Fore.LIGHTBLACK_EX}╗  {Fore.RED}██{Fore.LIGHTBLACK_EX}║
{demonUtil.space}{Fore.RED}██{Fore.LIGHTBLACK_EX}║  {Fore.RED}██{Fore.LIGHTBLACK_EX}║{Fore.RED}█████{Fore.LIGHTBLACK_EX}╗  {Fore.RED}██{Fore.LIGHTBLACK_EX}╔{Fore.RED}████{Fore.LIGHTBLACK_EX}╔{Fore.RED}██{Fore.LIGHTBLACK_EX}║{Fore.RED}██{Fore.LIGHTBLACK_EX}║   {Fore.RED}██{Fore.LIGHTBLACK_EX}║{Fore.RED}██{Fore.LIGHTBLACK_EX}╔{Fore.RED}██{Fore.LIGHTBLACK_EX}╗ {Fore.RED}██{Fore.LIGHTBLACK_EX}║
{demonUtil.space}{Fore.RED}██{Fore.LIGHTBLACK_EX}║  {Fore.RED}██{Fore.LIGHTBLACK_EX}║{Fore.RED}██{Fore.LIGHTBLACK_EX}╔══╝  {Fore.RED}██{Fore.LIGHTBLACK_EX}║╚{Fore.RED}██{Fore.LIGHTBLACK_EX}╔╝{Fore.RED}██{Fore.LIGHTBLACK_EX}║{Fore.RED}██{Fore.LIGHTBLACK_EX}║   {Fore.RED}██{Fore.LIGHTBLACK_EX}║{Fore.RED}██{Fore.LIGHTBLACK_EX}║╚{Fore.RED}██{Fore.LIGHTBLACK_EX}╗{Fore.RED}██{Fore.LIGHTBLACK_EX}║
{demonUtil.space}{Fore.RED}██████{Fore.LIGHTBLACK_EX}╔╝{Fore.RED}███████╗{Fore.RED}██{Fore.LIGHTBLACK_EX}║ ╚═╝ {Fore.RED}██{Fore.LIGHTBLACK_EX}║╚{Fore.RED}██████{Fore.LIGHTBLACK_EX}╔╝{Fore.RED}██{Fore.LIGHTBLACK_EX}║ ╚{Fore.RED}████{Fore.LIGHTBLACK_EX}║
{demonUtil.space}{Fore.LIGHTBLACK_EX}╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{Fore.RESET}

        ''')

    def launch(self):
        system('cls')
        demonUtil.setTitle()
        demonInit.logo()

        if demonAPI.alive() == True:
            if demonAPI.authorize() == True:
                if demonConfig.config() == True:
                    return True
                    
                else: 
                    return False
            else: 
                return False
        else: 
            return False


# DEMON UTILS


class DemonUtils:
    discord_api = 'https://discord.com/api/v7'
    config_nm = 'demon.json'
    space = ''.center(15, ' ')
    version = 2

    def makeLine(self):
        terminal_column = os.get_terminal_size().columns
        space_2 = len(demonUtil.space) * 3

        print(Fore.LIGHTBLACK_EX)
        print(demonUtil.space.ljust(terminal_column - space_2, '-'))
        print(Fore.LIGHTBLACK_EX)

    def setTitle(self):
        return ctypes.windll.kernel32.SetConsoleTitleW(f'demon v{self.version}')

    def getHWID(self):
        return str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

    def log(self, data):
        layout = f'{self.space}{Fore.LIGHTBLACK_EX}[{Fore.RED}DEMON{Fore.LIGHTBLACK_EX}] {data}'

        print(layout)

    def logCommand(self, name, description):
        command_space = ''.ljust(17 - len(name), ' ')
        layout = f'{self.space}{Fore.LIGHTBLACK_EX}{name}{command_space} {Fore.RED}:: {description}{Fore.RESET}'

        print(layout)

    def randomString(self, length):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))

        return result_str


# DEMON API


class DemonAPI:
    API = API_URL

    def alive(self):
        try:
            res = requests.get(self.API)
            data = res.json()

            if data['hello'] == 'world':
                return True
            else:
                self.dead()
        except Exception:
            self.dead()

    def dead(self):
        demonUtil.log('API is currently down, try again later')
        system('pause >NUL')

        return False

    def authorize(self):
        res = requests.get(self.API + '/v1/verify', headers={'hwid': demonUtil.getHWID()})
        data = res.json()

        if data['code'] == 400:
            self.unauthorized()
        else:
            return True

    def unauthorized(self):
        demonUtil.log(f'HWID: {demonUtil.getHWID()}')
        system('pause >NUL')

        return False

    def updates(self):
        command_space = lambda name: ''.ljust(17 - len(name), ' ')

        res = requests.get(demonAPI.API + '/v1/updates', headers={'hwid': demonUtil.getHWID()})
        data = res.json()

        for msg in data['updatesKeys']:
            print(f'{demonUtil.space}{Fore.LIGHTBLACK_EX}{msg}{command_space(msg)} {Fore.RED}:: {data[msg]}{Fore.RESET}')


# DEMON CONFIG


class DemonConfig:
    attempts = 0

    def config(self):
        if os.path.isfile(demonUtil.config_nm):
            return True
        else:
            self.createConfig()

    def createConfig(self):
        res = requests.get(demonAPI.API + '/v1/config', headers={'hwid': demonUtil.getHWID()})
        data = res.json()
        
        try:
            demonUtil.log('Enter your account token')
            data['token'] = str(input(demonUtil.space + '> '))
            print()

            if self._validateToken(data['token']) != False:
                demonUtil.log('Enter a prefix for your bot')
                data['prefix'] = str(input(demonUtil.space + '> '))
                print()

                self.setConfig(data)
            else:
                self.createConfig()
        except KeyboardInterrupt:
            self.createConfig()


    def setConfig(self, data):
        with open(demonUtil.config_nm, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        system('cls')
        demonInit.logo()
        launchDemon()

    def getConfig(self):
        file = open(demonUtil.config_nm, 'r').read()

        return json.loads(file)

    def _validateToken(self, token):
        res = requests.get(demonUtil.discord_api + '/users/@me', headers={'authorization':token})
        data = res.json()

        try:
            if data['code'] == 0:
                return False

        except Exception:
            return data


# DEMON KEYBINDS


class DemonKeybinds:
    def __init__(self, bot, config):
        keyboard.add_hotkey('ctrl+f9', lambda: self.joinSupport())
        keyboard.add_hotkey('ctrl+f8', lambda: self.help(bot, config))

        self.logKeybinds()
        
    def logKeybinds(self):
        command_space = lambda name: ''.ljust(17 - len(name), ' ')

        res = requests.get(demonAPI.API + '/v1/settings?info=keybinds', headers={'hwid': demonUtil.getHWID()})
        data = res.json()

        for keybind in data['keybindKeys']:
            print(f'{demonUtil.space}{Fore.LIGHTBLACK_EX}{keybind}{command_space(keybind)} {Fore.RED}:: {data[keybind]}{Fore.RESET}')
        
        print()

    def joinSupport(self):
        config = demonConfig.getConfig()
        data = requests.get(demonAPI.API + '/v1/settings?info=invite', headers={'hwid': demonUtil.getHWID()}).json()

        requests.post(demonUtil.discord_api + f'/invites/{data["code"]}', headers={'authorization':config['token']})

    def help(self, bot, config):
        system('cls')
        demonInit.logo()

        for command in bot.commands:
            demonUtil.logCommand(f'{config["prefix"]}{command}', command.description)


# DEMON CLIENT


def launchDemon():
    config = demonConfig.getConfig()
    bot = commands.Bot(command_prefix=config['prefix']
        , self_bot=True)

    demonAPI.updates()
    DemonKeybinds(bot, config)
    bot.remove_command('help')


    # EVENTS


    @bot.event
    async def on_command_error(ctx, error):
        # if isinstance(error, commands.errors.CommandNotFound):
        #     return

        if isinstance(error, commands.errors.MissingRequiredArgument):
            return await ctx.send(f':x: usage: **{ctx.command.usage}**', delete_after=2)

        try:
            await ctx.send(f':x: *{error}*', delete_after=2)
        except Exception:
            pass

    @bot.event
    async def on_command(ctx):
        try:
            await ctx.message.delete()
        except Exception:
            pass

    @bot.event
    async def on_connect():
        demonUtil.log(f'Connected as {bot.user}')

    @bot.event
    async def on_message(msg):
        await bot.process_commands(msg)


    # UTILITY COMMANDS


    @bot.command(description="Clears the console.")
    async def cc(ctx):
        system('cls')
        demonInit.logo()

    @bot.command(aliases=["whois"], description="Displays some information about users account.")
    async def user(ctx, *, member: discord.Member=None):
        if member == None: member = ctx.author

        embed = discord.Embed(description=member.mention
            , title=f'{member} ({member.id})')

        embed = embed.add_field(name='Created At'
            , value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
            , inline=True)

        await ctx.send(embed=embed, delete_after=5)

    @bot.command(description="Marks all servers as read.")
    async def mark(ctx):
        for guild in bot.guilds:
            await guild.ack()

    @bot.command(aliases=["eat", "cl"], description="Deletes all your past messages.")
    async def prune(ctx, amount: int=None):
        if amount == None: amount = 999999

        channel = await bot.fetch_channel(ctx.channel.id)

        async for message in channel.history(limit=amount).filter(lambda msg: msg.author == ctx.message.author).map(lambda m: m):
            try:
                await message.delete()
            except Exception:
                pass

    @bot.command(aliases=["gp"], usage="[channel/user id]", description="Deletes all your past messages in provided channel/user id's channel.")
    async def ghostprune(ctx, idx):
        try:
            try:
                channel = await bot.fetch_channel(int(idx))
            except Exception:
                channel = await bot.fetch_user(int(idx))
        except Exception:
            return await ctx.send(':x: *invalid channel/user id*', delete_after=2)

        async for message in channel.history(limit=999999).filter(lambda msg: msg.author == ctx.message.author).map(lambda m: m):
            try:
                await message.delete()
            except Exception:
                pass


    # GENERAL COMMANDS
    

    @bot.command(aliases=["pfp", "av"], description="Display someones avatar.")
    async def avatar(ctx, *, user: discord.Member=None):
        if user == None: user = ctx.author

        try:
            await ctx.send(user.avatar_url)
        except Exception:
            pass


    # FUN COMMANDS


    @bot.command(usage="[amount] (arguments)", description="Spams the chat customizable amount of times.")
    async def spam(ctx, amount: int, *, msg): 
        for _i in range(amount):
            try:
                await ctx.send(msg)
            except Exception:
                pass

    @bot.command(aliases=["ping"], description="Mentions a user in every text channel.")
    async def annoy(ctx, *, member: discord.Member=None):
        if member == None: return await ctx.send(':x: *invalid user*', delete_after=3)

        for channel in ctx.guild.channels:
            try:
                await channel.send(member.mention)
            except Exception:
                pass


    # STATUS COMMANDS


    @bot.command(description="Clears your status.")
    async def cs(ctx): 
        await bot.change_presence(status=discord.Status.dnd, activity=None)

    @bot.command(aliases=["streaming"], usage="(arguments)", description="Sets your status as streaming.")
    async def stream(ctx, *, args): 
        stream = discord.Streaming(name=args
            , url='https://twitch.tv/' + bot.user.display_name)

        await bot.change_presence(status=discord.Status.dnd
            , activity=stream)

    @bot.command(aliases=["playing", "game"], usage="(arguments)", description="Sets your status as playing.")
    async def play(ctx, *, args): 
        game = discord.Game(name=args)

        await bot.change_presence(status=discord.Status.dnd
            , activity=game)

    @bot.command(aliases=["watching"], usage="(arguments)", description="Sets your status as watching.")
    async def watch(ctx, *, args):
        await bot.change_presence(status=discord.Status.dnd
            , activity=discord.Activity(
                type=discord.ActivityType.watching
                , name=args
            ))

    @bot.command(aliases=["listening"], usage="(arguments)", description="Sets your status as listening to.")
    async def listen(ctx, *, args):
        await bot.change_presence(status=discord.Status.dnd
            , activity=discord.Activity(
                type=discord.ActivityType.listening
                , name=args
            ))


    # RAID COMMANDS


    @bot.command(aliases=["ct", "text"], usage="[amount] (arguments)", description="Creates a custom amount of text channels.")
    async def createtext(ctx, amount: int, *, msg=None):
        if int(amount) > 250: return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
            
        for _i in range(amount):
            if msg == None:
                await ctx.guild.create_text_channel(demonUtil.randomString(69))
            else:
                await ctx.guild.create_text_channel(msg)

    @bot.command(aliases=["cv", "voice"], usage="[amount] (arguments)", description="Creates a custom amount of voice channels.")
    async def createvoice(ctx, amount: int, *, msg=None):
        if int(amount) > 250: return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for _i in range(amount):
            if msg == None:
                await ctx.guild.create_voice_channel(demonUtil.randomString(69))
            else:
                await ctx.guild.create_voice_channel(msg)

    @bot.command(aliases=["cr", "role"], usage="[amount] (arguments)", description="Creates a custom amount of roles.")
    async def createrole(ctx, amount: int, *, msg=None):
        if int(amount) > 250: return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for _i in range(amount):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        
            if msg == None:
                await ctx.guild.create_role(name=demonUtil.randomString(69)
                    , colour=discord.Colour.from_rgb(r, g, b))
            else:
                await ctx.guild.create_role(name=msg
                    , colour=discord.Colour.from_rgb(r, g, b))

    @bot.command(aliases=["dc"], usage="[amount] (arguments)", description="Deletes all channels in a server.")
    async def deletechannels(ctx):
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except Exception:
                pass

    @bot.command(aliases=["dt"], description="Deletes all text channels.")
    async def deletetext(ctx):
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for channel in ctx.guild.channels:
            if str(channel.type) == 'text':
                try:
                    await channel.delete()
                except Exception:
                    pass

    @bot.command(aliases=["dv"], description="Deletes all voice channels.")
    async def deletevoice(ctx):
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for channel in ctx.guild.channels:
            if str(channel.type) == 'voice':
                try:
                    await channel.delete()
                except Exception:
                    pass

    @bot.command(aliases=["dcat"], description="Deletes all categories.")
    async def deletecategory(ctx):
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for channel in ctx.guild.channels:
            if str(channel.type) == 'category':
                try:
                    await channel.delete()
                except Exception:
                    pass

    @bot.command(aliases=["dr"], description="Deletes all roles.")
    async def deleterole(ctx):
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        for role in ctx.guild.roles:
            try:
                await role.delete()
            except Exception:
                pass

    @bot.command(aliases=["raid", "poof"], description="Deletes everything.")
    async def wizz(ctx):
        if bool(ctx.guild) == False: return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)

        await ctx.guild.edit(name=demonUtil.randomString(16))

        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
            except Exception:
                pass

        for role in ctx.guild.roles:
            try:
                await role.delete()
            except Exception:
                pass

        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except Exception:
                pass


    bot.run(config['token']
        , bot=False)


if __name__ == "__main__":
    demonConfig = DemonConfig()
    demonUtil = DemonUtils()
    demonInit = DemonInit()
    demonAPI = DemonAPI()

    if demonInit.launch() != False:
        data = demonConfig.getConfig()
        user = demonConfig._validateToken(data['token'])

        launchDemon()
    else:
        system('exit')
