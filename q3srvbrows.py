import sys
import os
import requests

serverList=["195.133.146.111:20018","server.unfreeze.ga:27960"]

def getDirectory():

	if pathDirectory == NULL:
		pathDirectory = raw_input("Enter the path of your file: ")
	else:
		return

	#assert os.path.exists(pathDirectory), "I did not find the file at, "+str(user_input)
	#f = open(pathDirectory,'r+')
	#print("Hooray we found your file!")
	#stuff you do with the file goes here
	#f.close()

def callServers():

	hostname = serverList[0]
	response = os.system("ping -c 1 " + hostname)

	#and then check the response...
	if response == 0:
  		print hostname, 'is up!'
	else:
  		print hostname, 'is down!'

def callServers_2():

	apiResponse = requests.get("https://use.gameapis.net/quake3/query/info/195.133.146.111:20018")
	print(apiResponse.content)

	

print callServers_2()

