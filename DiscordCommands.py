from discord import *
from discord.ext import commands
from discord.utils import get
import requests
from math import *
from random import *
from bs4 import *
from asyncio import *

import AnnexeCompteBon 



description = 'Bot Mathraining.'
bot = commands.Bot(command_prefix='&', description='Bot Mathraining, merci aux génialissimes créateurs !')

#____________________CONSTANTES_______________________________

token = 'SECRET'
valid_id = ["341619103896698892", "165728264554414081", "196705023772721153", "368050653118988292", "277155466432348160", "355047830571843584"]
NomsRoles = ["Grand Maitre", "Maitre", "Expert", "Chevronné", "Expérimenté", "Qualifié", "Compétent", "Initié", "Débutant", "Novice"]
colors = {'Novice' : 0x888888, 'Débutant' : 0x08D508, 'Débutante' : 0x08D508, 'Initié' : 0x008800, 'Initiée' : 0x008800,
          'Compétent' : 0x00BBEE, 'Compétente' : 0x00BBEE, 'Qualifié' : 0x0033FF, 'Qualifiée' : 0x0033FF, 'Expérimenté' : 0xDD77FF,
          'Expérimentée' : 0xDD77FF, 'Chevronné' : 0xA000A0, 'Chevronnée' : 0xA000A0, 'Expert' : 0xFFA000, 'Experte' : 0xFFA000,
          'Maître' : 0xFF4400, 'Grand Maître' : 0xCC0000}



nonRattachee = "Cette personne n'est pas rattachée à un compte Mathraining.\nTaper la commande &help pour plus d'informations."


#id_des_Canaux
canalDemandeBot = Object(id="448029413272190986")
canalInfoBot = Object(id="448105204349403137")
canalGeneral = Object(id="430291539449872384")


#_________________Fonctions_Annexes____________________

def roleScore(s):
    """Renvoie le role correspondant au score"""

    if s >= 7500:
        role = "Grand Maitre"
    elif s >= 5000:
        role = "Maitre"
    elif s >= 3200:
        role = "Expert"
    elif s >= 2000:
        role = "Chevronné"
    elif s >= 1250:
        role = "Expérimenté"
    elif s >= 750:
        role = "Qualifié"
    elif s >= 400 :
        role = "Compétent"
    elif s >= 200:
        role = "Initié"
    elif s >= 70:
        role = "Débutant"
    else:
        role = "Novice"

    return role


#_________________________EVENT_______________________________________

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=Game(name="Mathraining | &help"))

@bot.event
async def on_member_join(member):
    fmt = 'Bienvenue '+ member.mention + " ! Pense à lier ton compte Mathraining avec la commande &ask." + \
    "Tape &help pour en savoir plus sur le bot."
    await bot.send_message( canalGeneral ,fmt)

@bot.event
async def on_message(message):
    if message.author.name == "mtbot":
        return

    if '#' in message.content:
        msg = message.content.split()
        for i in msg:
            urlPb = ""
            if i[0] == "#":
                numeroPb = i[1:]
                if numeroPb.isdigit():
                    numeroPb = int(numeroPb)
                    with open("Problems.txt", "r") as file:
                        for line in file:
                            numero, url = map(int, line.split())
                            if numero == numeroPb:
                                urlPb = url
            if urlPb:
                aEnvoyer = "Problème " + str(numeroPb) + " : http://www.mathraining.be/problems/" + str(urlPb)
                await bot.send_message(message.channel, aEnvoyer )
    await bot.process_commands(message)

#_____________________COMMANDES___________________________________

@bot.command()
async def ask(user: Member, idMTmt: int):
    '''Pour pouvoir utiliser le bot: ask @utilisateur idMathraining
    (idMathraining est le nombre dans l'url de votre page de profil sur le site)'''

    msg = "-"*10 + "\nDemande de : " + str(user.mention) + ".\nid Mathraining : " + str(idMTmt) + "\n-------------\n"
    await bot.send_message(canalDemandeBot, msg)
    await bot.say("Attendez la validation d'un administrateur.")


@bot.command()
async def compte(result = 0):
    if result == 1:
        embed = Embed( title = "Le compte est bon", color = 0xFF4400 )
        embed.add_field( name = "Solveur", value = "https://repl.it/repls/WorrisomeSafeModes", inline = False)

    else:
        tirage = AnnexeCompteBon.compteBon()
        embed = Embed( title = "Le compte est bon", color = 0xFF4400 )
        embed.add_field( name = "Tirage", value = tirage, inline = False )

    await bot.say(embed=embed)


