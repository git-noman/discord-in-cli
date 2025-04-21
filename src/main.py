import os
from dotenv import load_dotenv

import discord

from events import on_ready, on_message

client = discord.Client(intents=discord.Intents.default())
load_dotenv()

for event in [on_ready, on_message]:
    event.setup(client)

client.run(os.environ.get('TOKEN'), bot=False)