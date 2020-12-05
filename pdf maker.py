## MODULES REQUIRED ##
# fpdf

from os import listdir
from fpdf import FPDF
path = input("Enter a Location of image folder: ")   # location of images
slash = "//"
path = path.replace("/" , "//")
path += str(slash)
filename = input("Enter name for pdf file: ")
imagelist = listdir(str(path)) # taking all images from folder
imagelist.sort()

pdf = FPDF('P', 'mm', 'A4') # create an A4-size pdf document

x = 0
y = 0
w = 210
h = 297

for image in imagelist:
    pdf.add_page()
    pdf.image(path + image, x, y, w, h)
pdf.output(str(path) + filename + ".pdf", "F")  # location of where you want to save the pdf