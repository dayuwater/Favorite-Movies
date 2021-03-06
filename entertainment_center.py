'''  The python file to fetch movie data from TheMovieDB API and display them 
in a scaffolded webpage    '''
import requests
import json
import media
import fresh_tomatoes


def get_full_path(path_from_api):
    ''' Convert the poster path from API to the full path '''
    return "http://image.tmdb.org/t/p/w185/"+path_from_api


def get_trailer(movie_id):
    ''' Get the movie trailer url from API '''
    url = "https://api.themoviedb.org/3/movie/"+str(movie_id) \
        + "/videos?api_key="+API_KEY+"&language=en-US"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    # since there are many video links coming out, I will just pick the first
    result_dic = json.loads(response.text)['results'][0]
    youtube_key = result_dic['key']
    return "https://www.youtube.com/watch?v="+youtube_key  
# Enter your API key here
API_KEY = "Your API key here"  

# the connection code for using the API
url = "https://api.themoviedb.org/3/discover/movie?api_key=" + \
      API_KEY+"&include_video=true"
payload = "{}"
response = requests.request("GET", url, data=payload)
# the webpage does not look nice after 9 items
result_dic = json.loads(response.text)['results'][0:9]
movies = []

for item in result_dic:
    # fetch the nessesary data
    title = item['title']
    image_path = item['poster_path']
    overview = item['overview']
    movie_id = item['id']
    # will use this to change the color of the title in the webpage
    vote = item['vote_average'] 
    image_path = get_full_path(image_path)
    trailer_url = get_trailer(movie_id)

    # create the instance of movie class
    new_movie = media.Movie(movie_id, title, overview, 
                            image_path, trailer_url, vote)
    movies.append(new_movie)

fresh_tomatoes.open_movies_page(movies)