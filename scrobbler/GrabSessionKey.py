import hashlib
import requests

API_KEY = "b4e0b5c9a9c79cd02b1031edd912d697"
API_SECRET = "867825633320317112962faebcc02dc8"

# Replace with the token from the URL after authorization
TOKEN = "AccuZ5_kvaahydOqfGN-EYyOWi7nK7Y3"

# Create API signature
sig_string = f"api_key{API_KEY}methodauth.getSessiontoken{TOKEN}{API_SECRET}"
api_sig = hashlib.md5(sig_string.encode()).hexdigest()

# Make request to get the session key
response = requests.get(
    "https://ws.audioscrobbler.com/2.0/",
    params={
        "method": "auth.getSession",
        "api_key": API_KEY,
        "token": TOKEN,
        "api_sig": api_sig,
        "format": "json",
    },
)

print(response.json())  # Save the `key` from the response
