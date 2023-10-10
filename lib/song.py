from collections import Counter

class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name =name
        self.artist =artist
        self.genre =genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        
        

    @classmethod
    def add_song_to_count(cls):
        cls.count +=1

    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.append(genre)
        cls.add_to_genre_count()

    @classmethod
    def add_to_artists(cls,artist):
          cls.artists.append(artist)
          cls.add_to_artisit_count()

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = Counter(cls.genres)
         
    @classmethod
    def add_to_artisit_count(cls):
        cls.artist_count = Counter(cls.artists)
