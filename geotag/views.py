from django.shortcuts import render_to_response
from twilio.rest import TwilioRestClient

def index(request):
	return render_to_response("location.html")

def msg(request,tag=1):
	tag = tag.split('l')
	print tag

	tbody = "latitude:" + tag[0] + " longitude:" + tag[1]
	print tbody

	def hasNumbers(inputString):
	    return any(char.isdigit() for char in inputString)

	if hasNumbers(tbody)==True:
		account_sid = "AC47c14207880690bd090357c9fcea4d0a"
		auth_token  = "762584f2bfe14397d7607aa00b455ff7"
		client = TwilioRestClient(account_sid, auth_token)
		 
		message = client.messages.create(body=tbody,
		    to="+971552342072",
		    from_="+12243771083")
		print message.sid

	return render_to_response("msg.html")



