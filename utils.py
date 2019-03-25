import numpy

# 添加椒盐噪声
# 传入参数为原始图片及信噪比
# random时0代表不处理，1代表盐噪声，2代表椒噪声，椒、盐噪声比例相同
def addSaltPepper(rawImg, SNR):
    noiseImg = rawImg.copy()
    row, col, channel = noiseImg.shape
    mask = numpy.random.choice((0, 1, 2), size=(row, col), replace=True, p=[SNR, (1 - SNR) / 2., (1 - SNR) / 2.])
    noiseImg[mask == 1] = [255, 255, 255]
    noiseImg[mask == 2] = [0, 0, 0]

    return noiseImg


# def arithmeticMeanFilter(noiseImg, maskSize):
#     processedImg = noiseImg.copy()
#     return processedImg