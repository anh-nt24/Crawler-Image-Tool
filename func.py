import os
from PIL import Image
import requests
import time
def rename(id, dir, folder):
    dir = os.path.join(dir,folder)
    os.chdir(dir)
    files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    n=1
    for i in files:
        if i.endswith('.jpg'):
            os.system(f"mv {i} {id}_{n}.jpg")
        n += 1
    os.chdir('..')

def png2jpg(dir):
    for i in os.listdir(dir):
        if i.lower().endswith('.png') or i.lower().endswith('.jpeg') or i.endswith('JPG'):
            # if (i.i.lower().endswith('.jpeg')):
            #     print(i)
            name = i.split('.')[0]
            img = Image.open(dir + '/' + i).convert('RGB')
            if img:
                img.save(f'{dir}/{name}.jpg')
                os.chdir(dir)
                os.system(f'rm -rf {i}')
                os.chdir('..')

def download_image(url, id, folder_name, num):
    # write an image to file
    extension = url.split('.')[-1]
    response = requests.get(url)
    if response.status_code==200: # response successfully
        with open(os.path.join(folder_name, id + str(num) + '.' + extension), 'wb') as file:
            file.write(response.content)

def scroll(driver, n):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    return new_height


def split(dir, folder, weights=(0.9,0.1)):
    numfiles = len(os.listdir(folder))
    train = int(numfiles*weights[0])
    test = numfiles - train

    print(f'total: {numfiles}, train: {train}, test: {test}')
    
    # come in train and create folder
    os.chdir(os.path.join(dir,'train'))
    try:
        os.mkdir(f'{folder}')
    except:
        pass

    os.chdir(os.path.join(dir,'test'))
    try:
        os.mkdir(f'{folder}')
    except:
        pass

    # come in the folder containing downloaded images
    os.chdir(os.path.join(dir, folder))
    i = 0
    for f in os.listdir(os.getcwd()): 
        if i >= train:
            break
        if os.path.isfile(f):
            os.system(f'mv {f} ../train/{folder}')
            i+=1

    i = 0
    for f in os.listdir(os.getcwd()):
        if i >= test:
            break
        if os.path.isfile(f):
            os.system(f' mv {f} ../test/{folder}')
            i+=1
    print("Done")
    os.chdir('..')