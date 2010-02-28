from ContactList import *
from Contact import *
from Group import *



cl = ContactList()
for c in cl.getContacts():
	print c
	
for g in cl.getGroups():
	print g[1]
	
	
#nc = cl.addContact('myname', '+392229090999')
print 'add contact'
nc = cl.addContact('lol', '+39102030')
nc = cl.addContact('lol', '+39102030', groups=['plugs.adm'])


print 'list'
for c in cl.getContacts():
	print c
	
print 'del'
cl.delContact(nc.getID())

print 'list'
for c in cl.getContacts():
	print c


