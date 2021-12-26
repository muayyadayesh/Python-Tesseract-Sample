from PIL import Image
import numpy as Numpy
import cv2
import pytesseract

# Custom config
custom_config = r'--oem 3 --psm 6'

filetoScan = 'sources/toscan_noise.jpeg'
Image = Numpy.array(Image.open(filetoScan))
scannedText = pytesseract.image_to_string(Image, config=custom_config)
# Print text before modifying the noise in the source image
print(scannedText)

# Modifying the noise using OpenCV
original_img = Numpy.zeros((Image.shape[0], Image.shape[1]))
cv2img = cv2.normalize(Image, original_img, 0, 255, cv2.NORM_MINMAX)
cv2img = cv2.threshold(cv2img, 100, 255, cv2.THRESH_BINARY)[1]
cv2img = cv2.GaussianBlur(cv2img, (1, 1), 0)
scannedText = pytesseract.image_to_string(cv2img, config=custom_config)

# Print text after modifying the noise in the source image
print(scannedText)