@bot.command()
async def correction():
    """Affiche la liste des correcteurs et leurs nombres de corrections"""

    req = requests.get("http://www.mathraining.be/correctors")
    response = req.text #on récupère le code source de la page
    soup = BeautifulSoup(response, "lxml")
    corrections = soup.find_all('td', attrs={"style":u"text-align:center;"})
    #print(corrections)
    msg = ""
    embed = Embed(title="Corrections", color=0xFF4400)

    for loop in range(0, len(corrections), 2):
        msg = ""
        msg2 = ""
        if corrections[loop+1].getText() != "0":
            if loop == 0:
                msg += "Corentin Bodart: "
            if loop == 2:
                msg += "Nicolas Radu: "
            if loop == 4:
                msg += "Rémy Lesbats: "
            if loop == 6:
                msg += "Cédric Pilatte: "
            if loop == 8:
                msg += "Damien Galant: "
            if loop == 10:
                msg += "Thomas Humbert: "
            if loop == 12:
                msg += "Damien Lefèvre: "
            if loop == 14:
                msg += "Cédric De Groote: "
            if loop == 16:
                msg += "Philippe Alphonse: "
            if loop == 18:
                msg += "Hoan-Phung Bui: "
            if loop == 20:
                msg += "Raphael Ducatez: "
            if loop == 22:
                msg += "François Staelens: "
            if loop == 24:
                msg += "Rodrigue Haya Enriquez: "
            if loop == 26:
                msg += "Errol Yuksel: "
            if loop == 28:
                msg += "Paul Cahen: "
            msg2 = corrections[loop].getText() + " corrections dont " +corrections[loop+1].getText() + " les deux dernières semaines.\n"
            embed.add_field(name=msg, value=msg2, inline=False)
    await bot.say(embed=embed)


@bot.command()
async def hi():
    await bot.say("Salut ! Comment vas-tu ?")


@bot.command()
async def info(user: Member):
    """Affiche les stats d'un utilisateur lie"""

    idMT = 0

    async for message in bot.logs_from(canalInfoBot, limit=500):
        #print(message.content)
        msg = message.content.split()
        if msg[0] == user.mention:
            idMT = msg[1]
            break

    if idMT != 0:
        url = "http://www.mathraining.be/users/"+str(idMT) #on construit l'url
        req = requests.get(url)
        response = req.text #on récupère le code source de la page
        soup = BeautifulSoup(response, "lxml")
        htmlscore = soup.find_all('p',attrs={"style":u"font-size:24px; margin-top:20px;"}, limit = 1) #on recupere le bout de code avec le score
        nameuser = soup.find_all('h1', limit = 1)
        avancement = soup.find_all('div', attrs={"class":u"progress-bar"})

        #print(avancement)
        #print(nameuser, nameuser[0].getText())
        #print(htmlscore[0].getText())

        username = ''.join(nameuser[0].getText().split('-')[:-1])
        rank = (nameuser[0].getText().split('-')[-1]).replace("\n", "")
        stats = ["Combinatoire :", "Géométrie :", "Théorie des nombres :", "Algèbre :", "Équations Fonctionnelles :", "Inégalités :"]

        #print("$"+avancement[1].getText()+"$")

        if avancement[1].getText() == "\n":
            nbpbsolved = "0/153"
        else:
            nbpbsolved = avancement[1].getText()
        embed = Embed(title=username + " - " + rank, description=url, color=colors[rank])
        embed.add_field(name="Score : ", value=htmlscore[0].getText().split()[2], inline=True)
        embed.add_field(name="Exercices résolus : ", value=avancement[0].getText(), inline=True)
        embed.add_field(name="Problèmes résolus : ", value=nbpbsolved, inline=True)
        pourcentage = []
        for i in range(2, 8):
            chaine=avancement[i]['style'][6:]
            j = 0
            stat=[]
            while chaine[j]!='.':
                stat.append(chaine[j])
                j+=1
            pourcentage.append(''.join(stat))

        for i in range(6):
            embed.add_field(name=stats[i], value=pourcentage[i]+'%', inline=True)

        await bot.say(embed=embed)

    else:
        await bot.say(nonRattachee)


@bot.command()
async def rand(borne1: int, borne2: int):
    '''Donne un nombre aléatoire entre 2 bornes'''
    nb = randint(min(borne1, borne2), max(borne2, borne1))
    await bot.say(str(nb))


