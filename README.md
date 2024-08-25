# Discord_Bot
A Bot with various administrative and miscellaneous features. This project was created to both for fun as a discord bot seemed like a fun summer project as well as to explore concepts such as SQL databases, External API interactions, and basic GUI design. <br />

As of 24/08/2024, This project will not be worked on (Despite a **much** needed code rewrite and minor bug fixes) and can be considered finished for the time being due to other active projects and time commitments.

![image](https://github.com/user-attachments/assets/34feec08-0576-4dbf-9150-970088539197)

**Current Features:**
* OCR support <br />
Using the Pytesseract library, OCR support can be added to the discord bot. This is done by locally downloading the target image from a discord chat message. The local image is then processed by the Pytesseract library with the text readout then outputted in a text message by the bot back to the original text channel.
  
* Wikipedia searchs <br />
Using the the Wikipedia library and API, Built in wikipedia search support can be built directly into the bot and by extension, Discord.
 
* Music Player (With GUI) <br />
Using FFmpeg, a locally based music player can be used with the bot.

* SQL Integration <br />
This discord bot can be integrated with a SQL server for database purposes. Data from user text messeges can be parsed, sorted, and sent to a SQL database for data gathering purposes.

# Gallery

![image](https://github.com/user-attachments/assets/2d76e50e-c171-4cc6-952a-38386d2ed526)
![image](https://github.com/user-attachments/assets/6d3f18f8-551a-4601-a202-f7ce002e10f1)
![image](https://github.com/user-attachments/assets/4d307b07-72c7-44e1-80ee-22220aaa639d)

  
# Required packages (Dependancies):
OCR
* Pillow
* PyTesseract
* NumPy
  
Main
* Discord.py

SQL Integration
* mysql.py
  
Misc
* datetime
* time
* wikipedia
* requests
