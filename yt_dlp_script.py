from yt_dlp import YoutubeDL
from pathlib import Path
from tqdm import tqdm
from pathlib import Path
import os

def download_yt_song_mp3(playlist_url, output_dir="music"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "overwrites": False
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def rename_all_songs(songs_path, genre_name):
    for index, mp3_file in enumerate(tqdm(os.listdir(songs_path), desc=f"Renaming all songs in path {songs_path} into {genre_name}.{format}")):
        mp3_file_path = os.path.join(songs_path, mp3_file)
        path = Path(mp3_file_path)
        file_suffix = Path(mp3_file_path).suffix
        path.rename(os.path.join(songs_path, f"{genre_name}.{index:05d}{file_suffix}"))

download_yt_song_mp3(
    "your_yt_playlist_url",
    output_dir="your_folder_path"  
)

rename_all_songs("your_dataset_path", "name")