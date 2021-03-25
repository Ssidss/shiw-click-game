from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading
import json

class BlowGame:
    def __init__(self):
        self.bTime= 0
        self.minItemCost = 10
        self.minItemIdx = 0

        self.item = [0, 0]
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-alert")

        self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    #chrome.get("https://tsj.tw/")
        t = threading.Thread(target = self.getWeb())
        self.blowBtn = self.chrome.find_element_by_css_selector('.btn.btn-success.mr-2.btn-lg')
        self.cleanBtn = self.chrome.find_element_by_css_selector('.btn.btn-danger.btn-lg')
        # print(self.cleanBtn)
        print(len(self.chrome.find_elements_by_css_selector('.btn.btn-primary.btn-sm')))
        self.item[0] = self.chrome.find_elements_by_css_selector('.btn.btn-primary.btn-sm')[0]
        self.item[1] = self.chrome.find_elements_by_css_selector('.btn.btn-primary.btn-sm')[1]
        tt = threading.Thread(target = self.clickIt())

    def cleanUp(self):
        self.cleanBtn.click()
        self.bTime = 0

    def getWeb(self):
        self.chrome.get("https://tsj.tw/")
    def clickIt(self):
        while 1:
            try:
                self.blowBtn.click()
                self.bTime  = int(self.chrome.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[2]/h4[2]').text.split(' ')[1])

                if self.bTime > self.minItemCost:
                    self.buyItem()
            except:
                pass

    def buyItem(self):
        self.item[self.minItemIdx].click()
        try:
            alert = self.chrome.switch_to_alert()
            alert.accept()
        except:
            pass
        itemOne = int(self.chrome.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[4]/table/tbody/tr[2]/td[3]').text.split(' ')[0])
        itemTwo = int(self.chrome.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[4]/table/tbody/tr[3]/td[3]').text.split(' ')[0])
#        print(itemOne, itemTwo)
        if itemOne < itemTwo:
            self.minItemCost = itemOne
            self.minItemIdx = 0
        else:
            self.minItemCost = itemTwo
            self.minItemIdx = 1


def main():
    blowGame = BlowGame()

if __name__ == '__main__':
    main()
