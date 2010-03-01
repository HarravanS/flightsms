#-*- coding: utf-8 -*-

import urllib

from parser import *
from utils import *


#class for send commands to vola gateway
class vola_cmd:

	#cmd  1 - sms credit
	def get_Credit(self,username,password):
		url = "%s?UID=%s&PWD=%s&CMD=1&SERIAL=%s" % (gateway,username,password,serial)
		sock = urllib.urlopen(url)
		gw_answer = sock.read()
		sock.close()
		return gw_answer
	
	#cmd 14 - send sms
	def send_Message(self,username,password,cid,sender,phones,text,date,time):
		url = "%s?UID=%s&PWD=%s&CMD=14&SERIAL=%s&SENDDATA=%s%s%s%s%s%s" % (gateway,username,password,serial,cid,"%09"+sender,"%09"+str(format_PhoneNumbers(phones)),"%09"+str(encode_MessageText(text)),"%09"+str(date),"%09"+str(time))
		print url
		#sock = urllib.urlopen(url)
		#gw_answer = sock.read()
		#sock.close()
		#return gw_answer
	
	#cmd 44 - send to gateway multiple sms and wait
	def send_MultiMessage(self,username,password,cid,sender,phones,text,date,time):
		url = "%s?UID=%s&PWD=%s&CMD=44&SERIAL=%s&SENDDATA=%s%s%s%s%s%s" % (gateway,username,password,serial,cid,"%09"+sender,"%09"+str(format_PhoneNumbers(phones)),"%09"+str(encode_MessageText(text)),"%09"+str(date),"%09"+str(time))
		print url
		#sock = urllib.urlopen(url)
		#gw_answer = sock.read()
		#sock.close()
		#return gw_answer
	
	#cmd 45 - confirm for multiple sms
	def confirm_MultiMessage(self,username,password,orderId):
		url = "%s?UID=%s&PWD=%s&CMD=44&SERIAL=%s&ORDERID=%s" % (gateway,username,password,serial,orderId)
		print url
		#sock = urllib.urlopen(url)
		#gw_answer = sock.read()
		#sock.close()
		#return gw_answer
	
	#cmd 32 - get sender list
	
