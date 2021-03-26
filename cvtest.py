import cv2
from numpy import asarray

img = cv2.imread("logo.png")
gray = cv2.imread('logo.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.imshow('gray',gray)

data = asarray(img)
print(data)

#Wait for any key before image disappears
cv2.waitKey(0)
cv2.destroyAllWindows()