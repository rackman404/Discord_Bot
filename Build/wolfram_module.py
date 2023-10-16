import discord
from discord.ext import commands, tasks

import requests
import string

def GetWolfram(Query):
    Query = Query.strip()
    Query = Query.replace("+", " plus ")
    Query = Query.replace("-", " minus ")

    simpleAppid = "K6UG4H-6YPEX7VYRQ"

    xml = requests.get("http://api.wolframalpha.com/v2/query?appid=" + simpleAppid + "&input=" + r'"' + Query + r'"' "&podstate=Step-by-step solution")

    print ("http://api.wolframalpha.com/v2/query?appid=" + simpleAppid + "&input=" + r'"' + Query + r'"' +"&podstate=Step-by-step solution") #debugging

    xmlStr = str(xml.content) #string conversion of xml 

    xmlStr = xmlStr.replace("amp;", "") # replaces amp link

    next_pod = 0
    image_list = []

    boolean = True #do while emulation

    while(boolean == True):

        imageLocationStart = xmlStr.find("img src=", next_pod) # finds start 
        imageLocationEnd = xmlStr.find("'" + r'\n' , imageLocationStart) # and end of image link
        next_pod = imageLocationEnd

        #print (str(imageLocationStart) + "\n" + str(imageLocationEnd))

        if (imageLocationStart == -1 or imageLocationEnd == -1): #error code for when first image doesnt exist
            return -1
        else:
            image_list.append(xmlStr[imageLocationStart+9:imageLocationEnd])
        
        if xmlStr.find("img src=" , next_pod) == -1:
            boolean = False

    

    print (image_list) #debug
    return image_list

class Buttons_Wolfram_Interaction(discord.ui.View):
    def __init__(self, ctx, image_list):
        self.ctx = ctx
        self.image_list = image_list

        self.current_image = 0
        self.buttonRightStatus = None
        self.buttonLeftStatus = None

        super().__init__(timeout = None)
        
    def setEmbedView(self, embedView):
        self.embedView = embedView


    @discord.ui.button (label = "←", style = discord.ButtonStyle.blurple, disabled = True)
    async def LeftInteraction(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_image = self.current_image - 1  

        for child in self.children:
            if ((self.buttonRightStatus and self.buttonLeftStatus) != None):
                break
            if type(child) == discord.ui.Button and child.label == "→":
                self.buttonRightStatus = child
            if type(child) == discord.ui.Button and child.label == "←":
                self.buttonLeftStatus = child

        updateEmbed = discord.Embed(title= "Results", description = str(self.current_image + 1) + " Out of " + str(len(self.image_list)), color = 0x00ff00)
        updateEmbed.set_image(url = self.image_list[self.current_image])


        
        if (self.current_image) == 0:
            self.buttonLeftStatus.disabled = True
            await interaction.response.edit_message(view=self)
        elif self.buttonRightStatus.disabled == True:
            self.buttonRightStatus.disabled = False
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.defer()
        

        await self.embedView.edit (embed = updateEmbed)
    
    @discord.ui.button (label = "→", style = discord.ButtonStyle.blurple)
    async def RightInteraction(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_image = self.current_image + 1  

        for child in self.children:
            if ((self.buttonRightStatus and self.buttonLeftStatus) != None):
                break
            if type(child) == discord.ui.Button and child.label == "→":
                self.buttonRightStatus = child
            if type(child) == discord.ui.Button and child.label == "←":
                self.buttonLeftStatus = child

        updateEmbed = discord.Embed(title= "Results", description =  str(self.current_image + 1) + " Out of " + str(len(self.image_list)), color = 0x00ff00)
        updateEmbed.set_image(url = self.image_list[self.current_image])

        if (self.current_image) == len(self.image_list) -1:
            self.buttonRightStatus.disabled = True
            await interaction.response.edit_message(view=self)
        elif self.buttonLeftStatus.disabled == True:
            self.buttonLeftStatus.disabled = False
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.defer()
           

        await self.embedView.edit (embed = updateEmbed)



        