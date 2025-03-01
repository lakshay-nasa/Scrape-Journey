from scrapy import Request, Spider


class QuotesToScrapeComScrollBrowserSpider(Spider):
    name = "quotes_toscrape_scroll_browser"

    def start_requests(self):
        yield Request(
            "http://quotes.toscrape.com/scroll",
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                    "actions": [
                        {
                            "action": "scrollBottom",
                        }
                    ],
                },
            },
        )

    def parse(self, response):
        with open("debug.html", "w") as f:
            f.write(response.text)  
        for quote in response.css(".quote"):
            item = {
            "author": quote.css(".author::text").get(),
            "tags": quote.css(".tag::text").getall(),
            "text": quote.css(".text::text").get()[1:-1],
            }
            self.logger.info(item)  # Log each scraped item
            yield item