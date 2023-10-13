import discord
from discord.ext import commands, tasks

import requests

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

    #GET ARRAY OF IMAGES

class Buttons_Music_Interaction(discord.ui.View):

    def __init__(self, ctx):
            self.ctx = ctx

            super().__init__(timeout = None)