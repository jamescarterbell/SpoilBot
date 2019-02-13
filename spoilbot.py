# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
from discord import Game, Emoji, User
from discord.ext.commands import Bot
import randomgen

BOT_PREFIX = ("spoilme ", "Spoilme ")
TOKEN = "NTM3NzA1NTQxNTk0NjQ0NTI4.Dz43gw.pUCEZE022gKtITuLOaRd6c9NgUs"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(pass_context=True)
async def mine(context):
    text = context.message.content
    dimensions = list()
    for s in text.split(): 
        if s.isdigit():
            dimensions.append(int(s))

    bombs = list()

    for i in range(0 , dimensions[2]):
        newBomb = (random.randrange(0, dimensions[0]), random.randrange(0, dimensions[1]))
        if not newBomb in bombs:
            bombs.append(newBomb)
    
    finalText = ""

    lookup = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:']

    for x in range(0, dimensions[0]):
        for y in range(0, dimensions[1]):
            surroundings = 0

            if (x, y) in bombs:
                finalText = finalText + "||💣||"
                continue


            for xCheck in range(-1, 2):
                for yCheck in range(-1, 2):
                    if xCheck == yCheck == 0:
                        continue
                    if x + xCheck < 0 or x + xCheck >= dimensions[0]:
                        continue
                    if y + yCheck < 0 or y + yCheck >= dimensions[1]:
                        continue
                    if (x + xCheck, y + yCheck) in bombs:
                        surroundings = surroundings + 1

            finalText = finalText + "||" + lookup[surroundings] + "||"
        finalText = finalText + "\n"



    await client.delete_message(context.message)

    await client.say(finalText)

@client.command(pass_context=True)
async def makedrink(context):
    finalText = "Here's a new drink for you:\n"
    rulelist = list()
    ingredients = list(["Vodka", "#mod Rum", "#mod Whiskey", "Lighter Fluid", "Water", "#mod Milk", "Hot Sauce", "#mod Ketchup", "Coke", "#mod Juice", "#mod Extract", "#mod Paste"])
    numbers = list(range(1, 10))
    measures = list(["Oz", "ml", "mols", "Kg", "cup(s)", "tbsp", "tsp"])
    modifiers = list(["Dark", "Light #mod", "Red", "Gold", "Blue", "Spicy", "Spicy #mod", "Sweet", "Chocolate", "Vanilla", "Coconut", "Cherry", "Banana", "Orange", "Lemon", "Lime", "Clarified", "Burnt", "Blackened", "#mod Potato", "Unfiltered", "Distilled"])
    rulelist.append(randomgen.rule("#ingredient", ingredients))
    rulelist.append(randomgen.rule("#amount", numbers))
    rulelist.append(randomgen.rule("#measure", measures))
    rulelist.append(randomgen.rule("#mod", modifiers))

    rules = randomgen.rulecollection(rulelist)

    for i in range(0, random.randrange(3,6)):
        
        finalText = finalText + rules.applyRules("#amount #measure #ingredient") + "\n"

        
    await client.delete_message(context.message)

    await client.say(finalText)

@client.command(pass_context=True)
async def targetedgay(context, target):
    finalText = "#name is #adjective #adjective #effect"
    rulelist = list()
    names = list([str(target)])

    
    others = list(["Elaine", "Justin", "Brandy", "Cam", "Tranerekk"])
    adjectives = list(["Super", "Super #adjective", "Ultra", "Mega", "Fucking", "Double", "Triple", "Secretly", "Udeniably", "Horrificly", "Double #adjective", "Unapologetically"])
    effects = list(["Dumb", "Hot", "Stuck-up", "Gay", "Retarded", "Rarted", "Stupid", "Smart", "Better than #other", "Dumber than #other", "Bad at Programming"])
    rulelist.append(randomgen.rule("#name", names))
    rulelist.append(randomgen.rule("#adjective", adjectives))
    rulelist.append(randomgen.rule("#effect", effects))
    rulelist.append(randomgen.rule("#other", others))

    rules = randomgen.rulecollection(rulelist)

    finalText = rules.applyRules(finalText)
    
    await client.delete_message(context.message)

    await client.say(finalText)

@client.command(pass_context=True)
async def compare(context, target, target2):
    finalText = "#1name.as #object is #comparison than #2name.as"
    rulelist = list()
    firstnames = list([str(target)])
    secondnames = list([str(target2)])
    
    objects = list(["Code", "Car", "#animal", "Algorithm", "Dick", "Donk", "Ass", "Dab", ":dab:", "DiscordBot", "Grade"])
    comparisons = list(["Bigger", "Better", "Faster", "Stronger", "Smarter", "Slower", "Dumber", "Gayer", "Straighter", "More #something", "Less #something", "Longer", "Shorter", "Taller"])
    animals = list(["Dog", "Cat", "Horse", "Pony", "Bird", "Lizard", "Turtle", "Mouse", "Rat", "Ferrit", "Sex Slave"])
    somethings = list(["Hot", "Ugly", "Pretty", "Smart", "Dab-Worthy", ":weary:", "Y'know", "Likeable", "Relatable", "Understandable", "#animal like"])

    rulelist.append(randomgen.rule("#1name", firstnames))
    rulelist.append(randomgen.rule("#2name", secondnames))
    rulelist.append(randomgen.rule("#object", objects))
    rulelist.append(randomgen.rule("#comparison", comparisons))
    rulelist.append(randomgen.rule("#animal", animals))
    rulelist.append(randomgen.rule("#something", somethings))

    rules = randomgen.rulecollection(rulelist)

    finalText = rules.applyRules(finalText)
    
    await client.delete_message(context.message)

    await client.say(finalText)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)