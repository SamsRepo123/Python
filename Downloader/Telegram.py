## MODULES REQUIRED ##
# telethon
# tqdm
from telethon.sync import TelegramClient, events
from tqdm import  tqdm
import os

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
print ("demo api id: 1845748")
api_id = int(input("Enter your api id: "))
print ("demo api hash: '968egc0f6ee8372f6a3e485ffe48662e'")
api_hash = str(input("Enter your api hash: "))
Channel_name = str(input("Enter name of Telegram channel from where you want to download: "))
path = str(input("Enter location where you want to save files: "))
n = int(input("Enter how many files you want to download: \n "
              "0 for all: "))
if(n == 0):
    n=99999
else:
    n==n

print(api_id,api_hash)
with TelegramClient('name', api_id, api_hash) as client:
    messages = client.get_messages(Channel_name, limit=n) #limit defaults to 1
    for msg in tqdm(messages):
        msg.download_media(file=os.path.join('media', path))


