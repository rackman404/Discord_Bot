import discord
import string

#INITILIZATION

token =  "MTEzMjA4MDUwNTY3MjY5OTk2NQ.GWYiiE.MuSF322Heb_6J4xw6gZf7f-xecqRN688U20gYI" #os.getenv("DISCORD_TOKEN")
my_guild = "361552282287996928"    #os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#INITILIZATION

#FUNCTIONS

def search_found_Nword(sent_message):
    sent_message = sent_message.lower()
    sent_message = sent_message.replace(" ", "")

    if (sent_message.find("nigger") != -1) or (sent_message.find("nigga") != -1) or (sent_message.find("n1ig3rs") != -1): #if words are not found (returns -1)
        return 1
    else:
        return


def search_found_phrases(sent_message):
    sent_message = sent_message.lower()
    if sent_message.find("kys") != -1:
        return 2
    elif sent_message.find("bruh") != -1:
        return 3
    else:
        return

#FUNCTIONS

#EVENTS

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )

@client.event
async def on_message(message):
    author = message.author # sets the variable "author" to the id of the user who sent "message"
    strmessage = message.content # copys message contents to the strmessage variable (of string type)

    if (message.author.bot):
        return  
    elif (message.author.id == 536340598375055361) and (search_found_Nword(strmessage) == 1): #If praneith says the n word
        await message.channel.send("of course praneith is being racist again. bro really did just say '" + strmessage + "' This is why you will never get a higher GPA than Soham and why your dad is in Italy.")
        await message.pin()
        return
    elif (search_found_Nword(strmessage) == 1): #If anyone else says the n word
        await message.channel.send("bruh thats racist")
        await message.channel.send(str(author) + " has been kicked for being racist")
        await message.delete()
        await author.kick(reason = "said the forbidden n word")
    elif (search_found_phrases(strmessage) == 2):
        await message.reply("no you kys")
    elif (search_found_phrases(strmessage) == 3):
        await message.channel.send("bruh")
    else:
        return

        #NEXT STEPS: OCR?? https://builtin.com/data-science/python-ocr

#EVENTS

client.run(token)