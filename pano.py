import cv2
from cv2 import Stitcher
import numpy as np
import os

root = './streetview/'
root_dir = []
for i in os.listdir(root):
    root_dir.append(root + i)

if './streetview/.DS_Store' in root_dir:
    root_dir.remove('./streetview/.DS_Store')

image_name = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
n = 0
for i in root_dir:
    n = n + 1
    print('正在拼接第{}个坐标的图片, 坐标为{}'.format(n, os.listdir(root)[root_dir.index(i)]))
    img = []
    for image in image_name:
        # print(i + '/' + image)
        img.append(cv2.imread(i + '/' + image))
    # (_result, pano) = stitcher.stitch((img[5], img[4], img[3], img[2], img[1], img[0]))
    (_result, pano) = stitcher.stitch((img[0], img[1], img[2], img[3], img[4], img[5]))
    if pano is None:
        # (_result, pano) = stitcher.stitch((img[0], img[1], img[2], img[3], img[4], img[5]))
        (_result, pano) = stitcher.stitch((img[5], img[4], img[3], img[2], img[1], img[0]))
        if pano is None:
            continue
    # cv2.imwrite(i + '/' + '{}.png'.format('pano1'), pano)
    cv2.imwrite('./pano' + '/' + '{}.png'.format(os.listdir(root)[root_dir.index(i)]), pano)
    




# stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
# (_result, pano) = stitcher.stitch((img1, img2, img3, img4, img5, img6))
# cv2.imshow('pano',pano)
# cv2.imwrite('./streetview/loc_33.96331,-118.2629199/no.png', pano)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


