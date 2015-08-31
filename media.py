class Movie:
    """Class for encapsulating the details of a movie."""

    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 lead_actors, release_date, story_line):
        """Constructor of the Movie class.

        Args:
            title (str): The title of the movie.
            poster_image_url (str): A URL pointing to the poster image of
                the movie.
            trailer_youtube_url (str): A URL pointing to the YouTube trailer
                of the movie.
            lead_actors (list[str]): A list of lead actors of the movie.
            release_date (date): The release date of the movie.
            story_line (str): A brief story line of the movie.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.lead_actors = lead_actors
        self.release_date = release_date
        self.story_line = story_line
