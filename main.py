import numpy
import cv2
from matplotlib import pyplot
import utils    # 噪声函数及滤波器

SNR = 0.8
rawImg = cv2.imread("D:\Picture\i\sp.jpg")
noiseImg = utils.addSaltPepper(rawImg, SNR)

cv2.imshow("rawImg", rawImg)
cv2.imshow("noiseImg", noiseImg)
cv2.waitKey(0)
