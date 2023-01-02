from lyricsgenius import Genius
import pandas as pd

token = "aYY9zAk_snRYcs1ZIpOPkTUgVgU9lsiLWUyaggdex4M8m5JqiYiI1HqJL3WCVEfy" #access key from genius
genius = Genius(
    token, skip_non_songs=True, excluded_terms=["Remix", "Live", "feat.", "with"], timeout=15
) #initialize class to scrape songs, try to skip non songs and exclude songs
# with "remix", "feat", "with" or "live" in title. 
# Try for 15 seconds before giving up on scraping

def get_text_from_artist(artist: str, max_songs=5):
    """Return dictionary of information about an artist's most popular songs

    Args:
        artist (str): name of artist
        max_songs (int, optional): Number of songs to scrape from each artist. Defaults to 5.

    Returns:
        list: list of dictionaries
    """    
    artist = genius.search_artist(artist, max_songs=max_songs, get_full_info=False)
    return [
        {"artist": artist.name, "song": song.title, "lyrics": song.lyrics}
        for song in artist.songs
    ]

empty_list = [] #initialize list to save the data

list_of_artists = ["Meghan Trainor", "Justin Timberlake", "Justin Bieber", "Beyonce", "Taylor Swift", "Bruno Mars", "Lizzo", "Carly Rae Jepsen", "Ariana Grande", "Katy Perry", "Harry Styles", "Jason Derulo", "Neyo", "Dua Lipa", "Mabel", "One Direction", "Spice Girls", "Flo Rida", "Lizzo", "OneRepublic", "Ed Sheeran", "Jonas Brother", "Shawn Mendes", "DNCE", "Lady Gaga"] #list of artists to s crape

for artist in list_of_artists: # loop over artists
    new_list_of_info = get_text_from_artist(artist = artist, max_songs = 4) #use previously defined function
    empty_list.extend(new_list_of_info) # extend the list with the new data
df = pd.DataFrame(empty_list) # make a dataframe from the scraped data
df.to_csv("C:/Users/julie/OneDrive/Dokumenter/Uni stuff/NLP/NLP_Exam/lyrics_25.csv", index = False)
