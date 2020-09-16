import requests
import json
from pprint import pprint


#pprint(movie_list)

def main():
    user_input = input("Vilken film vill du veta mer om? ")
    movie = requests.get("http://www.omdbapi.com/", params={"t": f"{user_input}", "apikey": "9f6d550c"})
    movie_list = movie.json()

    years = movie_list['Year']
    director = movie_list['Director']
    actors = movie_list['Actors']
    imdb = movie_list['imdbRating']
    award = movie_list['Awards']
    length = movie_list['Runtime']

    description = f"""    *** Resultat från OMDB! ***\n
      {user_input} ({years}) regisserades av {director}.
Skådisar:      {actors}
IMDB betyg:    {imdb}
Awards:        {award}
Längd:         {length}"""

    print(description)

main()