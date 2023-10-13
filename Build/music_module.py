import discord
from discord.ext import commands, tasks
import string


class Buttons_Music_Interaction(discord.ui.View):
        
        def __init__(self, ctx):
            self.ctx = ctx #instance variable
            self.pauseCheck = False

            if self.ctx.voice_client != None:
                self.vc = self.ctx.voice_client

            super().__init__(timeout = None)

        @discord.ui.button (label = "Disconnect", style = discord.ButtonStyle.red)

        #If button is pressed, disconnects the bot
        async def disconnectInteraction(self, interaction: discord.Interaction, button: discord.ui.Button): #Disconnect Function
            
            if interaction.response.is_done() is False:
                if self.ctx.author.voice is None:
                    return await interaction.response.send_message("You are not in VC, you cannot disconnect", ephemeral=True)

                elif interaction.user == self.ctx.author:
                    voice = self.ctx.voice_client
                    
                    if voice is None:
                        return await interaction.response.send_message("I'm already disconnected or never been in VC") 
                    
                    await voice.disconnect()
                    button.style = discord.ButtonStyle.green
                    button.label = "Disconnected!"
                    return await interaction.response.edit_message(view=self)
    

        @discord.ui.button (label = "Pause ⏯︎", style = discord.ButtonStyle.blurple)
        async def pauseplayInteraction(self, interaction: discord.Interaction, button: discord.ui.Button): #Pause Play Function  

            if self.ctx.author.voice is None:
                await interaction.response.send_message("you are not in a VC, you cannot use this function",  delete_after = 2,  ephemeral = True)
    
           # elif self.ctx.author.voice != None:
            #    vc = self.ctx.voice_client

            if ((interaction.response.is_done() == False) and (self.ctx.author.voice != None)):
                if self.pauseCheck is False:
                    self.vc.pause() 
                    self.pauseCheck = True
                    button.label = "Play ⏯︎"
                    button.style = discord.ButtonStyle.red
                    await interaction.response.edit_message(view=self)
                elif self.pauseCheck is True:
                    self.vc.resume() 
                    self.pauseCheck = False
                    button.label = "Pause ⏯︎"
                    button.style = discord.ButtonStyle.blurple
                    await interaction.response.edit_message(view=self)

        @discord.ui.button (label = "Skip", style = discord.ButtonStyle.success) 
        async def skipInteraction(self, interaction: discord.Interaction, button: discord.ui.Button): #Skip Function
     
            if self.ctx.author.voice is None:
                await interaction.response.send_message("you are not in a VC, you cannot use this function",  delete_after = 2, ephemeral = True)

            elif interaction.response.is_done() is False :
                self.vc.stop()
                await interaction.response.send_message("Skipping!", delete_after = 2, ephemeral = True)

        def pausePlayGetter(self): #Getter function
            return self.pauseCheck;

class Buttons_Embed_Interaction(discord.ui.View):
    def __init__(self, ctx, musicList2DArray):
        self.currentPageCount = 0
        self.ctx = ctx
        self.musicList2DArray = musicList2DArray


        super().__init__(timeout = None)

    def setEmbedViewAndPageCount(self, embedView, pageCount):
        self.embedView = embedView
        self.totalPageCount = pageCount - 1
        self.buttonRightStatus = None
        self.buttonLeftStatus = None


    @discord.ui.button (label = "←", style = discord.ButtonStyle.blurple)
    async def LeftInteraction(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.currentPageCount = self.currentPageCount - 1  

        for child in self.children:
            if ((self.buttonRightStatus and self.buttonLeftStatus) != None):
                break
            if type(child) == discord.ui.Button and child.label == "→":
                self.buttonRightStatus = child
            if type(child) == discord.ui.Button and child.label == "←":
                self.buttonLeftStatus = child

        updateEmbed = discord.Embed(title= "Songs", description = "playlist", color = 0x00ff00)
        for x in range (0, 10):
            updateEmbed.add_field (name=  self.musicList2DArray[self.currentPageCount][x], value = "", inline = False)

        if (self.currentPageCount) == 0:
            self.buttonLeftStatus.disabled = True
            await interaction.response.edit_message(view=self)
        elif self.buttonRightStatus.disabled == True:
            self.buttonRightStatus.disabled = False
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.defer()

        await self.embedView.edit (embed = updateEmbed)

        print (self.currentPageCount)
        print (self.totalPageCount)

    @discord.ui.button (label = "→", style = discord.ButtonStyle.blurple)
    async def RightInteraction(self, interaction: discord.Interaction, button: discord.ui.Button): 
        self.currentPageCount = self.currentPageCount + 1

        for child in self.children:
            if ((self.buttonRightStatus and self.buttonLeftStatus) != None):
                break
            if type(child) == discord.ui.Button and child.label == "→":
                self.buttonRightStatus = child
            if type(child) == discord.ui.Button and child.label == "←":
                self.buttonLeftStatus = child

        updateEmbed = discord.Embed(title= "Songs", description = "playlist", color = 0x00ff00)
        for x in range (0, 10):
            updateEmbed.add_field (name=  self.musicList2DArray[self.currentPageCount][x], value = "", inline = False)


        if (self.currentPageCount) >= (self.totalPageCount):
            self.buttonRightStatus.disabled = True
            await interaction.response.edit_message(view=self)
        elif self.buttonLeftStatus.disabled == True:
            self.buttonLeftStatus.disabled = False
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.defer()
           
        await self.embedView.edit (embed = updateEmbed)

        print (self.currentPageCount)
        print (self.totalPageCount)
