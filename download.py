import bs4
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from func import *

def pin_search(driver, keyword, folder_name):
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.pinterest.com/ideas/")
    inp = driver.find_element(By.XPATH, """//*[@id="__PWS_ROOT__"]/div[1]/div/div/div[1]/div/div[2]/div/div/form/div/div[1]/div[2]/div/input""")
    inp.send_keys(keyword,Keys.RETURN)
    #Scrolling all the way up
    new_height = scroll(driver, 2)

    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
    containers = pageSoup.findAll('div', {'class':"XiG zI7 iyn Hsu"} )
    len_containers = len(containers)
    driver.execute_script("window.scrollTo(0,0);")

    print(f"Found {len(containers)} image containers in PINTEREST")
    time.sleep(3)
    last_height = 0
    for i in range(1, len_containers+1):
        if i%8 == 0:
            last_height += new_height/12
            driver.execute_script(f"window.scrollTo(0,{last_height});")
            time.sleep(2)

        xPath = """//*[@id="mweb-unauth-container"]/div/div[2]/div[2]/div/div/div/div[1]/div[%s]/div/div/div/div/div[1]/a/div/div/div/div/div[1]"""%(i)
        previewImageXPath = """//*[@id="mweb-unauth-container"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div[%s]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/img"""%(i)
        previewImageElement = driver.find_element(By.XPATH, previewImageXPath)
        previewImageURL = previewImageElement.get_attribute("src")
        timeStarted = time.time()
        k=0
        while True:
            try:
                driver.find_element(By.XPATH,xPath).click()
                break
            except:
                currentTime = time.time()
                if currentTime - timeStarted > 10:
                    k=1
                    break
                continue
        if k == 1:
            continue
        try: # ignore logging in/signing up
            time.sleep(2)
            driver.find_element(By.XPATH,"""//*[@id="__PWS_ROOT__"]/div[1]/div/div[3]/div/div/div/div/div/div[1]/button""").click()
        except:
            pass

        time.sleep(3)
        # wait for loading high resolution
        timeStarted = time.time()
        k = 0
        while True:
            if i >= 2:
                time.sleep(3)
                from selenium.webdriver.common.action_chains import ActionChains
                p = """//*[@id="__PWS_ROOT__"]/div[1]/div/div[1]/div[1]/div/div[1]/div[1]"""
                element_to_hover_over = driver.find_element(By.XPATH, p)
                hover = ActionChains(driver).move_to_element(element_to_hover_over)
                hover.perform()

            generalElement = driver.find_element(By.XPATH, """//*[@id="mweb-unauth-container"]/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/div""")
            try: 
                imageElement = driver.find_element(By.XPATH,"""//*[@id="mweb-unauth-container"]/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/img""")
            except:
                k = 1
                break

            imageElement = driver.find_element(By.XPATH,"""//*[@id="mweb-unauth-container"]/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/img""")
            imageURL = imageElement.get_attribute('src')
            if imageURL != previewImageURL: # found a high resolution image
                break
            else:
                #making a timeout if the full res image can't be loaded
                currentTime = time.time()
                if currentTime - timeStarted > 10:
                    print("Timeout! Will download a lower resolution image and move onto the next one")
                    break

        if k != 1:
            print("From PINTEREST: ", end='')
            #Downloading image
            try:
                download_image(imageURL, 'pin_', folder_name, i)
                print(f"Downloaded element {i} out of {len_containers+1} total. URL: {imageURL}")
            except:
                print("Couldn't download an image %s, continuing downloading the next one"%(i))

        driver.back()
        time.sleep(1)


def gg_search(driver, keyword, folder_name):
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://images.google.com/")
    inp = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    inp.send_keys(keyword,Keys.RETURN)

    # search_URL = "https://www.google.com/search?q=nh%C3%A0+th%E1%BB%9D+con+g%C3%A0&tbm=isch&ved=2ahUKEwjO-rW_xvv6AhUbx4sBHe9YB_oQ2-cCegQIABAA&oq=nha+tho+con+ga&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBwgAEIAEEBgyBwgAEIAEEBg6BAgAEEM6CAgAEIAEELEDOgUIABCxAzoICAAQsQMQgwE6BwgAEIAEEAM6CwgAEIAEELEDEIMBOgYIABAIEB46BAgAEB5Q7QtYwEJgplJoDXAAeACAAeABiAGRFZIBBjMuMTMuM5gBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=QO1XY87aHpuOr7wP77Gd0A8"
    # driver.get(search_URL)


    #Scrolling all the way up
    scroll(driver, 3)

    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
    containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"} )
    len_containers = len(containers)

    print(f"Found {len(containers)} image containers in GOOGLE")
    time.sleep(2)
    # driver.execute_script("window.scrollTo(0,0);")
    for i in range(1, len_containers+1):
        if i % 25 == 0:
            continue

        xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)
        previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
        previewImageElement = driver.find_element(By.XPATH, previewImageXPath)
        previewImageURL = previewImageElement.get_attribute("src")
        driver.find_element(By.XPATH,xPath).click()

        # wait for loading high resolution
        time.sleep(2)
        timeStarted = time.time()
        while True:
            imageElement = driver.find_element(By.XPATH,"""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img""")
            imageURL= imageElement.get_attribute('src')

            if imageURL != previewImageURL: # found a high resolution image
                break
            else:
                #making a timeout if the full res image can't be loaded
                currentTime = time.time()
                if currentTime - timeStarted > 15:
                    print("Timeout! Will download a lower resolution image and move onto the next one")
                    break

        #Downloading image
        print("From GOOGLE: ", end='')
        try:
            download_image(imageURL, 'gg_', folder_name, i)
            print(f"Downloaded element {i} out of {len_containers+1} total. URL: {imageURL}")
        except:
            print("Couldn't download an image %s, continuing downloading the next one"%(i))

def download(id, driver, keyword, folder_name):
    if id == 1:
        gg_search(driver, keyword, folder_name)
    elif id == 2:
        pin_search(driver, keyword, folder_name)