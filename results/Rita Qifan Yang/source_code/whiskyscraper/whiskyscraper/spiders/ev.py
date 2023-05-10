import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class LePageSpider(scrapy.Spider):
    name = 'ev'
    #start_urls = ['https://montreal.evrealestate.com/inventaire//{}']

    start_urls = ['https://montreal.evrealestate.com/inventaire']
    


    # def start_requests(self):
    #    for x in range(1,103):
    #     url=self.start_urls[0].format(x)
    #     yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for products in response.css('article.rng-featured-property'):
            yield {
                'address1': products.css('div.site-global-container>div>main>section>article>a').attrib['aria-label'],
                'address2':products.css('div.banners>div::text').get(),
                'link': products.css('div.site-global-container>div>main>section>article>a').attrib['href'],
                'price': products.css('span.rng-featured-property-listing-price::text').get()
            }


       
