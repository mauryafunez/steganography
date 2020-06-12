#import cv module to be able to import images
from PIL import Image

#* is not the best, but for simplicity use it for now.
from functions import *
import numpy

#Funtion to import image and turn it into grayscale
img_vals = image_grayscale('saturn.png')

#View the new image
view_Image(img_vals)

#What text do we want to encrypt?
print('What message would you like to encrypt?')
text_msg = input()

#Encrypt message in the image
encrypt_img = encrypt_text(img_vals, text_msg)

decrypt_img(encrypt_img)
