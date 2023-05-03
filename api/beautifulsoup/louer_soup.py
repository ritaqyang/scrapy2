from bs4 import BeautifulSoup
import requests

r = requests.get('https://api.scrapingdog.com/scrape?api_key=6450247bd9ac1c06d00dbf8f&url=https://louer.ca/en/montreal?gclid=CjwKCAjwjMiiBhA4EiwAZe6jQzUI1NmRi44f4JJ58zS59X9md8kUpKgkdEq733wo0P2tdX_SXrU29BoCDSUQAvD_BwE')

#r = requests.get('https://api.scrapingdog.com/scrape?api_key=6450247bd9ac1c06d00dbf8f&url=https://www.wineonline.ca/wine-cellar.html')
soup = BeautifulSoup(r.text,'html.parser')
#print(r.text)
#all_listings = soup.find_all("div",{"class":"r-listing-card-v r-listing-card-v--with-title r-listing-card-v--with-carousel"})
all_listings = soup.find_all("div",{"class":"q-intersection"})
print(all_listings)

u = list()
for i in range(0, len(all_listings)):
	l["title"]= all_listings[i].text.replace("\n","")
	u.append(l)
	l ={}
print({"Titles":u})


