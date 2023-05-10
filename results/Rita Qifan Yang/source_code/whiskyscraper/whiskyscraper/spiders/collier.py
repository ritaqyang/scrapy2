import scrapy
#source tutorial-env/bin/activate
class MySpider(scrapy.Spider):
    name = 'collier'
    start_urls = ['https://www.collierscanada.com/en-ca/properties?gad=1&gclid=CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE#sort=relevancy&f:listingtype=[All%20Listings]&f:recenttransactions=[0]']

    def parse(self, response):
        token = response.css('input[name="__RequestVerificationToken"]::attr(value)').get()
        formdata = {
            '__RequestVerificationToken': token
            
        }
        yield scrapy.FormRequest(url='https://www.collierscanada.com/en-ca/properties?gad=1&gclid=CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE#sort=relevancy&f:listingtype=[All%20Listings]&f:recenttransactions=[0]/submit-form',
                                 formdata=formdata,
                                 callback=self.parse_results)

    def parse_results(self, response):
        # Here, you can access any elements underneath the token
        result = response.css('a.CoveoResultLink.teaser-card__overlay').get()
        yield {'link': result}
