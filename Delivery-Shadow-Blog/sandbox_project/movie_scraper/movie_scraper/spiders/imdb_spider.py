import scrapy
from movie_scraper.pages.imdb_movie_page import MovieListPage

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        page = MovieListPage(response)

        # yield from page.to_items()
        for item in page.to_items():
            yield item

        next_page = response.css('a.lister-page-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
