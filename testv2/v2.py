from selenium import webdriver
from datetime import datetime


driver = webdriver.Firefox()
driver.get("https://yandex.ru/time/")

test_time = "12:30"

def comparing_time ():
		title = driver.title.split(" ")
		arg = {"err": " - ОШИБКА: ", "success": " - УСПЕХ:  ", "eql": " = ", "non_eql": " ≠ ", "time": title[0]}
		if title[0] == test_time:
			res =  "%(success)s%(time)s%(eql)s" %(arg)
		else:
			res =  "%(err)s%(time)s%(non_eql)s" %(arg)
		return res

log_data = {"time_now" :datetime.strftime(datetime.now(), "%H:%M:%S"), 
						"ct_str"   :comparing_time(), 
						"test_time":test_time,
						"new_line" :"\n"}


log_v2 = open("log_v2.txt", "a")
log_v2.write("%(time_now)s%(ct_str)s%(test_time)s%(new_line)s" %(log_data)) 
log_v2.close()
driver.close()