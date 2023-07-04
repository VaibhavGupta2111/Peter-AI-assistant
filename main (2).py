import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


#	hour = int(datetime.datetime.now().hour)
#	if hour>= 0 and hour<12:
#		speak("Good Morning Sir !")
#
#	elif hour>= 12 and hour<18:
#		speak("Good Afternoon Sir !")
#
#	else:
#		speak("Good Evening Sir !")
#
#	assname =("Peter")
#	speak("I am your Assistant")
#	speak(assname)

def wishMe():
	currenttime = datetime.datetime.now()
	currenttime.hour
	if currenttime.hour>= 0 and currenttime.hour<12:
		speak("Good Morning Sir !")

	elif currenttime.hour>= 12 and currenttime.hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("Peter")
	speak("I am your Assistant")
	speak(assname)


def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('rajjjukajjju123@gmail.com', 'ninjahatori')
	server.sendmail('rajjjukajjju123@gmail.com', to, content)
	server.close()


if __name__ == 'main':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)  #4651653065164651236165132321516
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			music_dir = "C:\\Users\\HP\\Music"       #8678964546987/81418428
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")    #657198789264878
			speak(f"Sir, the time is {strTime}")


		elif 'email to vaibhav' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "Receiver email address"             #49872698598614926859865498645 blankkkk
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()                     #7848168486786 input nai liya
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		#elif "change my name to" in query:
		#	query = query.replace("change my name to", "")
		#	assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by vaibhav gupta.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())    #154894654
			
		elif "calculate" in query:
			
			app_id = "JGTWUT-KQGHR68A2Y"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to vaibhav gupta. further It's a secret")

		#elif 'power point presentation' in query:
		#	speak("opening Power Point presentation")
		#	power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"   #78419872897987
		#	os.startfile(power)

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by vaibhav gupta")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister vaibhav gupta ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
			speak("Background changed successfully")

		#elif 'open bluestack' in query:
		#	appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
		#	os.startfile(appli)

		elif 'news' in query:  #697982965678584168469846984
			
			try:
				jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=\\b7615d3cfc1146b88f40cc209f1295ab\\''')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.co.in/maps/place/" + location + "")   #9287987986    %20 kaise hatae

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "vaibhav Camera ", "img.jpg")         

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "sojao" in query or "sleep" in query:
			speak("Hibernating")                             #9287986468
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")    #687486744864 invalid format de rha e 
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

		 			
		
		elif "Peter" in query:
			
			wishMe()
			speak("Peter in your service Mister")
			speak(assname)

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather
			api_key = "001ec09b8530a6503947dd2e49a03bd6"                                           #bcufkebceucbeufcuebcu error de rha e 
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + "9c53d0fe518f7b97832bcf33c8f72f6e" + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["code"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")
			
		elif "send message " in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'SK34040884e3b7d305ae48dabe502a5f88'         #RECIEVER NO ?
				auth_token = 'YtxaTpiDrEPLujabea76bpafVlBcsfRf'
				client = Client(account_sid, auth_token)

				message = client.messages \
		                                    .create(body = takeCommand(),from_='7970094791',to ='Receiver No')

				print(message.sid)

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("JGTWUT-KQGHR68A2Y")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		# elif "" in query:
			# Command go here
			# For adding more commands

