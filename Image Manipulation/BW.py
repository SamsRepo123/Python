
from PIL import Image 
path = str(input("Enter location of image: "))
open_image = Image.open(path)
covert_to_bw = open_image.convert("L")
covert_to_bw.show()