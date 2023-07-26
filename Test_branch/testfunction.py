import string

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





string = "136791";


print(nhentai_code_check(string))
