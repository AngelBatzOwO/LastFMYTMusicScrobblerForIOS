import time
import os
import pylast
from flask import Flask, request

app = Flask(__name__)

# Set up Last.fm credentials
API_KEY = os.environ["LASTFM_API_KEY"]
API_SECRET = os.environ["LASTFM_API_SECRET"]
USERNAME = os.environ["LASTFM_USERNAME"]
PASSWORD_HASH = os.environ["LASTFM_PASSWORD_HASH"]

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=USERNAME,
    password_hash=PASSWORD_HASH

@app.route("/scrobble", methods=["POST"])
def scrobble():
    data = request.json
    artist = data.get("artist")
    title = data.get("track")
    
    if artist and title:
        try:
            # Log the scrobble to Last.fm
            network.scrobble(artist=artist, title=title, timestamp=int(time.time()))
            return "Scrobbled", 200
        except Exception as e:
            return f"Error: {str(e)}", 500
    return "Missing data", 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)