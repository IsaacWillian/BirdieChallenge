import requests
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def getNameandPrice(url):
    option = Options()
    option.headless = True

    drive = webdriver.Firefox(executable_path = 'geckodriver', options=option)


    drive.get(url)

    nameElement = drive.find_element_by_xpath("//h1[@class='ui-pdp-title']")
    productName = nameElement.get_attribute('innerHTML')

    priceElement =  drive.find_element_by_xpath("//span[@class='price-tag-fraction']")
    productPrice = priceElement.get_attribute('innerHTML')

    drive.quit()

    print(productName,productPrice)

    return productName,productPrice


urls = pd.read_csv('urls.csv',header=None)


[getNameandPrice(x) for x in urls[0]]









