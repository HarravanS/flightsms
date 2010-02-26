#-*- coding: utf-8 -*-

##### temporary #####
import hashlib
import urllib
import sqlite3.dbapi2 as sqlite
#####################



#configuration variables
gateway = "https://sms.vola.it/cgi/volasms_gw_plus2.php"
serial = "TR45GDLBO730HDUIEQJ5"
db_name = "flightsms.db"


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

#gateway output parsing
def parse_Result(cmd,in_data):
	error_codes={
			"88" : "SERIAL non corretto",
			"89" : "richiesta non valida",
			"93" : "errore AUTORESPONDER",
			"94" : "errore VCODE",
			"96" : "errore interno del gateway",
			"97" : "credito insufficiente",
			"99" : "errore di autenticazione"}

	parsed = in_data[16:-20].split()
	returned = str(parsed[0])

	if returned != "01":
		print error_codes[returned]
	else:
		if str(cmd) == "1":
			print "hai a disposizione " + parsed[1][0:2] + " messaggi"
		if str(cmd) == "14":
			print "messaggio inviato correttamente"
		if str(cmd) == "44":
			answer = parsed[1]
			answer.split(",")
			print answer
		if str(cmd) == "45":
			print "messaggio inviato correttamente"
	


#class to manage settings
class settings:
	
	def get_LoginUser(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("select value from userdata where id='user'")
		hash_user = dbcur.fetchone()
		return "%s" % (hash_user)
		dbcur.close()
		connect.close()

	def get_LoginPass(self):
		connect = sqlite.connect(db_name)
	 	dbcur=connect.cursor()
	 	dbcur.execute("select value from userdata where id='pass'")
	 	hash_pass = dbcur.fetchone()
		return "%s" % (hash_pass)
	 	dbcur.close()
		connect.close()
	
	def get_ReceiveKey(self):
		connect = sqlite.connect(db_name)
	 	dbcur=connect.cursor()
	 	dbcur.execute("select value from userdata where id='rkey'")
	 	receivekey = dbcur.fetchone()
		return "%s" % (receivekey)
	 	dbcur.close()
		connect.close()
	
	def set_LoginData(self,clear_username,clear_password):
		#creating object for md5 handling
		hash_username = hashlib.md5()
		hash_password = hashlib.md5()
		#add user and pass in hash
		hash_username.update(clear_username)
		hash_password.update(clear_password)
		#put hash to variables in hexadecimal format
		vola_username = hash_username.hexdigest()
		vola_password = hash_password.hexdigest()
		#connect to database
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		#insert new records
		print "%s\n%s" % (vola_username,vola_password)
		dbcur.execute("update userdata set value=? where id='user'", [vola_username])
		dbcur.execute("update userdata set value=? where id='pass'",[vola_password])
		#database commit
		connect.commit()
		dbcur.close()
		connect.close()
	
	def set_ReceiveKey(self,rkey):
		#connect to database
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		#insert new record
		dbcur.execute("update userdata set value=? where id='rkey'",[rkey])
		#database commit
		connect.commit()
		dbcur.close()
		connect.close()



#class for send commands to vola gateway
class vola_cmd:

	#cmd  1 - sms credit
	def get_Credit(self):
		username, password = loginUPData()
		url = "%s?UID=%s&PWD=%s&CMD=1&SERIAL=%s" % (gateway,username,password,serial)
		sock = urllib.urlopen(url)
		result = sock.read()
		sock.close()
		parse_Result("1",result)
	
	#cmd 14 - send sms
	def send_Message(self,cid,sender,phones,text,date,time):
		username, password = loginUPData()
		url = "%s?UID=%s&PWD=%s&CMD=14&SERIAL=%s&SENDDATA=%s%s%s%s%s%s" % (gateway,username,password,serial,cid,"%09"+sender,"%09"+str(format_PhoneNumbers(phones)),"%09"+str(encode_MessageText(text)),"%09"+str(date),"%09"+str(time))
		print url
		#sock = urllib.urlopen(url)
		#result = sock.read()
		#sock.close()
		#parse_Result("14",result)
	
	#cmd 44 - send to gateway multiple sms and wait
	def send_MultiMessage(self,cid,sender,phones,text,date,time):
		username, password = loginUPData()
		url = "%s?UID=%s&PWD=%s&CMD=44&SERIAL=%s&SENDDATA=%s%s%s%s%s%s" % (gateway,username,password,serial,cid,"%09"+sender,"%09"+str(format_PhoneNumbers(phones)),"%09"+str(encode_MessageText(text)),"%09"+str(date),"%09"+str(time))
		print url
		#sock = urllib.urlopen(url)
		#result = sock.read()
		#sock.close()
		#parse_Result("44",result)
	
	#cmd 45 - confirm for multiple sms
	def confirm_MultiMessage(self,orderId):
		username, password = loginUPData()
		url = "%s?UID=%s&PWD=%s&CMD=44&SERIAL=%s&ORDERID=%s" % (gateway,username,password,serial,orderId)
		print url
		#sock = urllib.urlopen(url)
		#result = sock.read()
		#sock.close()
		#parse_Result("45",result)
	
	#cmd 32 - get sender list
	
