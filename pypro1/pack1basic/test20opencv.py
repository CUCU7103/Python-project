# OpenCv : 다양한 영상/동영상 처리에 사용할 수 있는 오픈소스 라이브러리.

import cv2
from scipy.ndimage import interpolation

img1 = cv2.imread('./abc.jpg') 
cv2.imshow('image test', img1)
cv2.waitKey()
cv2.destroyAllWindows()

img3 = img1 - 50
cv2.imshow('image test', img3)
cv2.waitKey()
cv2.destroyAllWindows()

img5 = cv2.resize(img1,(320,100), interpolation = cv2.INTER_AREA)
cv2.imwrite('./abc2.jpg', img5)
cv2.imshow('test', img5)
cv2.waitKey()
cv2.destroyAllWindows()