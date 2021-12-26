from PIL import Image
import numpy as Numpy
from numpy.lib.type_check import imag
import pytesseract

filetoScan = 'sources/toscan.jpeg'
srcimage = Numpy.array(Image.open(filetoScan))
custom_config = r'--oem 3 --psm 6'

# Print the recognized text
scannedText = pytesseract.image_to_string(srcimage, config=custom_config)


print(scannedText)
