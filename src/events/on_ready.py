import logging
import concurrent.futures
import asyncio

from core.console import Console

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H-%M",
))
logger.addHandler(console_handler)

def setup(client, config):
    @client.event
    async def on_ready():
        logger.info(f"Logged in as {client.user.name} ({client.user.id})")

        # Start accepting commands
        # This piece of code runs the console in another thread to avoid blocking other parts of the program.
        # However, this might not be the best solution/practice. Will redo this when I have time.
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
        loop = asyncio.get_event_loop()
        await asyncio.gather(
            loop.run_in_executor(executor, Console.run)
        )