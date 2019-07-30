from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='/home/eduardo/Desktop/chromedriver')


    def closeBrowser(self):
        self.driver.close()

    def login(self):

        self.driver.get('https://www.instagram.com/')
        time.sleep(2)

        loginBtn = self.driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        loginBtn.click()
        time.sleep(2)

        inputUser = self.driver.find_element_by_xpath("//input[@name='username']")
        inputUser.clear()
        inputUser.send_keys(self.username)

        inputPass = self.driver.find_element_by_xpath("//input[@name='password']")
        inputPass.clear()
        inputPass.send_keys(self.password)
        inputPass.send_keys(Keys.RETURN)
        time.sleep(2)

    def myProfile(self):

        self.driver.find_element_by_css_selector('.aOOlW.HoLwm').click()
        
        profileBtn = self.driver.find_element_by_xpath("//a[@href='/eduardpereira/']")
        profileBtn.click()

        print(len("LEN:" + str(self.driver.find_element_by_css_selector('.9AhH0'))))


        




bot = InstagramBot('')
bot.login()
bot.myProfile()