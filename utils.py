#-*- coding: utf-8 -*-

import hashlib

from dbhandle import *
from history import *


#get user and pas
def loginUPData():
	userdata = usersetup()
	username = userdata.get_LoginUser()
	password = userdata.get_LoginPass()
	return username,password
	
#formatting a phone numbers list 
def format_PhoneNumbers(phone_list):
	phonebook = ""
	for phone in phone_list:
		if phone[0] != "+":
			phone = "+39" + phone	
		if len(phonebook) > 1:
			phonebook += "%2C" + phone
		else:
			phonebook += phone
	return phonebook

#url-encoding message content
def encode_MessageText(data):
	return urllib.quote(data.decode('utf-8').encode('iso-8859-1'))

#clear string to hex md5
def str2hash(data):
	hash_string = hashlib.md5()
	hash_string.update(data)
	return hash_string.hexdigest()

#get first unused cid
def nextcid():
	h = smshistory()
	last = h.lastcid_History()
	return (last + 1)

try_h = smshistory()
print "=" * 30 + "history:"
try_h.show_History()
try_h.add_History(1,"+393334455667","flightsms","this is a test","sent","ok",None,None)
print "=" * 30 + "history:"
try_h.show_History()
print "\n\nnext cid is"
print nextcid()
try_h.clear_History()
print "=" * 30 + "history:"
try_h.show_History()
	