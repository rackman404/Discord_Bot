import discord
from discord.ext import commands, tasks
import string

#import PyNaCl

#PYTESSERACT
from PIL import Image
import pytesseract
import numpy as np
#IMAGE DOWNLOAD FROM URL and FILE MANAGEMENT
import requests
import os
#TIME TRACKING
import datetime
import time

#INITILIZATION -------------------------

token =  "MTEzMjA4MDUwNTY3MjY5OTk2NQ.GWYiiE.MuSF322Heb_6J4xw6gZf7f-xecqRN688U20gYI" #os.getenv("DISCORD_TOKEN")
my_guild = "361552282287996928"    #os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix ="$", intents=intents)


utc = datetime.timezone.utc #timezone (note utc is 5 hours ahead of est)


set_times = [
    ##datetime.time(hour=7, tzinfo=utc), #NOTE THAT DATETIME.TIME IS AHEAD BY 4 HOURS (FORMAT IS HH:MM:SS)
    datetime.time(4, 0, 1), #midnight
    #datetime.time(20, 22, 50) #testtime
]


#INITILIZATION -------------------------

#FUNCTIONS -------------------------

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
    elif (sent_message.find(".png") != -1) or (sent_message.find(".jpg") != -1):
        return 100
    else:
        return

def search_found_command_phrase(sent_message):
    sent_message = sent_message.lower()
    if sent_message.find("translate for me majed") != -1:
        return 10

def nhentai_code_check(sent_message):
    seperated_message = list(sent_message)

    if len(seperated_message) == 6:
        for i in seperated_message:
            if (48 <= ord(i) <= 57): #ord converts string to unicode
                continue
            else:
                return False
        return True

def image_download_and_OCR_scanner (embeds):
    img_data = requests.get(embeds).content #???
    with open('tempimage_ocr.png', 'wb') as handler: #creates a temp file for image
        handler.write(img_data) #writes image to file ???

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    filename = 'tempimage_ocr.png' #defines filename as temp file above
    img1 = np.array(Image.open(filename)) #???
    scannedString = pytesseract.image_to_string(img1) #scans image with OCR and converts words into string

    os.remove("tempimage_ocr.png") #removes temp file afterwards
    
    return scannedString

#FUNCTIONS -------------------------

#TASKS ---------


#seconds = time_to_midnight (initial_time)

@tasks.loop(time=set_times)
async def timer():
    channel = client.get_channel(1132913818318680094)
    await channel.send("GM <@536340598375055361> <@351878946637479957> <@655354170601242634>")

#TASKS ---------


#COMMANDS -----------



@bot.command ()
async def p(ctx): #passes through message to command
    channel = ctx.author.voice.channel
    vc= await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="Y:/Utilities/ffmpeg-6.0-essentials_build/bin/ffmpeg.exe", source="C:/Users/jacky/Music/phoenixlegends.mp3"))


#EVENTS -------------------------

@bot.event
async def on_ready():

    timer.start()


#INITIALIZATION INFO ---
    for guild in bot.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{bot.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )
#INITIALIZATION INFO ---


@bot.event
async def on_message(message):
    author = message.author # sets the variable "author" to the id of the user who sent "message"
    channelid = message.channel.id
    strmessage = message.content # copys message contents to the strmessage variable (of string type)
    
    #EXPERIMENTAL BUILD (FOR TESTING, REMOVE ON LIVE VERSION)
    #if (channelid != 1132913818318680094):
    #    return

    if (message.author.bot):
        return  


    # STRING CHECK ---

    #elif ((nhentai_code_check(strmessage) == True) and channelid == 1083235734481276968):
        #await message.channel.send("https://www.nhentai.net/g/" + strmessage)
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

    # STRING CHECK ---

    # EMBEDDED IMAGE CHECK ---

    #if channelid == 1132913818318680094:
    """
    if (1 == len(message.attachments)): #If theres 1 AND ONLY 1 Attachment to the message
        strattachments = message.attachments[0].url
        if search_found_phrases(strattachments) == 100: #If .png is found to be the file extension
            print (str(image_download_and_OCR_scanner(strattachments))) #TEMP AND SHOULD BE REMOVED AFTER TESTING
            scannedstring = str(image_download_and_OCR_scanner(strattachments))
            scannedstring = scannedstring.strip() #TEMP AND SHOULD BE REMOVED AFTER TESTING

            if search_found_command_phrase(strmessage) == 10:
                await message.channel.send(scannedstring)
    """

    # EMBEDDED IMAGE CHECK ---

    #TODO
    #INDIA TIME FUNCTION (BASE IT OFF OF SYSTEM CLOCK?)
    #DEFINITIONS (IDK HOW EVEN)
    #MAKE A COUNTER FOR MENTIONS OF N WORD
    #PERSISTENT NICKNAME FOR BOT

    #KVM Raspberry

#EVENTS -------------------------

    #PASS TO COMMANDS
    await bot.process_commands(message)

bot.run(token)
















