import discord,os,comando as c, comandapi as sapi,ambiente as am
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

@bot.command (name="img")
async def meme(ctx):
    url = c.meme()
    await ctx.send(file=url)

@bot.command (name="imgs")
async def memes(ctx):
    url = c.memes()
    await ctx.send(file=url)
@bot.command(name = "patos")
async def duck(ctx):
    image_url = sapi.get_duck_image()
    await ctx.send(image_url)

@bot.command(name="eco")
async def eco(ctx):
    await ctx.send(embed=am.etiqueta_reciclaje())


bot.run (TOKEN)