import discord
from discord.ext import commands, tasks
import string

#PYTESSERACT
from PIL import Image
import pytesseract
import numpy as np
#IMAGE DOWNLOAD FROM URL and FILE MANAGEMENT
import requests
import os
import os.path
#TIME TRACKING
import datetime
import time
import asyncio
#EXTERNAL API
import wikipedia
#OTHER
import math

#Personal Classes
import music_module
import wolfram_module

#INITILIZATION -------------------------

token =  "MTEzMjA4MDUwNTY3MjY5OTk2NQ.GWYiiE.MuSF322Heb_6J4xw6gZf7f-xecqRN688U20gYI" #os.getenv("DISCORD_TOKEN")
my_guild = "361552282287996928"    #os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix ="$", intents=intents, activity=discord.CustomActivity(name='Teaching Linear Algebra and Calculus 1'))


set_times = [
    ##datetime.time(hour=7, tzinfo=utc), #NOTE THAT DATETIME.TIME IS AHEAD BY 4 HOURS (FORMAT IS HH:MM:SS)
    datetime.time(4, 0, 1), #midnight
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
    elif ((sent_message.find(".png") != -1) or (sent_message.find(".jpg") != -1)) and (sent_message.find("https://cdn.discordapp.com/attachments/") != 1):
        return 100
    else:
        return

def search_found_command_phrase(sent_message):
    sent_message = sent_message.lower()
    if sent_message.find("m?") != -1: #DEPRECIATED
        return 10 #DEPRECIATED

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

"""
def GetWolfram(Query):
    Query = Query.strip()
    Query = Query.replace("+", " plus ")
    Query = Query.replace("-", " minus ")

    simpleAppid = "K6UG4H-6YPEX7VYRQ"

    xml = requests.get("http://api.wolframalpha.com/v2/query?appid=" + simpleAppid + "&input=" + r'"' + Query + r'"' "&podstate=Step-by-step solution")

    print ("http://api.wolframalpha.com/v2/query?appid=" + simpleAppid + "&input=" + r'"' + Query + r'"' +"&podstate=Step-by-step solution") #debug

    xmlStr = str(xml.content) #string conversion of xml 

    xmlStr = xmlStr.replace("amp;", "") # replaces amp link


    imageLocationStart = xmlStr.find("img src=", xmlStr.find("Possible intermediate steps")) # finds start 
    imageLocationEnd = xmlStr.find("'" + r'\n' , imageLocationStart) # and end of image link

    #print (str(imageLocationStart) + "\n" + str(imageLocationEnd))

    if (imageLocationStart == -1 or imageLocationEnd == -1): #error code for when image doesnt exist
        return -1
    else:
        imageURL = xmlStr[imageLocationStart+9:imageLocationEnd]
        return imageURL #sends image URL out

    #NEXT STEPS, GET ARRAY OF IMAGES
"""

def fileCounter():
    if (os.path.isfile("config/data.txt") == False):
        open("config/data.txt", 'x') 

    with open('config/data.txt', "r+") as f:
        if (os.path.getsize('config/data.txt') == 0):
            f.write("1")

        f.seek(0)
        count = f.read()

        f.seek(0)

        num = f.readlines()

        f.seek(0)
        f.write(str(int(num[0]) - 1))
        f.close()

    return count
    





#FUNCTIONS -------------------------


#Static Embeds ----


embedVarSuicide = discord.Embed(title = "Suicide Hotlines", description = "if you or your loved ones are thinking about suicide, seek help", color = 0x00ff00, url = "https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines", )
embedVarSuicide.set_image(url = "https://cdn.discordapp.com/attachments/361552282287996930/1146039651795226624/Final.gif")
embedVarSuicide.set_footer(text = "©2023 Government of Canada", icon_url = "https://media.discordapp.net/attachments/1079596478693130260/1080003377301307423/IMG_0483.gif")
embedVarSuicide.add_field (name= "If you are contemplating suicide in Canada, There is no help for you. Consider the use of MAID (Medical Assistance in Suicide). \nPhone The Government of Canada at 1.833.456.4566 (Toll Free) for more information", value = "", inline = True)
embedVarSuicide.add_field (name= "Si vous envisagez de vous suicider au Canada, il n'y a aucune aide pour vous. Envisagez le recours à l’AMM (assistance médicale en cas de suicide).Appelez le gouvernement du Canada au 1.833.456.4566 (sans frais) pour plus d'informations.", value = "",inline = True)
embedVarSuicide.add_field (name= "यदि आप आत्महत्या के बारे में सोच रहे हैं, तो सहायता उपलब्ध है, मदद के लिए किरण \n राष्ट्रीय आत्महत्या हेल्पलाइन 961-944-5504 (टोल फ्री) पर फोन करें। \n पर फ़ोन टॉक सुसाइड कनाडा उपलब्ध है।", value = "", inline = True)

embedVarHelp = discord.Embed(title = "Commands", color = 0x00ff00)
embedVarHelp.add_field(name = "$TimeNow", value = "Time in your locale", inline = True)
embedVarHelp.add_field(name = "$TimeIndia", value = "Time in IST (Indian Standard Time)", inline = True)
embedVarHelp.add_field(name = "$Whats", value = "Searches the following string message for a wikipedia article", inline = True)
embedVarHelp.add_field(name = "$Disconnect", value = "Disconnects Bot from VC if it is already connected to VC", inline = True)
embedVarHelp.add_field(name = "$PlayMusic", value = "Primitive music player (Now with pause and play functionality!)", inline = True)
embedVarHelp.add_field(name = "$OCR", value = "Reads a image attachment on same message that called the command", inline = True)
embedVarHelp.add_field(name = "$Wolfram", value = "Returns a step by step solution of a query (if it returns no result then reword your question/equation)", inline = True)

#Static Embeds ----


#TASKS ---------


@tasks.loop(time=set_times)
async def timer():

    
        


    channel = bot.get_channel(1056035329888493649)
    await channel.send("the time is now " + discord.utils.format_dt(discord.utils.utcnow(), style = "D") + " There are " + str(fileCounter()) + " Days until reading week!!!")
    
    """
    diick = await channel.send("✈️                                                                                     🏙️")
    await asyncio.sleep(1)

    for x in range(50):
        await diick.edit(content = "✈️                                                                                    🏙️")
        await asyncio.sleep(1)
        await diick.edit(content = "✈️                                                        🏙️")
        await asyncio.sleep(1)
        await diick.edit(content = "✈️                            🏙️")
        await asyncio.sleep(1)
        await diick.edit(content = "✈️      🏙️")
        await asyncio.sleep(1)
        await diick.edit(content = "💥")
        await asyncio.sleep(1)
        await diick.edit(content = "😵😵😵😵😵😵")
        await asyncio.sleep(2)

    """

#TASKS ---------





#COMMANDS -----------
bot.remove_command('help') #removes default help command 

@bot.command ()
async def testCommand (ctx):
    
    await ctx.channel.send ("the time is now " + discord.utils.format_dt(discord.utils.utcnow(), style = "D") + "There are " + str(fileCounter()) + " Days until reading week!!!")



@bot.command ()
async def Wolfram (ctx):
    ctx.message.content = ctx.message.content.replace("$Wolfram", "")
    URL = wolfram_module.GetWolfram(ctx.message.content)
    if URL != -1:
        await ctx.channel.send(URL) 
    else:
        await ctx.channel.send("No Results")

@bot.command ()
async def Help (ctx): 
    await ctx.channel.send(embed = embedVarHelp)


@bot.command ()
async def Whats (ctx):
    search_phrase = ctx.message.content.replace("$Whats ", ".")

    try:
        search_string = wikipedia.summary(search_phrase, chars = 1000)
        temp = wikipedia.suggest(search_phrase)
        if temp is None: #If no suggestions to make (eg. correct spelling)
            page = wikipedia.page(search_phrase)
        else: 
            page = wikipedia.page(str(temp)) #Uses suggested title (should match with .summary which automatically uses .suggest)

        if search_found_Nword(page.title) == 1:
            return await ctx.channel.send("page contains forbidden words")

        embed_search = discord.Embed(title= page.title, url = page.url,color = 0xEEEFF1)
        if len(page.images) >= 1 :
            embed_search.set_image(url = page.images[0])
        embed_search.add_field (name= "summary", value = search_string, inline = False)
        embed_search.set_footer(text = page.url, icon_url = "https://media.discordapp.net/attachments/1079596478693130260/1080003377301307423/IMG_0483.gif")
        await ctx.channel.send(embed = embed_search)

    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.channel.send("be more specific")
    except wikipedia.exceptions.PageError as e:
        await ctx.channel.send("Your Spelling is wrong or it doesn't exist or something else went wrong")
    except:
        await ctx.channel.send("generic error occured, the following search term may be too long or my code is dogshit idk")

@bot.command ()
async def OCR (ctx):
    if (1 == len(ctx.message.attachments)): #If theres 1 AND ONLY 1 Attachment to the message
        strattachments = ctx.message.attachments[0].url
        if search_found_phrases(strattachments) == 100: #If .png is found to be the file extension
            print (str(image_download_and_OCR_scanner(strattachments))) #TEMP AND SHOULD BE REMOVED AFTER TESTING
            scannedstring = str(image_download_and_OCR_scanner(strattachments))

            await ctx.channel.send(scannedstring)

@bot.command ()
async def PlayMusic(ctx):
    
    #exits command if user isn't in VC
    if ctx.author.voice is None:
        return await ctx.channel.send("You aren't connected to a VC fool")

    #defines the vc channel from context object (ctx) and joins the vc
    channel = ctx.author.voice.channel
    vc = await channel.connect()

    #vc = ctx.author.voice.channel

    #lists local folder file names and places them in an array while a empty array is made using the same length, it is then appended with the directory location
    music_arr = os.listdir("Y:/Coding/Live/Discord Bot/Songs/French Frog Music/")
    appended_music_arr = [""] * len(music_arr)
    for x in range (0,len(music_arr)):
        appended_music_arr[x] = "Y:/Coding/Live/Discord Bot/Songs/French Frog Music/" + music_arr[x]


    #New Algorithm


    pageCount = (int(math.ceil(len(music_arr)/10)))
    cols = 10
    musicList2DArray = [[""]*cols for j in range(pageCount)]
    
    externalCount = 0
    for i in range (0, pageCount):
        
        for j in range (0,10):
            musicList2DArray[i][j] = music_arr[externalCount]
            externalCount = externalCount + 1
            if externalCount >= len(music_arr):
                break



    #creates an embed for a list of songs
    embedVar = discord.Embed(title= "Songs", description = "playlist", color = 0x00ff00)
    for x in range (0, 10):
        embedVar.add_field (name=  musicList2DArray[0][x], value = "", inline = False)

    
    buttonViewMusic = music_module.Buttons_Music_Interaction(ctx)
    buttonEmbedInteract = music_module.Buttons_Embed_Interaction(ctx, musicList2DArray)

    await ctx.channel.send(view = buttonEmbedInteract)
    embedView = await ctx.channel.send(embed = embedVar)
    await ctx.channel.send(view = buttonViewMusic)
    
    buttonEmbedInteract.setEmbedViewAndPageCount(embedView, pageCount)
    

    #plays through the songs

    for x in range (0,len(music_arr)): 
        
        vc.play(discord.FFmpegPCMAudio(executable="Y:/Utilities/ffmpeg-6.0-essentials_build/bin/ffmpeg.exe", source=appended_music_arr[x]))
        
        vc.pause() 
        await asyncio.sleep(2.5) #Removes the Speed Up At Start of song (Buffer)
        vc.resume()

        while (vc.is_playing()) or (buttonViewMusic.pausePlayGetter() == True):
            await asyncio.sleep(1)


    vc.stop()


    await vc.disconnect()

@bot.command ()
async def Disconnect(ctx):

    voice = ctx.voice_client

    if voice is None:
        return await ctx.channel.send("I ain't connected to a VC fool") 
          
    await voice.disconnect()
    return await ctx.channel.send("Big Bertha has disconnected!")  

@bot.command()
async def TimeIndia(ctx):

    initial_time = time.localtime(time.time())
    if (initial_time[3] + 9) > 24:
        hour = int(initial_time[3]) + 9 - 24
    else:
        hour = int(initial_time[3]) + 9
    if ((initial_time[4] + 30) < 60):
        minute = int(initial_time[3]) + 30
    else:
        minute = int(initial_time[4]) + 30 - 60
        hour = hour + 1
        

    print (str(hour) + " "  +  str(minute))

    if hour > 12 and minute < 10:
        return await ctx.channel.send("time in india is " + str(hour - 12) + ":0" + str(minute) + "PM")
    elif hour < 12 and minute < 10:
        return await ctx.channel.send("time in india is " + str(hour) + ":0" + str(minute) + " AM")   
    elif hour > 12 and minute > 10:
        return await ctx.channel.send("time in india is " + str(hour - 12) + ":" + str(minute) + "PM")
    elif hour < 12 and minute > 10:
        return await ctx.channel.send("time in india is " + str(hour) + ":" + str(minute) + " AM")   

@bot.command()
async def TimeNow(ctx):
    await ctx.channel.send(discord.utils.format_dt(discord.utils.utcnow(), style = "F"))

@bot.command()
async def Test(ctx):
    channel = bot.get_channel(361552282287996930)

    c = await channel.send("✈️                            🏙️")
    await asyncio.sleep(1)

    for x in range(500):
        await c.edit(content = "✈️                                                                                    🏙️")
        await asyncio.sleep(1)
        await c.edit(content = "✈️                                                        🏙️")
        await asyncio.sleep(1)
        await c.edit(content = "✈️                            🏙️")
        await asyncio.sleep(1)
        await c.edit(content = "✈️      🏙️")
        await asyncio.sleep(1)
        await c.edit(content = "💥")
        await asyncio.sleep(1)
        await c.edit(content = "😵😵😵😵😵😵")
        await asyncio.sleep(2)





@bot.command() #in case something breaks
async def CloseTooHTR(ctx):
    await ctx.channel.send("closing")
    exit()



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


#async def on_command_error(ctx, error): #error handling
#    if isinstance(error, commands.CommandNotFound):  
#        await ctx.send("Command not found, try typing $Help for a list of commands")

@bot.event
async def on_message(message): #on messages
    author = message.author # sets the variable "author" to the id of the user who sent "message"
    channelid = message.channel.id
    strmessage = message.content # copys message contents to the strmessage variable (of string type)
    
    #FOR TESTING
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
        #await message.reply("no you kys" , delete_after = 1)
        await message.reply(embed = embedVarSuicide)
    #elif (search_found_phrases(strmessage) == 3):
        #await message.channel.send("bruh")

    # STRING CHECK --
    # EMBEDDED IMAGE CHECK ---
    
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

#EVENTS -------------------------
    
    #PASS TO COMMANDS
    await bot.process_commands(message)

bot.run(token)




    #TODO
    #make a counter for who and how much times a person has been kicked for n word (read and write from text file?)
    #Comic book reader
    #Unity, Stack objects game
    #Setup YT DL as a discord command maybe?

