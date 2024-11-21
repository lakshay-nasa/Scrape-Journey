import scrapy


class BooksHawkSpider(scrapy.Spider):
    name = "books_hawk"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'availability': book.css('p.instock.availability::text').re_first(r'\w+'),
                'category': response.css('ul.breadcrumb li:nth-child(3) a::text').get(),
            }
        
        # Move to Next page
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
