import discord
from utils.tools import Tools
from utils.color import Colors

def setup(client, config):
    @client.event
    async def on_message(message: discord.Message) -> None:
        # Convert message to a dict
        # Not all properties are kept, only the ones I deemed important
        # Message dicts are kept as short as possible to save space in the JSON file, so
        # if you wanted to, say, perform an action on a guild, you can fetch it directly using the guild_id provided
        msg_dict = message.to_message_reference_dict()
        msg_dict['content'] = message.content
        msg_dict['author_id'] = message.author.id

        # Feed message
        Tools.feed(msg_dict)

        # All messages are fed to the message pool on arrival, after which they can be used by the rest of the program

        # Stream if config.stream = true
        if config['stream']:
            print(f"""
{Colors.BLUE}{Colors.UNDERLINE}{message.author.display_name}{Colors.RESET} -> {Colors.BLUE}{Colors.UNDERLINE}{message.guild.name}{Colors.RESET} |
{message.content} """)
