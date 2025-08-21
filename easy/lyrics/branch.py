import lyricsgenius

genius = lyricsgenius.Genius("YOUR_API_TOKEN")
artist = genius.search_artist("Coldplay", max_songs=3)

    for song in artist.songs:
        print(song.lyrics)