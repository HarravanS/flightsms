#-*- coding: utf-8 -*-

import sqlite3.dbapi2 as sqlite

from conf import *


class smshistory():

	#new history entry
	def add_History(self, cid, receiver, sender, message, genre, status, orderid, notes):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("insert into history values (?,?,?,?,?,?,?,?,?)",(None,cid, receiver, sender, message, genre, status, orderid, notes))
		connect.commit()
		dbcur.close()
		connect.close()
	
	def get_History(self,args):
		pass
	
	#return all history
	def show_History(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("select * from history")
		self.history = dbcur.fetchall()
		
		for row in self.history:
			return row
		
		dbcur.close()
		connect.close()
	
	#delete all history entry
	def clear_History(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("delete from history")
		connect.commit()
		dbcur.close()
		connect.close()
	
	#obtain last cid in history
	def lastcid_History(self):
		connect = sqlite.connect(db_name)
		dbcur=connect.cursor()
		dbcur.execute("select * from history order by cid desc")

		self.cid_row = dbcur.fetchone()
		return int(self.cid_row[1])

		dbcur.close()
		connect.close()

