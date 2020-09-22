import discord
from datetime import timedelta

TOKEN = "REPLACE WITH TOKEN"

INSTRUCTIONS = "Hello!\nusage:\n \"!time convert [hour to convert] [min to convert] [your current hour]\"\n IMPORTANT: all times are in 24 HOUR format!!!"

HTML = [
    "<p><span id=\"datetime\"></span></p>" + "\n" + "<script>" + "\n" + "var dt = new Date();" + "\n" + "document.getElementById(\"datetime\").innerHTML = \"",
    "\\'s time is \" + (((new Date()).getHours() + ",
    ")%24) + \":",
    " your time\"" + "\n" + "</script>"
]

client = discord.Client()


@client.event
async def on_ready():
    print("time bot is running")


@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith("!time help"):
            await message.channel.send(INSTRUCTIONS)
        elif message.content.startswith("!time convert "):
            data = [int(p) for p in (t.split(":") for t in message.content[14:].split(" "))]
            data.append(message.author.name)
            generate_link(data)
            await message.channel.send(file=discord.File("time.html"))


# TODO: make dif store a time value (ex 12:30 means 12 hours and 30 mins difference from UTC)
def generate_link(data):
    difference = timedelta(hours=data[1][0], minutes=data[1][1]) - timedelta(hours=data[0][0], minutes=data[0][1])
    dif = "{0:.0f}:{1:.0f}".format(difference.seconds / 3600, (difference.seconds / 60) % 60)
    username = data[2]
    return "https://cjbell630.github.io/discord_time_bot/html/time.html?name=" + username + \
           "&og_time=" + str(data[0][0]) + ":" + str(data[0][1]) + "&difference=" + dif


client.run(TOKEN)
