# Class for encapsulating the details of a movie
class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url, lead_actors, release_date, story_line):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.lead_actors = lead_actors
        self.release_date = release_date
        self.story_line = story_line
