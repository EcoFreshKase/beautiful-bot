import discord
from dotenv import load_dotenv
import os

print("test")
load_dotenv()

bot_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run(bot_token)
