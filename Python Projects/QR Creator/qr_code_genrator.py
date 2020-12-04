
##  Modules Reouires   ##
# pypng
# pyqrcode

import pyqrcode
import png
from pyqrcode import QRCode

QRstring =  "https://github.com/SamsRepo123/Python/Python%20Projects/" #paste any url here
url = pyqrcode.create(QRstring)
# Specify the location where you want generate the qr code as output
url.png('X:\\Python\\output\\qr.png', scale = 8)
