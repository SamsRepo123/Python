from PIL import Image, ImageFilter  # imports the library

path = str(input("Enter location of image you want to blur: "))
original = Image.open(path) # load an image from the hard drive
blurred = original.filter(ImageFilter.BLUR) # blur the image
# display both images
original.show()     # original image
blurred.show()       # blur image