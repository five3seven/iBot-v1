from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import urllib
from random import random, randint
from selenium.webdriver.chrome.options import Options

class insta:
    global whotofollow, whotounfollow
    global list
    global credentials
    def __init__(self):
        global driver
        open('credentials.txt', 'r')
        file = open('credentials.txt', 'r')
        f = file.readlines()
        credentials = []
        for line in f:
            if line[-1] == '\n':
                credentials.append(line[:-1])
            else:
                credentials.append(line)

        PATH = "https://www.instagram.com/"
        ops = Options()
        '''ops.add_argument('--headless')'''
        driver = webdriver.Chrome('chromedriver.exe', options=ops)

        driver.get(PATH)
        username = credentials[0]
        password = credentials[1]
        #detects login form
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
        )
        #enters email
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(str(username))
        #enters password
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(str(password))
        #presses the login button
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        #detects notification
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))
        )
        #closes notification
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        # detects notification
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]'))
        )
        # closes notification
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def follow_button(self):
        try:
            r = random() + randint(1, 3)
            sleep(r)
            driver.find_element_by_xpath("//button[@class='_5f5mN    -fzfL     _6VtSN     yZn4P   m4t9r ']").click()
        except:
            r = random() + randint(1, 3)
            sleep(r)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button').click()

    def unfollow_button(self):
        try:
            g = random() + randint(10, 12)
            r = random() + randint(1, 3)
            sleep(r)
            WebDriverWait(driver, g).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='_5f5mN    -fzfL     _6VtSN     yZn4P   ']"))
            )
            driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']").click()
        except:
            g = random() + randint(10, 12)
            r = random() + randint(1, 3)
            sleep(r)
            WebDriverWait(driver, g).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button'))
            )
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[4]/div/div/div/div[3]/button[1]'))
        )
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()

    def follow(self):
        whotofollow = ['steveaoki', 'louboutinworld', 'hermes',
                       'louteasdale', 'rubyrose', 'bigsean', 'beyonce', 'khloekardashian', 'caradelevingne', 'ciara',
                       'angelcandices',
                       'brunomars', 'dior', 'disneyland', 'danialves', 'gq', 'millionaire_mentor', 'mensfashionpost',
                       'justinbieber', 'liampayne',
                       'nicekicks', 'mirandakerr', 'ralphlauren', 'neymarjr', 'snoopdogg', 'thebillionairesclub',
                       'ladygaga', 'treysongz',
                       'tonyhawk', 'urbanoutfitters', 'vanessahudgens', 'zooeydeschanel', 'victoriajustice',
                       'iamzlatanibrahimovic', 'mercedesbenz', 'ryanseacrest', 'asos', 'badgalriri', 'izkiz',
                       'chrisbrownofficial',
                       'nashgrier', 'abercrombie', 'macklemore', 'aeropostale', 'xxxibgdrgn', '__youngbae__',
                       't3chmate', '8fact',
                       'champagnepapi', 'camerondallas', 'dolcegabbana', 'elliegoulding', 'garethbale11', 'gemmastyles',
                       'hm',
                       'jennamarbles', 'jessicaalba', 'justintimberlake', 'lanvinofficial', 'kingjames', 'leomessi',
                       'marvel',
                       'eminem', 'mtv', 'nickiminaj', 'natgeo', 'niallhoran', 'prada', 'onedirection', 'gucci',
                       'natgeotravel',
                       'louisvuitton', 'adidasfootball', 'lelepons', 'chanelofficial', 'adidasoriginals', 'zara',
                       'nasa',
                       'nikefootball', 'realmadrid', 'fcbarcelona', 'camila_cabello', 'ddlovato', 'katyperry', 'nike']
        for i in range(len(whotofollow)):
            follow_person = whotofollow[0]
            driver.get('https://www.instagram.com/{}/'.format(follow_person))
            if len(whotofollow) == 60 or len(whotofollow) == 30:
                d = random() + randint(10, 23)
                sleep(d)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.refresh()
            elif len(whotofollow) == 20 or len(whotofollow) == 10:
                d = random() + randint(10, 23)
                sleep(d)
            elif len(whotofollow) == 40 or len(whotofollow) == 50:
                d = random() + randint(10, 23)
                sleep(d)
            try:
                f = random() + randint(5, 8)
                WebDriverWait(driver, f).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/h2'))
                )
                self.follow_button()
                whotofollow.pop(0)
                f = random() + randint(1, 2)
                sleep(f)
                i += 1
            except:
                whotofollow.pop(0)
                i += 1
            finally:
                driver.quit()

    def unfollow(self):
        whotounfollow = ['steveaoki', 'louboutinworld', 'hermes',
                       'louteasdale', 'rubyrose', 'bigsean', 'beyonce', 'khloekardashian', 'caradelevingne', 'ciara',
                       'angelcandices',
                       'brunomars', 'dior', 'disneyland', 'danialves', 'gq', 'millionaire_mentor', 'mensfashionpost',
                       'justinbieber', 'liampayne',
                       'nicekicks', 'mirandakerr', 'ralphlauren', 'neymarjr', 'snoopdogg', 'thebillionairesclub',
                       'ladygaga', 'treysongz',
                       'tonyhawk', 'urbanoutfitters', 'vanessahudgens', 'zooeydeschanel', 'victoriajustice',
                       'iamzlatanibrahimovic', 'mercedesbenz', 'ryanseacrest', 'asos', 'badgalriri', 'izkiz',
                       'chrisbrownofficial',
                       'nashgrier', 'abercrombie', 'macklemore', 'aeropostale', 'xxxibgdrgn', '__youngbae__',
                       't3chmate', '8fact',
                       'champagnepapi', 'camerondallas', 'dolcegabbana', 'elliegoulding', 'garethbale11', 'gemmastyles',
                       'hm',
                       'jennamarbles', 'jessicaalba', 'justintimberlake', 'lanvinofficial', 'kingjames', 'leomessi',
                       'marvel',
                       'eminem', 'mtv', 'nickiminaj', 'natgeo', 'niallhoran', 'prada', 'onedirection', 'gucci',
                       'natgeotravel',
                       'louisvuitton', 'adidasfootball', 'lelepons', 'chanelofficial', 'adidasoriginals', 'zara',
                       'nasa',
                       'nikefootball', 'realmadrid', 'fcbarcelona', 'camila_cabello', 'ddlovato', 'katyperry', 'nike']
        for i in range(len(whotounfollow)):
            unfollow_person = whotounfollow[0]
            driver.get('https://www.instagram.com/{}/'.format(unfollow_person))
            if len(whotounfollow) == 80 or len(whotounfollow) == 60 or len(whotounfollow) == 40 or len(
                    whotounfollow) == 20 or len(whotounfollow) == 10:
                d = random() + randint(25, 57)
                sleep(d)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.refresh()
            try:
                f = random() + randint(2, 3)
                WebDriverWait(driver, f).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[3]/div/span/span[1]/button'))
                )
                self.unfollow_button()
                whotounfollow.pop(0)
                f = random() + randint(1, 2)
                sleep(f)
                i += 1
            except:
                whotounfollow.pop(0)
                i += 1
            finally:
                driver.quit()

    def auto_follow(self):

        while True:
            self.follow()
            s = random() + randint(462, 649)
            sleep(s)
            self.unfollow()
            s = random() + randint(462, 649)
            sleep(s)
            self.auto_follow()

    def screenShot(self, person):
        self.where = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        self.where.clear()
        self.where.send_keys(person)
        sleep(random() + randint(1, 3))
        self.button4 = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[1]')
        self.button4.click()
        self.where.send_keys(Keys.RETURN)
        sleep(random() + randint(1, 3))
        try:
            self.button5 = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div/section/div[2]/button[2]')
            self.button5.click()
            pass
        except:
            pass
        sleep(random() + randint(1, 3))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//div[contains(@class,'eLAPa')]"))
        ).click()
        n = 0
        state = True
        while state == True:
            try:
                sleep(random() + randint(2, 3))
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         "//div[contains(@class, 'ZyFrc')]"))
                ).screenshot('photos/{}{}.png'.format(person, n))
                #find a way to select the 640p image from this driver.find_element_by_xpath('//img[contains(@class, "FFVAD")]').text
                #make a loop that saves all the links and make a headless bot that saves all the pics from the links
                driver.find_element_by_xpath("//a[contains(@class, ' _65Bje  coreSpriteRightPaginationArrow')]").click()
                n+= 1
            except:
                state = False
        driver.close()
        os.startfile(os.path.realpath('photos'))

