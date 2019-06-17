<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import base64
import re
import time
import os
import stat


class Demo():
		
	def login(self):
		wait=WebDriverWait(driver,500)			
		wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/ul/li[2]/a'))).click()
		username=wait.until(EC.presence_of_element_located((By.ID,'J-userName')))
		time.sleep(3)
		username.send_keys("526113727@qq.com")
		password=wait.until(EC.presence_of_element_located((By.ID,'J-password')))
		time.sleep(3)
		password.send_keys("*********")
		time.sleep(3)
		self.get_check()
		
	def get_check(self):
		place=input('手动输入验证码位置，以","间隔:')
		message=place.split(',')
		yanSol=[35,50,105,50,175,50,245,50,35,120,105,120,175,120,245,120]
		img=driver.find_element_by_xpath("//div[@id='J-loginImgArea']/img")
		imglocation=img.location
		for item in message:
			x=yanSol[int(item)*2]+imglocation.get('x')
			y=yanSol[int(item)*2+1]+imglocation.get('y')
			webdriver.ActionChains(driver).move_by_offset(x,y).click().perform()
			webdriver.ActionChains(driver).move_by_offset(-x,-y).click().perform()
			print(x,y)
		time.sleep(1)
		driver.find_element_by_xpath("//a[@id='J-login']").click() 
		time.sleep(10)       
if __name__=='__main__':
	driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
	driver.get("https://kyfw.12306.cn/otn/resources/login.html")
	time.sleep(3)
	a=Demo()
	a.login()
	
	
=======
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import base64
import re
import time
import os
import stat


class Demo():
		
	def login(self):
		wait=WebDriverWait(driver,500)			
		wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/ul/li[2]/a'))).click()
		username=wait.until(EC.presence_of_element_located((By.ID,'J-userName')))
		time.sleep(3)
		username.send_keys("526113727@qq.com")
		password=wait.until(EC.presence_of_element_located((By.ID,'J-password')))
		time.sleep(3)
		password.send_keys("*********")
		time.sleep(3)
		self.get_check()
		
	def get_check(self):
		place=input('手动输入验证码位置，以","间隔:')
		message=place.split(',')
		yanSol=[35,50,105,50,175,50,245,50,35,120,105,120,175,120,245,120]
		img=driver.find_element_by_xpath("//div[@id='J-loginImgArea']/img")
		imglocation=img.location
		for item in message:
			x=yanSol[int(item)*2]+imglocation.get('x')
			y=yanSol[int(item)*2+1]+imglocation.get('y')
			webdriver.ActionChains(driver).move_by_offset(x,y).click().perform()
			webdriver.ActionChains(driver).move_by_offset(-x,-y).click().perform()
			print(x,y)
		time.sleep(10)
		driver.find_element_by_xpath("//a[@id='J-login']").click()        
if __name__=='__main__':
	driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
	driver.get("https://kyfw.12306.cn/otn/resources/login.html")
	time.sleep(3)
	a=Demo()
	a.login()
	
	
>>>>>>> 48443e97acef20cb525ee644032115bf086e5e45
