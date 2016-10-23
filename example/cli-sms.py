#!/usr/bin/python
# Example App
# @author ksdme

# Get The Libs
import pytextbelt, sys

# Usage:
# 	./cli-sms.py <Phone> <Message>

if __name__ == "__main__":

	# Getta Param
	phone, message = sys.argv[1:]

	recepient = pytextbelt.Textbelt.Recepient(phone)
	print "Sent Successfully!" if recepient.send(message)["success"] else "Sending Failed!"