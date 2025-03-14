import random as r,string as s, discord,os

def contra (Lenght):
    Elements = s.ascii_letters+s.ascii_uppercase+s.digits+s.punctuation
    Pasword = ""
   

    for i in range (Lenght):
        Pasword += r.choice(Elements)
    return Pasword   

def flipcoin():
    coin = ["Cara","Sello"]
    return r.choice (coin)

def meme () :
    with open ("img/meme 1.webp","rb") as img :
        picture = discord.File (img)
    return picture

def memes () :
    img_Ran = r.choice (os.listdir("img"))
    with open (f"img/{img_Ran}","rb") as img :
        picture = discord.File (img)
    return picture

