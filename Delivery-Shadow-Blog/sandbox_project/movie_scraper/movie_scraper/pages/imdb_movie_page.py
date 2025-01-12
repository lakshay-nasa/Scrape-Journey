from web_poet.pages import WebPage
from movie_scraper.items import MovieItem
import json


class MovieListPage(WebPage):
    def to_items(self):
        script_data = self.css('#__NEXT_DATA__::text').get()
        if script_data:
            json_data = json.loads(script_data)
            movies_data = json_data['props']['pageProps']['pageData']['chartTitles']['edges']

            for movie in movies_data:
                # yield MovieItem(
                    title=movie['node']['titleText']['text'],
                    year=movie['node']['releaseYear']['year'],
                    rating=movie['node']['ratingsSummary']['aggregateRating'],
                    # rank=movie['currentRank'],
                    # id=movie['node']['id'],
                    # original_title=movie['node']['originalTitleText']['text'],
                    # votes=movie['node']['ratingsSummary']['voteCount'],
                    # genres=[genre['genre']['text'] for genre in movie['node']['titleGenres']['genres']],
                    # plot=movie['node']['plot']['plotText']['plainText'],
                    # poster_url=movie['node']['primaryImage']['url'],
                    # )

                    yield MovieItem(title=title, year=year, rating=rating)
