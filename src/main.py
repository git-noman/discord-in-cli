import os
import json
from dotenv import load_dotenv

import discord

from events import on_ready, on_message

client = discord.Client(intents=discord.Intents.default())
load_dotenv()

# Load config.
with open("config.json", "r") as f:
    config = json.load(f)

for event in [on_ready, on_message]:
    event.setup(client, config)

client.run(os.environ.get('TOKEN'), bot=False)