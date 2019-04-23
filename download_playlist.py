import argparse

from pytube import Playlist


def download_playlist(playlist_url, location):
    pl = Playlist(playlist_url)
    pl.download_all(location)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_url", type=str, help="URL of playlist to download.")
    parser.add_argument("location", type=str, help="Location where to place the downloads.")
    args = parser.parse_args()
    download_playlist(args.playlist_url, args.location)
