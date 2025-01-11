import cv2 as cv
import random
import numpy as np
from matplotlib import pyplot as plt

# 属性变换
def attribute(img,brightness=False,contrast=False,saturation=False,
              b=None,
              c=None,
              s=None):
    if type(img) == np.ndarray:
        if brightness == True:
            img = cv.addWeighted(img, 1, img, 0, b)
        if contrast == True:
            img = cv.addWeighted(img, c, img, 0, 1)
        if saturation == True:
            hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
            hsv_img[...,1] = hsv_img[...,1]*s
            img = cv.cvtColor(hsv_img,cv.COLOR_HSV2BGR)
    else:
        pass
    return img

# 阈值
def threshold(img,
              min=None,max=None):
    if type(img) == np.ndarray:
        if len(img.shape)==3:
            img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            _,img = cv.threshold(img,min,max,cv.THRESH_BINARY)
    else:
        pass
    return img

# 噪声
def noise(img,gaussian=False,salt=False,random_=False,
          mean=None,sigma=None,
          salt_rate=None,
          random_rate=None):
    if type(img) == np.ndarray:
        if gaussian == True:
            sigma = random.uniform(sigma,sigma)
            img = img / 255
            noise = np.random.normal(mean, sigma, img.shape)
            gaussian_out = img + noise
            gaussian_out = np.clip(gaussian_out, 0, 1)
            img = np.uint8(gaussian_out*255)
            return img
        elif random_ == True:
            img1 = img.copy()
            rows, cols, _ = img.shape
            num = int(rows * cols * random_rate)
            for i in range(num):
                x = np.random.randint(0, rows)          # 随机生成指定范围的整数
                y = np.random.randint(0, cols)
                img1[x, y, :] = 255
            return img1
        elif salt == True:
            img2 = img.copy()
            height, width = img.shape[0], img.shape[1]  # 获取高度宽度像素值
            num = int(height * width * salt_rate)       # 一个准备加入多少噪声小点
            for i in range(num):
                w = random.randint(0, width - 1)
                h = random.randint(0, height - 1)
                if random.randint(0, 1) == 0:
                    img2[h, w] = 0
                else:
                    img2[h, w] = 255
            return img2
        else:
            pass
    else:
        pass

# 滤波
def filtering(img,mean=False,median=False,Gaussian=False,bilateral=False,
              meanKW=None,meanKH=None,
              medianKS=None,
              GaussianKW=None,GaussianKH=None,GaussianSX=None,GaussianSY=None,
              bilateralD=None,bilateralC=None,bilateralS=None):
    if type(img) == np.ndarray:
        if mean == True:
            img = cv.blur(img,(meanKW,meanKH))                                       # 均值滤波
        if median == True:
            img = cv.medianBlur(img,medianKS)                                        # 中值滤波
        if Gaussian == True:
            img = cv.GaussianBlur(img,(GaussianKW,GaussianKH),sigmaX=GaussianSX,sigmaY=GaussianSY)     # 高斯滤波
        if bilateral == True:
            img = cv.bilateralFilter(img,bilateralD,bilateralC,bilateralS)           # 双边滤波
    else:
        pass
    return img

# 形态学操作
def morphology(img,dilate=False,etch=False,open=False,close=False,
               dilateKS=None,dilateI=None,
               etchKS=None,etchI=None,
               openKS=None,openI=None,
               closeKS=None,closeI=None):
    if type(img) == np.ndarray:
        _,BINARY = cv.threshold(img,127,255,cv.THRESH_BINARY)         
        if dilate == True:
            kernel = np.ones((dilateKS,dilateKS),np.uint8)
            img = cv.dilate(BINARY,kernel,iterations=dilateI)                       # 膨胀
        if etch == True:
            kernel = np.ones((etchKS,etchKS),np.uint8)
            img = cv.erode(BINARY,kernel,iterations=etchI)                          # 腐蚀
        if open == True:
            kernel = np.ones((openKS,openKS),np.uint8)
            img = cv.morphologyEx(BINARY,cv.MORPH_OPEN,kernel,iterations=openI)     # 开运算
        if close == True:
            kernel = np.ones((closeKS,closeKS),np.uint8)
            img = cv.morphologyEx(BINARY,cv.MORPH_CLOSE,kernel,iterations=closeI)   # 闭运算
    else:
        pass
    return img

