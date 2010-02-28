import sqlite3
from Contact import *
from Group import *

_DB_PATH = 'contacts.db'

class ContactList:

	def __init__(self):
		# would be better passing along a db connection, 
		# it's no good opening and closing everytime..
		self._con = sqlite3.connect(_DB_PATH)
		self._checkDB()
		
		self._contacts = []
		self._groups = {}
		self._groupid2group = {}
		self._groupid2name = {}
		self._groupname2id = {}
		
		self._loadContacts()
		self._loadGroups()
			
	def _loadContacts(self):
		#
		# populate contacts
		#
		cur = self._con.cursor()
		cur.execute('SELECT * FROM contacts')
				
		for row in cur:
			groups = []
			if row[5] != None:
				groups = row[5].split()
			c = Contact(row[0], row[1], row[3], row[2], row[4], groups)
			self._contacts.append(c)
			
			
	def _loadGroups(self):
		#
		# populate groups
		#
			
		cur = self._con.cursor()
		cur.execute('SELECT * FROM groups')
		
		for row in cur:
			self._groupid2name[row[0]] = row[1]
			self._groupname2id[row[1]] = row[0]
			
			if (row[1].find('.') >= 0):
				parent = self._groups[row[1].split('.')[0]] # can throw exc XXX => subgroup without parent
				c = parent.addSubgroup(row[0], row[1], row[2])
			else:
				c = Group(row[0], row[1], row[2])
				self._groups[row[1]] = c
				
			self._groupid2group[row[0]] = c
			
			
	def _checkDB(self):
		cur = self._con.cursor()
		cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
		
		found = False
		
		for row in cur:
			if row[0] == 'contacts':
				found = True
				break

		if not found:
			cur.execute("create table contacts (id integer primary key autoincrement, name text, surname text, mobile text, notes text, groups text)")
			cur.execute('insert into contacts values (NULL,?,?,?,?,?)', ('Name','Surname','+39111002233444', 'abc abcd', 'plugs plugs.adm'))
			self._con.commit()
			cur.execute("create table groups (id integer primary key autoincrement, name text, descr text)")
			cur.execute('insert into groups values (NULL,?,?)', ('plugs', 'PLUGS association members'))
			cur.execute('insert into groups values (NULL,?,?)', ('plugs.adm', 'PLUGS administration group'))
			self._con.commit()
			print 'DBG: contacts/groups db init'

		
	def id2group(self, id):
		if id in self._groupid2group:
			return self._groupid2group[id]
		else:
			return None
			
	def id2groupname(self, id):
		if id in self._groupid2name:
			return self._groupid2name[id]
		else:
			return None
			
	def groupname2id(self, name):
		if id in self._groupname2id:
			return self._groupname2id[name]
		else:
			return None
		
	# groups is a list of Group names, maybe we'll change
	def addContact(self, name, mobile, surname=None, notes=None, groups=[]):
		nc = None
			
		try:
			nc = Contact(0, name, mobile, surname, notes, groups) #contact takes a list of groups names too
		except:
			return None
		
		cur = self._con.cursor()
		cur.execute('insert into contacts values (NULL,?,?,?,?,?)', (name, surname, mobile, notes, ' '.join(groups)))
		self._con.commit()
		cur.execute('SELECT last_insert_rowid() as last_insert_rowid')
		row = cur.fetchone()
		nc._id = row[0]
		self._contacts.append(nc)
		return nc

	def getContactByID(self, id):
		c = filter(lambda x: x.getID() == id, self._contacts)
		if len(c) > 0:
			return c[0]
		else:
			return None
		
	def delContact(self, id):
		if self.getContactByID(id) != None:
			cur = self._con.cursor()
			cur.execute('delete from contacts where id = ?', (id,))
			self._con.commit()
			self._contacts = filter(lambda x: x.getID() != id, self._contacts)
			return True
		else:
			return False
		
	
	def getContacts(self):
		return self._contacts
		
	def getGroupByName(self):
		return self._groups
		
	def getGroups(self):
		return self._groups.items()
