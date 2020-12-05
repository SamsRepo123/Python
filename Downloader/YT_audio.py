## MODULES REQUIRED ##
# pafy
# youtube-dl

import pafy
url = input("Enter a youtube link for which you want to download audio: ")  # Youtube link
video = pafy.new(str(url))
bestaudio = video.getbestaudio()
bestaudio.download()