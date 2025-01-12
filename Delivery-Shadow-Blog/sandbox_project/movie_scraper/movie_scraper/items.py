# from dataclasses import dataclass
# from typing import List

# @dataclass
# class MovieItem:
#     title: str
#     year: int
#     rating: float
#     # rank: int
#     # id: str
#     # original_title: str
#     # votes: int
#     # genres: list
#     # plot: str
#     # poster_url: str

import scrapy

class MovieItem(scrapy.Item):
    title = scrapy.Field()  
    year = scrapy.Field()   
    rating = scrapy.Field()  
