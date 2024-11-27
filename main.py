# Importing Image module from PIL package 
from PIL import Image 
import PIL 

print(":: Welcome to Universal Image Converter :: - Harsh Raj Singhania")

# creating a image object (main image) 
im1 = Image.open(input("Enter full path of the image (with extension): "))

# Saving the image with desired extension
im1.save(input("Enter full path of NEW image (with desired extension): ")) 

print("Image Conversion Success!")
input("")