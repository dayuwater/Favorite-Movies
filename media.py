import webbrowser

''' 
The Movie class
Stores all the data for a movie
'''
class Movie():
    ''' This class provides a way to store movie related information '''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, mid, movie_title, movie_storyline, poster_image, trailer_youtube,vote):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.mid = mid
        self.vote = vote

   
    def show_trailer(self):
        ''' Open a webbrowser to show the trailer of the movie '''
        webbrowser.open(self.trailer_youtube_url)


    
