# it can be used to check number before insertion
# maybe should be moved in utilities ?
def isMobileValid(num):
	return True


class Contact:
		
	def __init__(self, id, name, mobile, surname=None, notes=None, groups=[]):
		if not isMobileValid(mobile):
			raise Exception('param not valid', 'mobile')

		if name == None:
			raise Exception('param not valid', 'name is None')

		if len(name) == 0:
			raise Exception('param not valid', 'name len is 0')
			
		self._id = id
		self._name = name
		self._mobile = mobile
		self._surname = surname
		self._notes = notes
		self._groups = groups
		
	def __str__( self ):
		groups_str = ''
		for g in self._groups:
			groups_str = groups_str + '\t\t' + g + '\n' 
		return '\n(%-2d) Name:%s Surname:%s\n\tMobile:%s\n\tNotes:%s\n\tGroups:\n%s' % (self._id, self._name, self._surname, self._mobile, self._notes, groups_str)

	def getID(self):
		return self._id
		
	def getName(self):
		return self._name

	def setName(self, name):
		if name == None: 
			raise Exception('param not valid', 'name is None')
		
		if len(name) == 0:
			raise Exception('param not valid', 'name len is 0')
		
		self._name = name

	def getSurname(self):
		return self._surname

	def getMobile(self):
		return self._mobile

	def setMobile(self, mobile):
		if not isMobileValid(mobile):
			raise Exception('param not valid', 'mobile')
		
		self._mobile = mobile

	def getNotes(self):
		return self._notes

	def getGroups(self):
		return self._groups
	

