## MODULES REQUIRED ##
# pafy
# youtube-dl

import pafy
url = input("Enter a youtube link for which you want to download: ")  # Youtube link
video = pafy.new(str(url))
streams = video.streams
for i in streams:
    print(i)
best = video.getbest()
print(best.resolution, best.extension)
best.download()
print("Video Download Complete!")