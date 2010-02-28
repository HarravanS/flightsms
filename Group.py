class Group:

	def __init__(self, id, name, description):
		if name.find('.') > 0:
			raise Exception('invalid param', 'name is a subgroup')
			
		self._id = id
		self._name = name
		self._descr = description
		self._subgroups = {}
		
	def addSubgroup(self, id, name, descr):
		if name.find('.') < 0:
			raise Exception('invalid param', 'name is NOT a subgroup')
		
		tmp = name.split('.')
		parent = tmp[0]
		if parent != self._name:
			raise Exception('invalid param', 'parent group does NOT match')
			
		subname = tmp[1]
		
		if subname in self._subgroups:
			raise Exception('invalid param', 'subgroup already exist')
		
		subgroup = Group(id, subname, descr)
		self._subgroups[subname] = subgroup
		return subgroup
		
	def subString(self):
		return '\t(%-2d) %s (%s)\n' % (self._id, self._name, self._descr)
		
		
	def __str__(self):
		sg_str = ''
		for sgn in self._subgroups:
			sg = self._subgroups[sgn]
			sg_str = sg_str + sg.subString() 
		return '\n(%-2d) Groupname:%s Description:%s\n%s' % (self._id, self._name, self._descr, sg_str)