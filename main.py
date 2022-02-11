import discord
from discord.ext import tasks

client = discord.Client()
msgCount = 0
mbrCount = 0

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    await client.change_presence(activity=discord.Game(name="logging statistics"))

@client.event
async def on_message(message):
    global msgCount
    global msgLog

    print('Message from {0.author}: {0.content}'.format(message))
    msgCount += 1

@client.event
async def on_member_join(member):
    global mbrCount
    mbrCount += 1

@tasks.loop(hours=24)
async def DailyLoop():
    global msgCount
    global mbrCount
    print("daily announcement")
    if (discord.utils.get(client.get_all_channels(), name="daily-notices") != None):
        await discord.utils.get(client.get_all_channels(), name="daily-notices").send(f"@everyoneDAILY NOTICE\nMessages sent in the past 24 hours: {msgCount}\nNew members joined in the past 24 hours: {mbrCount}")
        msgCount = 0
        mbrCount = 0
DailyLoop.start()

client.run("OTQxNDgwOTI3NTQ3MjMyMzM3.YgWkcA.wZxqPLXkRt0WVCcmujDGtA_MaWY")