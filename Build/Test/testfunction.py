import string

#PYTESSERACT
from PIL import Image
import pytesseract
import numpy as np
#IMAGE DOWNLOAD FROM URL and FILE MANAGEMENT
import requests
import os
#TIME and COROUTINES
import time
import asyncio


def search_found (sent_message):
	if (sent_message.find("nigger") == -1) and (sent_message.find("nigga") == -1): #if words are not found (returns -1)
		return False
	else:
		return True

def nhentai_code_check (sent_message):
	seperated_message = list(sent_message)

	if len(seperated_message) == 6:
		for i in seperated_message:
			if (48 <= ord(i) <= 57):
				continue
			else:
				return False
		return True

#OCR
def image_download_and_OCR_scanner (embeds):
	img_data = requests.get(embeds).content
	with open('tempimage_ocr.png', 'wb') as handler:
		handler.write(img_data)

	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

	filename = 'tempimage_ocr.png'
	img1 = np.array(Image.open(filename))
	scannedString = pytesseract.image_to_string(img1)

	os.remove("tempimage_ocr.png")
	
	return scannedString

"""
string = "https://cdn.discordapp.com/attachments/1132913818318680094/1133950394859536474/test.png";
print(image_download_and_OCR_scanner(string))
"""


## TIMER
"""
def time_to_midnight (time):
	
	initial_hour = initial_time[3]
	initial_minute = initial_time[4]

	midnight_hour = 24 - initial_hour
	midnight_minute = 60 - initial_minute

	midnight_seconds = (midnight_minute*60) + (midnight_hour*60*60)

	print ("time to midnight is " + str(midnight_hour) + ":" + str(midnight_minute))
	
	return midnight_seconds



initial_time = time.localtime(time.time()); #note that initial_time is a structure (can call individual elements in index (eg. [2] is the day of the month))

secondsleft = time_to_midnight(initial_time)

async def timer(midnight_seconds):
	for i in range (midnight_seconds):
		await asyncio.sleep(1)
		midnight_seconds = midnight_seconds - 1
		print (midnight_seconds)
	return

async def main():
	await asyncio.gather(
		#find_midnight(),
		timer(secondsleft)
	)	

asyncio.run(main())
"""



rows, cols = (10, int((55/10)))
musicList2DArray = [[]*cols for j in range(rows)]