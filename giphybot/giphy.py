import requests

import os


def random(tag=""):
    api_url = "https://api.giphy.com/v1/gifs/random"
    response = requests.get(api_url, params={"api_key": os.environ["GIPHY_KEY"],
                                             "tag": tag})
    gif_url = response.json()["data"]["images"]["fixed_width_downsampled"]["url"]

    return gif_url
