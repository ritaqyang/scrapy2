from bs4 import BeautifulSoup
import requests



r = requests.get('https://api.scrapingdog.com/scrape?api_key=6450247bd9ac1c06d00dbf8f&url=https://www.wineonline.ca/wine-cellar.html')
soup = BeautifulSoup(r.text,'html.parser')

all_listings = soup.find_all("div",{"class":"category-products-grid product-grid-configurable"})

l={}
u = list()
for i in range(0, len(all_listings)):
	l["title"]= all_listings[i].text.replace("\n","")
	u.append(l)
	l ={}
print({"Titles":u})


