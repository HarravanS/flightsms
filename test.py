#-*- coding: utf-8 -*-

from flightsmslib import *
from history import *

impostazioni = usersetup()
messaggi = vola_cmd()
hH = smshistory()

def main_menu():
	mchoise = "CHOISE AN OPTION\n\n\
	x) press X for settings\n\
	m) press M to send message\n\
	h) press H for history\n\
	c) press C to view credit\n\
	Q) press Q to exit"
	print mchoise
	m_action = raw_input("choise: ")
	if m_action == ("x" or "X"):
		settings_menu()
	elif m_action == ("m" or "M"):
		username, password = loginUPData()
		dest = raw_input("receiver: ")
		smesg = raw_input("message: ")
		print parse_Result("14",messaggi.send_Message(username,password,nextcid(),"flightsms",[dest],smesg,"0000-00-00","00:00"))
	elif m_action == ("h" or "H"):
		history_menu()
	elif m_action == ("c" or "C"):
		username, password = loginUPData()
		print parse_Result("1",messaggi.get_Credit(username,password))
		m_action = ""
		main_menu()
	elif m_action == "Q":
		quit("\n\nbye\n\n")
	else:
		print "\n\nYou must select one of the following options\n\n"
		main_menu()

def settings_menu():
	schoise = "CHOISE AN OPTION\n\n\
	a) press A for view settings\n\
	u) press U to set new user and pass\n\
	k) press K to set receive key\n\
	q) return to main menu"
	print schoise
	s_action = raw_input("choise: ")
	if s_action == ("a" or "A"):
		print "username: " + impostazioni.get_LoginUser()
		print "password: " + impostazioni.get_LoginPass()
		print "receivekey: " + impostazioni.get_ReceiveKey()
		s_action = ""
		settings_menu()
	elif s_action == ("u" or "U"):
		n_user = raw_input("insert new user: ")
		n_pass = raw_input("insert new pass: ")
		impostazioni.set_LoginData(str2hash(n_user),str2hash(n_pass))
		s_action = ""
		settings_menu()
	elif s_action == ("k" or "K"):
		n_rkey = raw_input("insert new key: ")
		impostazioni.set_ReceiveKey(n_rkey)
		s_action = ""
		settings_menu()
	elif s_action == ("q" or "Q"):
		m_action,s_action = "",""
		main_menu()
	else:
		print "\n\nYou must select one of the following options\n\n"
		settings_menu()

def history_menu():
	hchoise = "CHOISE AN OPTION\n\n\
	p) press P for print full history\n\
	i) press A to insert a message in history\n\
	c) press C to clean history\n\
	q) press M to main menu"
	print hchoise
	h_action = raw_input("choise: ")
	if h_action == ("p" or "P"):
		hH.show_History
		h_action = ""
		history_menu()
	elif h_action == ("a" or "A"):
		pass
	elif h_action == ("I" or "C"):
		pass
	elif h_action == "q":
		m_action,h_action = ""
		main_manu()
	else:
		print "\n\nYou must select one of the following options\n\n"
		history_menu()

def msg_menu():
	gchoise = "CHOISE AN OPTION\n\n\
	N) press N for view settings\n\
	q) return to main menu"
	print gchoise
	g_action = raw_input("choise: ")
	if s_action == ("n" or "N"):
		pass
	elif s_action == ("q" or "Q"):
		m_action,g_action = ""
		main_manu()
	else:
		print "\n\nYou must select one of following option\n\n"
		msn_menu()

print "*" * 32 + "\nFLIGHTSMS easy test client\n" + "*" * 32 + "\n\n\n"

main_menu()


