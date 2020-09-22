import time
import discord
from datetime import timedelta

# the token for the bot to use to connect to Discord servers
# (the physical servers that Discord relies on, like the ones that go on server racks, not "Discord servers"
TOKEN: str = "REPLACE WITH TOKEN"

# the instructions for how to use the bot
INSTRUCTIONS: str = "Hello!\nusage:\n \"!time convert [hour to convert] [min to convert] [your current hour]\"\n IMPORTANT: all times are in 24 HOUR format!!!"

# the bot's client
client = discord.Client()


@client.event
async def on_ready():
    """
    Runs when the bot has ben initialized and is online.
    Specifically, this Overridden version prints a message to the console once this has happened.
    """
    print("time bot is running")


@client.event
async def on_message(message):
    """
    Handles every message sent to the parts of the Discord server this bot is allowed to see.
    Specifically, this Overridden version processes messages with the bot's prefix and reacts accordingly.
    :param message: an object containing all of the information about the message.
    """
    if message.author != client.user:
        # sends the help message if the user requests it
        if message.content.startswith("!time help"):
            await message.channel.send(INSTRUCTIONS)

        # responds with a conversion link if the user requests one
        elif message.content.startswith("!time convert "):
            data = [([int(p) for p in t.split(":")]) for t in message.content[14:].split(" ")]
            data.append(message.author.name)
            await message.channel.send(generate_link(data))


def generate_link(data: list) -> str:
    """
    Generates a link that can be used to convert the timezone of the given time.
    :param data: a list containing
        [1] a list of ints containing the hours and minutes of the target time
        [2] a list of ints containing the hours and minutes of the sender's current local time
        [3] a str containing the sender's username
    :return: a str containing the generated URL
    """
    og_time = str(data[0][0]) + ":" + str(data[0][1])
    difference = timedelta(hours=data[0][0], minutes=data[0][1]).total_seconds() - \
                 timedelta(hours=data[1][0], minutes=data[1][1]).total_seconds()
    username = data[2]
    return "https://cjbell630.github.io/discord_time_bot/html/time.html?" + \
           "name=" + username + "&" + \
           "og_time=" + og_time + "&" + \
           "target_time_utc=" + str((difference + time.time()) * 1000)


# starts the bot's client
client.run(TOKEN)
