# download-youtube-playlists
Download video playlists from Youtube as `mp3`.

## Installation

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### How to run example
Just replace the URL in `download_playlist.py` and run it.
You will get a new folder with the name of the playlist and all the videos in it in both mp4 and mp3 format.

### Gotchas
Make sure the playlist is public or unlisted, if it's private it won't work.