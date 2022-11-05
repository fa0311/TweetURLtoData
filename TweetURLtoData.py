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
        self.url = "https://cdn.syndication.twimg.com/tweet-result"
        self.params = {
            "features": "tfw_timeline_list:linktr.ee,tr.ee,terra.com.br,www.linktr.ee,www.tr.ee,www.terra.com.br;tfw_horizon_timeline_12034:treatment;tfw_tweet_edit_backend:on;tfw_refsrc_session:on;tfw_chin_pills_14741:color_icons;tfw_tweet_result_migration_13979:tweet_result;tfw_sensitive_media_interstitial_13963:interstitial;tfw_experiments_cookie_expiration:1209600;tfw_duplicate_scribes_to_settings:on;tfw_video_hls_dynamic_manifests_15082:true_bitrate;tfw_show_blue_verified_badge:off;tfw_related_videos_15128:many_vids;tfw_tweet_edit_frontend:on",
            "id": id,
            "lang": "en"
        }
        
        self.headers = {
            "content-type": "application/json; charset=utf-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }
        self.proxies = {}

    def get(self):
        self.content = json.loads(requests.get(url=self.url, headers=self.headers, params=self.params, proxies=self.proxies).text,object_hook=lambda d: SimpleNamespace(**d))
        print(self.content)
        self.content.created_at = datetime.datetime.fromisoformat(self.content.created_at.replace("Z", ""))
        return self
