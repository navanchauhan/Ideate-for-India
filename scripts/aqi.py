import requests
import json
import datetime
import sys
from prettytable import PrettyTable
import argparse


log = "true"


def supports_color():
	plat = sys.platform
	global blue, green, red, yellow, cyan
	supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
	is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
	if not supported_platform or not is_a_tty:
		blue = lambda text: text
		green = lambda text: text
		red = lambda text: text
		cyan = lambda text: text
		yellow = lambda text: text
	blue = lambda text: '\033[0;34m' + text + '\033[0m'
	green = lambda text: '\033[0;32m' + text + '\033[0m'
	red = lambda text: '\033[0;31m' + text + '\033[0m'
	yellow = lambda text: '\033[0;33m' + text + '\033[0m'
	cyan = lambda text: '\033[0;36m' + text + '\033[0m'
def logging():
	if(log == "true"):
		print(blue("[LOG] " + str(datetime.datetime.now())))
def getResponseFromWAQI():
	params = (('token', '41ecfdf888497be166376a6bedd6dd5807cc9f4e'),)
	response = requests.get('http://api.waqi.info/feed/' + myLocation + "/", params=params)
	return response
def getAQI():
	response = getResponseFromWAQI()
	if(response.json()['status'] != 200):
		logging()
		global aqi
		aqi = response.json()['data']['aqi']
		print(green("[LOG] Good Response"))
		return aqi

	else:
		logging()
		print("Bad Response")
def getCondition(quality):
	if(quality == 1):
		condition = red("Hazardous")
		return condition
	elif(quality == 2):
		condition = red("Very Unhealthy")
		return condition
	elif(quality == 3):
		condition = red("Unhealthy")
		return condition
	elif(quality == 4):
		condition = yellow("Unhealthy for sensitive people")
		return condition
	elif(quality == 5):
		condition = yellow("Moderate")
		return condition
	elif(quality == 6):
		condition = green("Good")
		return condition
def getDominantPol():
	response = getResponseFromWAQI()
	dominantpollutant = response.json()['data']['dominentpol']
	return dominantpollutant
def getQuality(aqi):
	if(aqi <= 50):
		quality = 6
		return quality
	elif(aqi <= 100):
		quality = 5
		return quality
	elif(aqi <= 150):
		quality = 4
		return quality
	elif(aqi <= 200):
		quality = 3
		return quality
	elif(aqi <= 300):
		quality = 2
		return quality
	elif(aqi <= 301):
		quality = 1
		return quality
def prettyPrint(aqi,quality,condition, dominantpollutant, myLocation):
	table = PrettyTable(['Name','Value'])
	table.add_row([blue('Location'), cyan(myLocation)])
	table.add_row([blue('AQI'),aqi])
	table.add_row([blue('Quality'),cyan(str(quality) + '/6')])
	table.add_row([blue('Dominant Pollutant'), red(dominantpollutant)])
	table.add_row([blue('Condition'),condition])
	print(table)


parser = argparse.ArgumentParser()
parser.add_argument("location", help="fetch the data for a patricular location", type=str)
argument = parser.parse_args()
myLocation = argument.location


supports_color()
aqi = getAQI()
quality = getQuality(aqi)
condition = getCondition(quality)
dominantpollutant = getDominantPol()


prettyPrint(aqi, quality, condition, dominantpollutant, myLocation)