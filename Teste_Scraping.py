##TESTE DE SCRAPING UTILIZANDO SELENIUM

import requests
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def getNameandPrice(url):
    option = Options()
    option.headless = False

    drive = webdriver.Firefox(executable_path = 'geckodriver', options=option)


    drive.get("https://www.casasbahia.com.br/Eletrodomesticos/maquinadelavar/Acimade10kg/lavadora-colormaq-lcs14pb-semiautomatica-com-reuso-de-agua-branca-14kg-15112803.html")

    nameElement = drive.find_element_by_xpath("//h1[@class=' css-rfo7gs eym5xli0']")
    productName = nameElement.get_attribute('innerHTML')

    priceElement =  drive.find_element_by_xpath("//span[@class='price-tag-fraction']")
    productPrice = priceElement.get_attribute('innerHTML')

    drive.quit()
    print(productName,productPrice)

    return productName,productPrice


urls = pd.read_csv('urls.csv',header=None)


[getNameandPrice(x) for x in urls[0]]









