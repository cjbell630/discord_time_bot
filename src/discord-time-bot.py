import discord

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
            data = [int(i) for i in message.content[14:].split(" ")]
            data.append(message.author.name)
            generate_link(data)
            await message.channel.send(file=discord.File("time.html"))


def generate_link(data):
    dif = str(data[0] - data[2])
    username = data[3]
    formatted_des_min = (str(data[1]) if len(str(data[1])) > 1 else "0" + str(data[1]))
    hour_to_convert = str(data[0])
    file = open("time.html", "w")
    file.write(HTML[0] + hour_to_convert + ":" + formatted_des_min + " " + username + HTML[1] + dif + HTML[
        2] + formatted_des_min + HTML[3])
    file.close()
    return "https://cjbell630.github.io/discord_time_bot/html/time.html?name=" + username + \
           "&og_time=" + hour_to_convert + ":" + formatted_des_min + "&difference=" + dif


client.run(TOKEN)
