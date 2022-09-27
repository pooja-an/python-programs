'''
Prgram to download YouTube audio
'''

import pytube

#url = input("Enter video URL: ")

## Create a list of all youtube links to download
urls = ['']

## Set the path of a folder you wish to download to
path = ""

for url in urls:
    pytube.YouTube(url).streams.filter(only_audio=True).first().download(path)

