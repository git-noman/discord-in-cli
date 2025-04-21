import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H-%M",
))
logger.addHandler(console_handler)

def setup(client):
    @client.event
    async def on_ready():
        logger.info(f"Logged in as {client.user.name} ({client.user.id})")