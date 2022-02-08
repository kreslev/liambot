import os

import discord
from discord import message
from dotenv import load_dotenv

import help
import emailSender
import liam

#Created 2022 by Kreslev and T34p075. So blame them.

# Welcome to the code of Liam Bot!
# Beyond this point lies madness.
# Turn back now or risk insanity.
# This bot is made to scan for a help message
# and take the following actions:
# Email a group of people (set in emailSender.py)
# Send an alert to person's discord inbox
# Alert user on specific channel.

# Loads discord token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Establishes client
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connect to Discord!')

# Listener for chat commands.
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    #Listens for mentions of bot
    if client.user.mentioned_in(message):
        await message.channel.send(liam.quote(message.author.name))

    #Command to test if bot is running
    if message.content == "!rolecall":
        await message.channel.send(help.rollcall(message.author.name))
    
    #Returns an about message
    if message.content == "!about":
        await message.channel.send(help.aboutMessage())

    if "golden ratio" in message.content.casefold():
        await message.channel.send("The Golden Ratio is 1:1.61803398875.")

    if "fibonacci" in message.content.casefold():
        await message.channel.send("The first few numbers of the Fibonacci Sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...")

    #Scans all messages on channel for the word help
    if ("help" in message.content.casefold() or "sos" in message.content.casefold() or "911" in message.content.casefold())\
        and not message.content.startswith("!help"):
        
        if (message.author.bot):
            await message.channel.send("I do not help bots.")
        else:
            #Gets name of current channel
            channel2 = message.channel.name
            #Gets name of message author
            name = message.author.name
            #Sends reassuring message on channel
            await message.channel.send("It's okay, " + name + ", help is on its way.")
            #Sends a private message to author with emergency information
            await message.author.send(help.helpMessage())
            #Sends email
            emailSender.sendEmail(name, message.content)
        
            #Gets admin channel and drops mention with author and channel name
            channel = client.get_channel(922611939148976159)
            await channel.send("<@133397776565403648>, **" + name + "** has requested assistance"\
                " in channel **" + channel2 + "**.\nSaying:\n" + message.content)

    #Returns simple unit conversion
    if message.content.startswith("!convert"):
        await message.channel.send(liam.convert(message.content))


client.run(token)
