import webbrowser

class Video():
    """Parent class for TvShow() and Movie()"""

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class TvShow(Video):
    """Video child class with season, episode, e.g. vars. Inherits title and duration."""

    def __init__(self, title, season, episode, tv_station):
        Video.__init__(self, title)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        pass

class Movie(Video):
    """Video child class with storyline, trailer link, e.g vars. Inherits title and duration."""

    VALID_RATINGS = ["G", "PG", "R", "PG-13"]

    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url, duration, rating):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer)