import os
import shutil
from mutagen import File

music_directory = "/home/fuck/Personal/Music"

for filename in os.listdir(music_directory):
    filepath = os.path.join(music_directory, filename)
    try:
        audio = File(filepath)
        artist = audio.tags.get("artist", ["Unknown"])[0]
        album = audio.tags.get("album", ["Unknown"])[0]
        artist_directory = os.path.join(music_directory, artist)
        if not os.path.exists(artist_directory):
            os.makedirs(artist_directory)
        album_directory = os.path.join(artist_directory, album)
        if not os.path.exists(album_directory):
            os.makedirs(album_directory)
        shutil.move(filepath, album_directory)
        print(f"Moved '{filename}' to '{album_directory}'")
    except Exception as e:
        print(f"Error processing '{filename}': {e}")

