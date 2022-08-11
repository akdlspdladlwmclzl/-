#from tkinter import X
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
'''
x = np.array([5, 10, 15])
y = np.array([10, 20, 15])
plt.plot(x, y, 'b-o', label='Data1')
plt.ylabel('Y axis')
plt.ylabel('X axis')
plt.legend()
plt.show()
'''
'''
##2.라인 그래프 생성하기 ##
x = np.linspace(0,2,100)
y1 = 0.5 * x
y2 = 0.5 * x**2
y3 = 0.5 * x**3

plt.plot(x, y1, label="linear")
plt.plot(x, y2, label="quadratic")
plt.plot(x, y3, label="cubic")

plt.legend()
plt.show()
'''

## BGR & RGB ##
# 1. 이미지 불러오기
image = cv.imread('lmk.jpg')

# 2. BGR
plt.figure()
plt.imshow(image)
plt.title("Original")
#plt.show()

# 3. RGB
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
plt.figure()
plt.imshow(rgb)
plt.title("rgb")
#plt.show()

# 4. Gray
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray)
plt.title("gray")
#plt.show()

# 5. Convert to the Gray
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title("gray")
#plt.show()

#blur
blur = cv.blur(image,(50,50))
blur = cv.cvtColor(blur,cv.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(rgb)
plt.title("rgb")
plt.subplot(122)
plt.imshow(blur)
plt.title("Blur")
#plt.show()

# 7. Edge Detection
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title("gray")
#plt.show()

edges = cv.Canny(gray, 100, 200)
plt.subplot(121)
plt.imshow(gray)
plt.title("Gray")
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.show()
