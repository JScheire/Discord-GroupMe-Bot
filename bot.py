import os
import discord
import aiohttp
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GROUPME_BOT_ID = os.getenv('GROUPME_BOT_ID')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

client = discord.Client()

endpoint = f'https://api.groupme.com/v3/bots/post?bot_id={GROUPME_BOT_ID}'

async def post(message):
    payload = {'text': f'{message.content}'}
    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, json=payload) as response:
            print(await response.json())

@client.event
async def on_message(message):
    if message.channel.name == CHANNEL_NAME:
        return await post(message)

@client.event
async def on_ready():
    print('Bot is ready')

<<<<<<< HEAD
client.run(DISCORD_TOKEN)
=======
client.run(DISCORD_TOKEN)
>>>>>>> 58f68b68308d3e12711655ecf393cf885d41845e
