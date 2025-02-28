import discord,os
from dotenv import load_dotenv
import comando as c


load_dotenv()
token = os.getenv("dt")

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('-elbicho'):
        await message.channel.send("SIUUUUUUU!!!")
    elif message.content.startswith('-contraseña'):
        item = c.contra(25)
        await message.channel.send(f"Tu contraseñña es: {item}")
    else:
        await message.channel.send(message.content)

client.run(token)