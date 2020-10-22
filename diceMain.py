import discord
import sys

# さいころの和を計算する用の関数
from func import  diceroll

TOKEN = 'NzY4NDcyMDk2MzM4MDgzOTIx.X5A9aQ.x-BeibpCobZM5dchsFYZEdYTYp8'

client = discord.Client()

@client.event
async def on_ready():
    print('--------------')
    print('Joined')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    await channel.send('Let us start a fun TRPG！')
    await channel.send('Foooooooooo!!!!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!dice"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)

client.run(TOKEN)