# 梯度算子
def gradient(img,canny=False,laplacian=False,scharr=False,sobel=False,
             min=None,max=None,
             laplacian_KS=None,
             scharr_XY=None,
             sobel_XY=None,sobel_KS=None):
    if type(img) == np.ndarray:
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        if canny == True:
            img = cv.Canny(img, min, max)
        if laplacian == True:
            img = cv.Laplacian(img, -1, ksize=laplacian_KS)
        if scharr ==True:
            if scharr_XY == "X":
                img = cv.Scharr(img, cv.CV_16S, 1, 0)
                img = cv.convertScaleAbs(img)
            if scharr_XY == "Y":
                img = cv.Scharr(img, cv.CV_16S, 0, 1)
                img = cv.convertScaleAbs(img)
            if scharr_XY == "XY":
                x = cv.Scharr(img, cv.CV_16S, 1, 0)
                y = cv.Scharr(img, cv.CV_16S, 0, 1)
                Scale_absX = cv.convertScaleAbs(x)                          # 格式转换函数
                Scale_absY = cv.convertScaleAbs(y)
                img = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)   # 图像混合
        if sobel == True:
            if sobel_XY == "X":
                img = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=sobel_KS)
                img = cv.convertScaleAbs(img)
            if sobel_XY == "Y":
                img = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=sobel_KS)
                img = cv.convertScaleAbs(img)
            if sobel_XY == "XY":
                x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=sobel_KS)
                y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=sobel_KS)
                Scale_absX = cv.convertScaleAbs(x)  
                Scale_absY = cv.convertScaleAbs(y)
                img = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
    else:
        pass
    return img

# 直方图
def histogram(img):
    if type(img) == np.ndarray:
        if img.shape[2] == 1:
            hist = cv.calcHist([img], [0], None, [256], [0, 256])
            return hist
        if img.shape[2] == 3:
            B,G,R = cv.split(img) 
            hist_B = cv.calcHist([B], [0], None, [256], [0, 256])
            hist_G = cv.calcHist([G], [0], None, [256], [0, 256])
            hist_R = cv.calcHist([R], [0], None, [256], [0, 256])
            return hist_R,hist_G,hist_B
    else:
        pass

# 色彩空间
def colorspace(img,mode=None):
    if type(img) == np.ndarray:

        if mode == "RGB":
            B,G,R = cv.split(img) 
            return cv.cvtColor(R,cv.COLOR_GRAY2RGB),cv.cvtColor(G,cv.COLOR_GRAY2RGB),cv.cvtColor(B,cv.COLOR_GRAY2RGB)
        if mode == "HSV":                                          
            hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)                     
            H,S,V = cv.split(hsv_img)      
            return cv.cvtColor(H,cv.COLOR_GRAY2RGB),cv.cvtColor(S,cv.COLOR_GRAY2RGB),cv.cvtColor(V,cv.COLOR_GRAY2RGB)
        if mode == "GRAY":                                 
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            return cv.cvtColor(gray, cv.COLOR_GRAY2RGB)
    else:
        pass

# 频域转换
def frequency(img):
    if type(img) == np.ndarray:
        if len(img.shape) == 3:
            img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        img = 15*np.log(np.abs(fshift))
        img = np.uint8(img)
        img = cv.cvtColor(img,cv.COLOR_GRAY2RGB)
        img = cv.resize(img,(1000,1000))
    else:
        pass
    return img

if __name__ == "__main__":
    img = cv.imread('D:/BS002/images/panda.jpg',cv.IMREAD_GRAYSCALE)
    cv.imwrite('panda_gray.jpg',img)
    cv.imshow("img",img)
    cv.waitKey(0)