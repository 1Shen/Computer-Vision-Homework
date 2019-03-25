import numpy
import cv2
from matplotlib import pyplot
import utils    # 噪声函数及滤波器

rawImg = cv2.imread("D:\Picture\i\sp.jpg")  # 图片路径
cv2.imshow("rawImg", rawImg)

SNR = 0.95
noiseImg = utils.addSaltPepper(rawImg, SNR)
cv2.imshow("noiseImg", noiseImg)

# meanImg = utils.meanFilter(noiseImg, 3)
# cv2.imshow("meanImg", meanImg)


cv2.waitKey(0)