@bot.command()
async def solved(user: Member, idpb: int):
    """Indique si le problème numéro numPb a été résolu par l'utilisateur"""

    idMT = 0

    async for message in bot.logs_from(canalInfoBot, limit=500):
        #print(message.content)
        msg = message.content.split()
        if msg[0] == user.mention:
            idMT = msg[1]
            break

    if idMT != 0:
        url = "http://mathraining.be/users/" + str(idMT)
        req = requests.get(url)
        response = req.text
        namepb = '#' + str(idpb)

        if namepb in response:
            await bot.say("Probleme résolu par l'utilisateur.")
        else:
            await bot.say("Probleme non résolu par l'utilisateur.")
    else:
        await bot.say(nonRattachee)


@bot.command()
async def update(user: Member):
    '''Pour mettre a jour son/ses roles'''

    idMT = 0

    async for message in bot.logs_from(canalInfoBot, limit=500):
        #print(message.content)
        msg = message.content.split()
        if msg[0] == user.mention:
            idMT = msg[1]
            break


    if idMT != 0:
        url = "http://www.mathraining.be/users/"+str(idMT)
        req = requests.get(url)
        response = req.text #on récupère le code source de la page
        soup = BeautifulSoup(response, "lxml")
        htmlscore = soup.find_all('p',attrs={"style":u"font-size:24px; margin-top:20px;"}) #on recupere le bout de code avk le score
        scoreuser = htmlscore[0].getText()
        s=""

        for char in scoreuser:
            if char.isdigit():
                s+=char

        s = int(s)

        role = roleScore(s)
        roleToRemove = ""


        for roleMembre in user.roles:
            if roleMembre.name in NomsRoles:
                roleToRemove = roleMembre.name
                break

        if role != roleToRemove :
            servRole = get(user.server.roles, name = role )
            roleToRemove = get(user.server.roles, name = roleToRemove )

            await bot.add_roles(user, servRole)

            await bot.say(role)
            await bot.say("Mis à jour !")

            await bot.remove_roles(user, roleToRemove)

        else :
            await bot.say("Déjà à jour !")

    else:
        await bot.say(nonRattachee)


@bot.command()
async def verify(user: Member, idMT: int):
    """Lie le compte d'un utilisateur au bot (ajoute son id MT dans le canal Info-bot) """
    if not (str(message.author.id) in valid_id):
        return
    await bot.add_roles(user, get(user.server.roles, name = "Vérifié") )
    await bot.send_message(canalInfoBot, str(user.mention)+ " " + str(idMT))

    url = "http://www.mathraining.be/users/"+str(idMT)
    req = requests.get(url)
    response = req.text #on récupère le code source de la page
    soup = BeautifulSoup(response, "lxml")
    htmlscore = soup.find_all('p',attrs={"style":u"font-size:24px; margin-top:20px;"}) #on recupere le bout de code avk le score
    scoreuser = htmlscore[0].getText()
    s=""

    for char in scoreuser:
        if char.isdigit():
            s+=char

    s = int(s)

    role = roleScore(s)

    servRole = get(user.server.roles, name = role )

    await bot.add_roles(user, servRole)
    await bot.say(role)





bot.remove_command('help')
@bot.command(pass_context = True)
async def help(ctx):
    embed = Embed(title="Mathraining bot", type="rich", description="Préfixe avant les commandes : &.", color=0xEEE657)

    embed.add_field(name="info @utilisateur", value="Donne le score et le rang Mathraining de l'utilisateur mentionné.", inline=False)
    embed.add_field(name="update @utilisateur", value="Pour mettre a jour son rang.", inline=False)
    embed.add_field(name="solved @utilisateur numPb", value="Indique si le problème numéro numPb a été résolu par l'utilisateur.", inline=False)
    embed.add_field(name="ask @utilisateur idMathraining", value="Pour demander à rattacher votre compte Mathraining:" +
    " idMathraining (idMathraining est le nombre dans l'url de votre page de profil sur le site).", inline=False)
    embed.add_field(name="correction", value="Affiche la liste des correcteurs et leurs contributions.", inline=False)
    embed.add_field(name="rand a b", value="Donne un nombre aléatoire entre a et b.", inline=False)
    embed.add_field(name="compte + 6 nombres", value="Effectue un tirage si aucun nombre n'est donné, résoud le tirage sinon", inline=False)
    embed.add_field(name="help", value="Affiche ce message en MP.", inline=False)

    await bot.send_message(ctx.message.author,embed=embed)

#______________________________________________________________


bot.run(token) #Token MT
