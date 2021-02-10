from PIL import Image
import os

colorPath = '../../Desktop/未命名文件夹/'
savePath = '../../Desktop/1/'
for imageName in os.listdir(colorPath):
    print('正在转换', imageName)
    im = Image.open(os.path.join(colorPath, imageName)).convert('L')
    im.save(os.path.join(savePath, imageName))
