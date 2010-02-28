#-*- coding: utf-8 -*-

import hashlib

from dbhandle import *


#get user and pas
def loginUPData():
	userdata = settings()
	username = userdata.get_LoginUser()
	password = userdata.get_LoginPass()
	return username,password
	
#formatting a phone numbers list 
def format_PhoneNumbers(phone_list):
	phonebook = ""
	for phone in phone_list:	
		if len(phonebook) > 1:
			phonebook += "%2C%2B"+"39%s" % phone
		else:
			phonebook += "%2B"+"39%s" % phone
	return phonebook

#url-encoding message content
def encode_MessageText(content):
	return urllib.quote(content.decode('utf-8').encode('iso-8859-1'))

#clear to hex md5
def str2hash(data):
	hash_data = hashlib.md5()
	hash_data.update(data)
	return hash_data.hexdigest()