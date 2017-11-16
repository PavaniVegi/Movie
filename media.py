import webbrowser


# define movie class and it properties
class Movie():  
    """ Movie class consists the structure of object """
    def __init__(self, movie_title, movie_storyline, 
                 poster_img, trailer_youtuber_url):
        """constructer of movie class defines all the key variables"""
        """in Movie class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtuber_url

    def show_trailer(self):
        """on call of show_trailer method open's url in web browser"""
        webbrowser.open(self.trailer_youtube_url)
