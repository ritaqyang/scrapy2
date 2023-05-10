import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class LePageSpider(scrapy.Spider):
    name = 'LP'
    start_urls = ['https://www.royallepage.ca/en/qc/montreal/properties/1/']

    def parse(self, response):
        for products in response.css('div.card.card--listing-card.js-listing.js-property-details'):
            yield {
                'address1': products.css('div.card__body>address>a::text').get(),
                'address2':products.css('div.card__body>address::text').get(),
                'link':products.css('div.card__body>address>a').attrib['href'],
                'price':products.css('span.title--h3.price>span::text').get(),
            }

        next_page = response.css('div.paginator__inner>div>a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


       
