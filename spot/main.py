import discord
import os

client = discord.Client()


# listening for a client event
@client.event
# on_ready waits for our bot to be logged in
async def on_ready():
    print(f"{client.user} logged in now!")


@client.event
# function that will run whenever a message is sent
async def on_message(message):
    print(message.content)
    # print(dir(message))


my_secret = os.environ['TOKEN']
client.run(my_secret)
