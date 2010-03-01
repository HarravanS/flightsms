#-*- coding: utf-8 -*-

import sqlite3.dbapi2 as sqlite

from conf import *


class smshistory():

	def add_History(self, cid, receiver, sender, message, genre, status, orderid, notes):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("insert into history values (null,?,?,?,?,?,?,?,?)",(cid, receiver, sender, message, genre, status, orderid, notes))
		dbcur.close()
		connect.close()
	
	def get_History(self,args):
		pass
	
	def show_History(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("select * from history")
		self.history = dbcur.fetchall()
		
		print self.history
		
		dbcur.close()
		connect.close()
	
	def clear_History(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("delete from history")
		dbcur.close()
		connect.close()
	
	def lastcid_History(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("select * from history where cid")
		dbcur.close()
		connect.close()

