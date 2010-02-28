#-*- coding: utf-8 -*-

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