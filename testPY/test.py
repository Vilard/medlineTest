from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

print("Start script")
now = datetime.now()
driver = webdriver.Firefox()
driver.get("https://yandex.ru/time/")
log = open("log.txt", "a")
title = driver.title
testTime = "12:30"
res = "".join(i for i in title if i in "0123456789:")

if res == testTime:
	print("true" + " Current time: " + res + " testTime: " + testTime)
	log.write(datetime.strftime(datetime.now(), "%H:%M:%S") + " - SUCCESS: " + str(res) + " = " + str(testTime) + "\n")
else:
	print("false" + " Current time: " + res + " testTime: " + testTime)
	log.write(datetime.strftime(datetime.now(), "%H:%M:%S") + " - ERROR:   " + str(res) + " != " + str(testTime) + "\n")

print("Write file log.txt")

log.close()
driver.close()