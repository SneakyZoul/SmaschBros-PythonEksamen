import cv2 as cv
#from imageai.Detection import ObjectDetection as od

import numpy as np
import requests as req
import os as os


url = 'https://smashbros-unofficial-api.vercel.app/api/v1/ultimate/characters?name=mario'
r = req.get(url)
with open('testimage.jpg', 'wb') as outfile:
    outfile.write(r.content)
def showmage(img):
    img = cv.imread('testimage.jpg')
    window_name = 'image'
    cv.imshow(window_name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


hardhatLoc = 'https://api.kuroganehammer.com/api/characters/ThumbnailUrl'

hardhatImages = req.get(hardhatLoc).text
noOfImages = 0

if not os.path.exists('smash'):
    os.makedirs('smash')

for i in hardhatImages.split('\n'):
        r = req.get(i, timeout=0.5)
        file = i.split("/")[-1].split('\r')[0]
        if 'image/JPEG' in r.headers['Content-Type']:
            if len(r.content) > 8192:
                with open('hardhat\\' + file, 'wb') as outfile:
                    outfile.write(r.content)
                    noOfImages += 1
                    print('Success: ' + file)
            else:
                print('Failed: ' + file + ' -- Image too small')
        else:
            print('Failed: ' + file + ' -- Not an image')



print('*********** Download Finished **************')


#if __name__ =='__main__':
   #showmage(outfile)