class login:
    def __init__(self):
        try:
            if os.path.getsize("credentials.txt") == 0:
                print("you need to enter your instagram credentials here:\n")
                username = input("username: ")
                password = input("password: ")
                credentials = [username, password]
                file = open('credentials.txt', 'r')
                w = open('credentials.txt', "w")
                for element in range(len(credentials)):
                    w.write(credentials[0])
                    w.write('\n')
                    credentials.pop(0)
                    element += 1
        except:
            open('credentials.txt', 'r')
            login()

class switch_account:
    def __init__(self):
        print("-----SWITCH ACCOUNT MENU-----\n")
        print("enter a new username and password")
        username = input("username: ")
        password = input("password: ")
        credentials = [username, password]
        file = open('credentials.txt', 'r')
        w = open('credentials.txt', "w")
        for element in range(len(credentials)):
            w.write(credentials[0])
            w.write('\n')
            credentials.pop(0)
            element += 1

def start(do_what):
    if do_what.lower() == "autofollow" or do_what.lower() == "follow" or do_what.lower() == "auto" or do_what.lower() == "f" or do_what.lower() == "a":
        insta().auto_follow()
        print('finish')
        start(input('enter a command\n'))
    elif do_what.lower() == "ss" or do_what.lower() == "screenshot":
        person = input('person:\n')
        insta().screenShot(person)
        print('finish')
        start(input('enter a command\n'))
    elif do_what.lower() == 'switch' or do_what.lower() == 's':
        switch_account()
        print('finish')
        start(input('enter a command\n'))
    elif do_what.lower() == 'stop':
        exit()
    else:
        print('not a valid command')
        start(input('enter a command\n'))
        
login()
start(input('enter a command\n'))