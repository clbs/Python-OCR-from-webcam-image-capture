import time
import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
tessdata_dir_config = '--psm 6 --tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to include double quotes around the dir path.
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)  
return_value, image = camera.read()
cv2.imwrite("opencv.jpg", image)
del(camera) 
im = Image.open("opencv.jpg")  
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(1)
im = im.convert('1')
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('opencv.jpg'),lang='eng' , config=tessdata_dir_config)
print(text)


