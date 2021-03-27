from discord.ext import commands
import discord
import json

bot = commands.Bot(',')

amounts = {}

@bot.event
async def on_ready():
    global amounts
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}

@bot.command(pass_context=True)
async def balance(ctx):
    id = ctx.message.author.id
    if id in amounts:
        await ctx.send("You have {} in the bank".format(amounts[id]))
    else:
        await ctx.send("You do not have an account")

@bot.command(pass_context=True)
async def register(ctx):
    id = ctx.message.author.id
    if id not in amounts:
        amounts[id] = 100
        await ctx.send("You are now registered")
        _save()
    else:
        await ctx.send("You already have an account")

@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    primary_id = ctx.message.author.id
    other_id = other.id
    if primary_id not in amounts:
        await ctx.send("You do not have an account")
    elif other_id not in amounts:
        await ctx.send("The other party does not have an account")
    elif amounts[primary_id] < amount:
        await ctx.send("You cannot afford this transaction")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.send("Transaction complete")
    _save()

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

@bot.command()
async def save():
    _save()
