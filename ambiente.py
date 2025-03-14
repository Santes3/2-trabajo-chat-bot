import discord

def etiqueta_reciclaje ():
    embed = discord.Embed (
        title="Tips Recicleje",
        description="El reciclaje es el proceso de convertir desechos en nuevos productos o materia prima. Es una forma de cuidar el planeta, la economía y a las personas. ",
        color=0x00aaff
    )
    embed.add_field(
        name="Beneficios del reciclaje ",
        value=""" 
         -Ahorra materias primas, energía y agua\n
         -Reduce las emisiones de gases de efecto invernadero\n
         -Limpia ciudades y sus periferias\n
         -Genera nuevos puestos de trabajo e industrias\n
         
        """,
        inline=False
        
    )
    embed.add_field(
        name="Cómo reciclar ",
        value=""" 
         -Separa la basura biodegradable y líquida de los materiales reciclables \n
         -Recicla papel y cartón, envases de plástico, de metal y de madera, botellas de vidrio \n
         -Recicla residuos orgánicos, como la fruta, verdura y restos de alimentos \n
         -Recicla electrodomésticos, pilas y similares, aceite usado \n
         
        """,
        inline=False
        
    )
    embed.add_field(
        name="Reglas",
        value=""" 
         -Reducir: minimizar el impacto en el medio ambiente produciendo menos desechos\n
         -Reutilizar: prolongar la vida útil de los objetos y los materiales \n
         -Reciclar: cuando no puedas ni reducir tu cantidad de residuos ni reutilizarlos\n
         
        """,
        inline=False
        
    )
    embed.set_thumbnail(
            url="https://i.postimg.cc/Nj2GVpqJ/recicjale1.jpg"
    )
    return embed
