from interactions import listen, Client, slash_command, SlashContext
from interactions.api.events import Startup, Ready
from commands import *

import json

bot: Client = Client()


@listen()
async def on_startup(event: Startup) -> None:
    """
    Called when the bot is starting.
    :return: None
    """
    print("Bot is starting as {}!".format(bot.user.username))


@listen()
async def on_ready(event: Ready) -> None:
    """
    Called when the bot is ready.
    :return: None
    """
    print("Bot is ready as {}!".format(bot.user.username))


@slash_command(
    name="ping",
    description="Replies pong!"
)
async def ping(ctx: SlashContext) -> None:
    await ping_executor(ctx)

try:
    with open('token.json') as tokenFile:
        data = json.load(tokenFile)
    bot.start(data['token'])
except ConnectionError:
    print("Connection")
