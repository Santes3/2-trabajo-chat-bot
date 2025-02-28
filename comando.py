import random as r,string as s

def contra (Lenght):
    Elements = s.ascii_letters+s.ascii_uppercase+s.digits+s.punctuation
    Pasword = ""
   

    for i in range (Lenght):
        Pasword += r.choice(Elements)
    return Pasword   

def flipcoin():
    coin = ["Cara","Sello"]
    return r.choice (coin)