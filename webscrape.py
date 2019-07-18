import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Target Website Page
my_url = 'https://www.twitch.tv/speedgaming/videos?filter=archives&sort=time'

#Grab the HTML
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Prse that HTML
soup = BeautifulSoup(page_html, "html.parser")

#Grab Main Page Area
containers = soup.findAll(class_="simplebar-scroll-content")

print (containers)