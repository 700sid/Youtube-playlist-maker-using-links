# Install selenium before running the script


import re
from selenium import webdriver
from time import sleep
from getpass import getpass


class Automate:
    def __init__(self, username, pwd, links):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(10)
        count = 0
        unusedlinks = []
        errorslist = []
        for link in links:
            try:
                count = count+1
                self.driver.get(link)
                sleep(3)
                self.driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-button-renderer[2]/a').click()
                sleep(2)
                self.driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/ytd-add-to-playlist-renderer/div[2]/ytd-playlist-add-to-option-renderer[2]/paper-checkbox').click()
                sleep(2)
                print("{} Completed, {} Remaining".format(count, len(links)-count))

            except Exception as error:
                print("{} Completed, {} Remaining, error happens May be video Unavailable".format(count, len(links)-count))
                unusedlinks.append(link)
                errorslist.append(error)

        with open('error.txt', 'w') as f:
            f.write(','.join(map(str, unusedlinks)))
            f.write(','.join(map(str, errorslist)))
        print('Links that are not added to playlist are stored in error.txt')


file = input('Input filename Make Sure that file is in same folder :')
with open(file, 'r', encoding='utf8') as f:
    links = f.read()

urls = re.findall(r'(?P<url>https?://youtu[^\s]+)', links)
urls = set([x for x in urls])

user = input('Enter Username :')
password = getpass()

Automate(user, password, urls)
