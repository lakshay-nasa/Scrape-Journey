import scrapy


class QuoteHawkSpider(scrapy.Spider):
    name = "quote_hawk"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        pass
