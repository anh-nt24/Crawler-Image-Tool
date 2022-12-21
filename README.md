# Image-Crawler-Tool
This tool is used to download images from 2 platforms which are Google Image Search and Pinterest. 

The purpose is for preparing dataset(s) for a computer vision project.

## Requirements:
- Ubuntu 20.04
- Python3.7+
- BeautifulSoup (bs4): 4.11.1
- Selenium: 4.1.3
- PIL: 9.1.0
- Stable internet connection

## Note:
The tool depends on your internet. It may cause some error if the connection is not stable or bad effect on the downloading process.

## Brief description:
Type `python3 main.py` in terminal to run the project. Then, you will be required to enter number of keywords and each keyword you intending to search. 
Next, the tool will find and download images related to the folder whose name is the keyword you entered.  

## How to use:
The instruction is attacked on the main.py file. You can read there again.

```
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
```
