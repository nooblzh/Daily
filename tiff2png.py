from PIL import Image
import os
import numpy
imagesDirectory = '../../Desktop/test'
distDirectory = '../../Desktop/1/'
for imageName in os.listdir(imagesDirectory):
    print('正在转换', imageName)
    imagePath = os.path.join(imagesDirectory, imageName)
    image = Image.open(imagePath)
    distImagePath = os.path.join(distDirectory, imageName[:-5]+'.png')
    image.save(distImagePath)
