import requests
from dataclasses import dataclass
import datetime
import re
import json
from types import SimpleNamespace

def TweetURLExtractor(text):
    pattern = "(https?://twitter.com/[\w_]{1,15}/status/(\d{,19}))"
    return re.findall(pattern, text)


class TweetURLtoData:
    def __init__(self, id):
        self.url = "https://cdn.syndication.twimg.com/tweet"
        self.params = {
            "features": "tfw_experiments_cookie_expiration:1209600;tfw_horizon_tweet_embed_9555:hte;tfw_space_card:off",
            "id": id,
            "lang": "en"
        }
        self.headers = {
            "content-type": "application/json; charset=utf-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
        self.proxies = {}

    def get(self):
        self.content = json.loads(requests.get(url=self.url, headers=self.headers, params=self.params, proxies=self.proxies).text,object_hook=lambda d: SimpleNamespace(**d))
        self.content.created_at = datetime.datetime.fromisoformat(self.content.created_at.replace("Z", ""))
        return self
