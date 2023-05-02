import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class WineSpider(scrapy.Spider):
    name = 'wine'
    start_urls = ['https://www.wineonline.ca/wine-cellar.html']

    def parse(self, response):
        for products in response.css('div.category-products-grid.product-grid-configurable'):
            yield {
                'name': products.css('h2.product-name>a').attrib['title'],
                'price':products.css('span.price::text').get(),
                'link':products.css('h2.product-name>a').attrib['href']
            }

        next_page = response.css('a.next.i-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


       
