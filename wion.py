import feedparser
from dateutil import parser
from PIL import Image
import requests
import urllib.request

# url="https://cdn.wionews.com/images/wion-logo.png"
# con=requests.get('https://cdn.wionews.com/images/wion-logo.png',"sources.png")

con=urllib.request.urlretrieve('https://cdn.wionews.com/images/wion-logo.png','sources.png')

img=Image.open('sources.png')
img.show()







url='https://www.wionews.com/feeds/world/rss.xml'
con=feedparser.parse(url)
# print(con)

# 0 value given for first value, under square bracket it is not used to parse the feed, to solve we implemented new variable under that it will get the value
# published=con.entries[0].published
# dt=parser.parse(published)
# print(published)
# print(dt) # that is timezone aware
# print(dt.utcoffset()) # time zone of time
# print(dt.astimezone(tz.tzutc())) # that is timezone aware as UTC


i=0
for data in con.entries:
    # for getting time
    published=con.entries[i].published
    dt=parser.parse(published)
    print("Time:",published)
    i=i+1
    print("Title:",data.title)
    print("Description:",data.description)
    print("Link:",data.link)
    print()









# for multiple websites

# import feedparser
# from dateutil import parser
# from PIL import Image
# import urllib.request

# con=urllib.request.urlretrieve('https://cdn.wionews.com/images/wion-logo.png','sources.png')

# img=Image.open('sources.png')
# img.show()
# import time
# time.sleep(20)
# import os
# # close the photo window
# os.system("TASKKILL /F /IM Microsoft.Photos.exe")


# lst=['https://www.wionews.com/feeds/south-asia/rss.xml',
# 'https://www.wionews.com/feeds/world/rss.xml',
# 'https://www.wionews.com/feeds/business-economy/rss.xml',
# 'https://www.wionews.com/feeds/cricket/rss.xml',
# 'https://www.wionews.com/feeds/football/rss.xml',
# 'https://www.wionews.com/feeds/sports/rss.xml',
# 'https://www.wionews.com/feeds/science-technology/rss.xml',
# 'https://www.wionews.com/feeds/opinions-0/rss.xml',
# 'https://www.wionews.com/feeds/india-news/rss.xml',
# 'https://www.wionews.com/feeds/entertainment/rss.xml']



# print("1. South Asia")
# print("2. World")
# print("3. Business & Economy")
# print("4. Cricket")
# print("5. Football")
# print("6. Sports")
# print("7. Science & Technology")
# print("8. Opinions")
# print("9. India News")
# print("10. Entertainment")

# inputt=int(input("Enter the Choice: "))
# # sel=inputt-1
# sels=lst[inputt-1]
# # print(sel,sels)

# url=f'{sels}'
# print(url)
# con=feedparser.parse(url)

# i=0
# for data in con.entries:
#     # for getting time
#     published=con.entries[i].published
#     dt=parser.parse(published)
#     print("Time:",published)
#     i=i+1
#     print("Title:",data.title)
#     print("Description:",data.description)
#     print("Link:",data.link)
#     print()

