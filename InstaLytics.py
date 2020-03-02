from selenium.webdriver import Chrome
import requests
import time
import csv



class InstaLytics():

    def __init__(self, username):
        self.browser = Chrome(executable_path='/home/eduardo/Desktop/chromedriver')
        self.username = username
        self.url = "https://www.instagram.com/" + self.username + "/"
        self.info = []
        self.posts = 0


    def getBrowser(self):
        return self.browser.get(self.url)
    

    def userExists(self):
        r = requests.get(self.url)

        if r.status_code==200:
            return True
        return False

    def closeSession(self):
        self.browser.quit()

    
    def getInfo(self):
        return self.info

    
    def getNumberPosts(self):
        return self.posts


    def get_all_posts(self):

        post = 'https://www.instagram.com/p/'
        post_links = []
        
        for a in self.browser.find_elements_by_tag_name('a'):

            if post in a.get_attribute('href'):
                post_links.append(a.get_attribute('href'))
          
        time.sleep(5)
        self.posts = len(post_links)

        return post_links



    def scrollToBottom(self):

        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            

    def getData(self, links):
        body = "/html/body/div[1]/section/main/div/div/article/div[2]/"
        xDateTime = "div[2]/a/time"
        xLikes = "section[2]/div/"

        photo = "div/button/span"
        video = "/span/span"
        

        for link in links:

            t="Photo"
            self.browser.get(link)

            try:
                likes = self.browser.find_element_by_xpath(body + xLikes + photo).text
                
            except:
                t="Video"
                likes = self.browser.find_element_by_xpath(body + xLikes + video).text

            dateTime = self.browser.find_element_by_xpath(body + xDateTime).get_attribute("datetime")                        
            date, time = dateTime.split("T")
            url = link.split("/")[4]
            
            self.info.append({"Url": url, "Date": date, "Time": time[:5] , "Likes": likes, "Video/Photo": t})
        
        return self.info


    def saveCsv(self, filename):

        with open(filename, "w", newline="") as csvfile:
            
            fieldnames = ["Url", "Date", "Time", "Likes", "Video/Photo"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for imgData in self.info:
                writer.writerow(imgData)
           

    def __repr__(self): 
       return "InstaLytics(username = {})".format(self.username)   