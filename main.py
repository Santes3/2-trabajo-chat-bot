import discord,os,comando as c
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("dt")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='()', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command (name="psw")
async def pasword(ctx,largo = 25):
    x = c.contra(largo) 
    await ctx.send(f"🔐Contraseña generada: {x}")
    
@bot.command (name="coin")
async def flip(ctx):
    x = c.flipcoin() 
    await ctx.send(f"🪙ELECCION : {x}")



bot.run (TOKEN)