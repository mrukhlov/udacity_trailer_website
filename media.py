import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class TvShow(Video):
    def __init__(self, title, season, episode, tv_station):
        Video.__init__(self, title)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        pass

class Movie(Video):
    """readme for movie class"""

    VALID_RATINGS = ["G", "PG", "R", "PG-13"]

    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url, duration, rating):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer)