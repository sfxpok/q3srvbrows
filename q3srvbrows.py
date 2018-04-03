import sys
import os
import requests
import subprocess

serverList = ["195.133.146.111:20018","server.unfreeze.ga:27960"]


def getDirectory():

	pathDirectory = None

	if pathDirectory is None:
		pathDirectory = raw_input("Enter the path of your file: ")
		# executableName = raw_input("Enter the executable name: ")
	else:
		return

	assert os.path.exists(pathDirectory), "I did not find the file at, "+str(pathDirectory)
	f = open(pathDirectory,'r+')
	print("Hooray we found your file!")
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

def pingServers_2():

	apiResponse = requests.get("https://use.gameapis.net/quake3/query/info/195.133.146.111:20018")
	print(apiResponse.content)
	
	# os.system('q3 195.133.146.111:20018')
	subprocess.call('q3', shell=True, executable='/bin/bash')
	
# def printServers():

	

	
# print getDirectory()
print pingServers_2()

