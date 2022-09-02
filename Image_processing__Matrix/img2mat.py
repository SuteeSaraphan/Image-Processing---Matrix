# Import the necessary libraries
from PIL import Image
from numpy import asarray
import numpy as np
import os
import sys
from scipy.signal import convolve2d
from skimage.io import imshow, imread,imsave

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#load image
img = Image.open((resource_path("Sutee.jpg")))
#image convert to black/white
imgGray = img.convert('L')
#save image to test_gray.png
imgGray.save('test_gray.png')
#load new image black/white
imgg = Image.open((resource_path("test_gray.png")))
#convert image to Matrix array
numpydata = asarray(imgg)
#convert Matrix array to Matrix
m = np.matrix(numpydata)
#Display Matrix
print("Matrix Form Original Image")
print(m)

# Gaussian Blur
gaussian = (1 / 16.0) * np.array([[1., 2., 1.],
                                  [2., 4., 2.],
                                  [1., 2., 1.]])
# Box blur                    
box = (1 / 9.0) * np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])

# Identity
identity = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

def multi_convolver(image, kernel, iterations):
    for i in range(iterations):
        image = convolve2d(image, kernel, 'same', boundary = 'fill',fillvalue = 0)
    return image

con = multi_convolver(imgg, gaussian, 1)
con3 = multi_convolver(imgg, box, 1)
con4 = multi_convolver(imgg, identity, 1)

imsave('a1.jpg',con)
imsave('a3.png',con3)
imsave('a4.jpg',con4)
print("")


print("Result Box Blur :")
print(con3)
print("")

print("Result Identity Blur :")
print(con4)
print("")

print("Result Gaussian Blur :")
print(con)
print("")

#Link Excel : https://docs.google.com/spreadsheets/d/1MqIbMBwiZOj6_yLksXMgdv9jdnwMDzfeEpMs9v5uhuo/edit?usp=sharing