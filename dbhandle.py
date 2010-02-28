#-*- coding: utf-8 -*-

import sqlite3.dbapi2 as sqlite
from conf import *


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