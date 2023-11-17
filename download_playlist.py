import os

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from pytube import Playlist
from slugify import slugify

PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLalP5H2VpMn5YrAX0zJpCG9RElDJ3roQM'

if __name__ == "__main__":
    p = Playlist(PLAYLIST_URL)
    print(f'Downloading playlist: {p.title}')
    for video in p.videos:
        try:
            audio_streams = video.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc()
        except Exception as e:
            print(f'Cannot download {video.title}. Error: {e}')
            continue

        folder = slugify(p.title)
        filename = f'{slugify(video.title)}'
        full_path = os.path.join(folder, filename)

        # if file is already downloaded, skip
        if os.path.exists(f'{full_path}.mp4'):
            print(f'Skipping {full_path}.mp4 as it already exists')
            continue

        print(f'Downloading: {video.title}, abr={audio_streams[0].abr}')
        audio_streams[0].download(output_path=folder, filename=f"{filename}.mp4")
        print(f'Downloaded: {full_path}.mp4')

        mp4_file = f'{full_path}.mp4'
        mp3_file = f'{full_path}.mp3'

        print(f'Converting: {mp4_file} to {mp3_file}')
        ffmpeg_extract_audio(mp4_file, mp3_file)
        print(f'Converted: {mp4_file} to {mp3_file}')

    print('\n')
