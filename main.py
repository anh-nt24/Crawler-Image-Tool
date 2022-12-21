import os
import time
import threading
from selenium import webdriver
from download import *
from func import *

global exitFlag, n
exitFlag = 0
kws = []
folders = []

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, driver):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.driver = driver

    def run(self):
        for i in range(self.counter):
            print(f"Starting downloading {self.name}")
            task_thread(self.threadID, self.name, self.driver, i)
            print(f"Finish downloading {self.name}")
        self.driver.close()

def task_thread(threadID, threadName, driver, i):
    if exitFlag:
        threadName.exit()
    try:
        download(threadID, driver, kws[i], folders[i])
    except Exception as e:
        print("ID: ",threadID, e)
        print("Stop downloading due to some trouble...")

def main():
    n = int(input("Number of keywords: "))
    for i in range(n):
        kws.append(input(f"Enter keyword {i+1}: "))
        #creating a directory to save images
        folders.append(input(f"Enter folder name {i+1}: "))
        if not os.path.isdir(folders[-1]):
            os.makedirs(folders[-1])

    driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Create threads
    thread1 = myThread(1, "On Google Image", n, driver1)
    thread2 = myThread(2, "On Pinterest", n, driver2)

    # Start threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Done")

if __name__ == '__main__':
    # main()  # will be COMMENTED to stop running after downloading

    # # 1. now filter images and remove some if nescessary

    # MARKED CODE. Uncomment them when you have finished downloading the images
    # # 2. convert PNG to JPG
    folders = input("Enter folders name (separated by the ', '): ").split(', ')
    for i in folders:
        # print(os.listdir(os.getcwd()))
        png2jpg(f'./{i}')

    # 3. rename it in order and split the dataset
    if not os.path.isdir(os.path.join(os.getcwd(),'train')):
        os.system('mkdir train test')

    for i in folders:
        rename('tor', os.getcwd(), i)
        split(os.getcwd(), i)
        os.system(f'rm -rf {i}')



############################### THINGS TO NOTE ##############################
#                           Instruction for use                             #
# I/ About browser:                                                         #
#       - 1: Google image seach:                                            #
#           Always in stable condition                                      #
#       - 2: Pinterest:                                                     #
#           Dependent on your network and                                   #
#           browser that might cause some errors                            #
#                                                                           #
# II/ When running, you will be asked for:                                  #
#       - 1: Number of keywords: enter as much as you like.                 #
#               Each will be searched in both engines                       #
#       - 2: Keyword to search: Vietnamese language accepted                #
#       - 3: Folder name: where to save your downloaded images              #
#                                                                           #
# III/ In the process of downloading:                                       #
#    If having some problems like cannot download, a crash program, etc     #
#    -> FIX it if you can or note it and NOTICE everyone for the error(s)   #
#                                                                           #
# IV/ After downloading:                                                    #
#       - Add images you have collected to their correct folder             #
#       - Checking the images, remove some unsatisfactory photo             #
#       - Comment the main function                                         #
#       - Uncomment all the marked code above to:                           #
#               + convert to .jpg files                                     #
#               + rename all the images                                     #
#               + split the dataset                                         #
#         -> In this step, you will be required to                          #
#             input the folders name and then all are worked automatically  #
# The folder structure after this step should be:                           #
#      ./                                                                   #
#       |___ test                                                           #
#           |___ folder 1 - containing destination images 1. e.g: Ha Long   #
#           |___ folder 2 - containing destination images 2                 #
#           |___ folder n                                                   #
#       |___ train                                                          #
#           |___ folder 1                                                   #
#           |___ folder 2                                                   #
#           |___ folder n                                                   #
# Then, when all are perfect, zip all folders of images and SEND ME.        #
#                            Thank you!                                     #
#                                                                           #
#############################################################################