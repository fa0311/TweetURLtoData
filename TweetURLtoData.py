import requests
from dataclasses import dataclass
import datetime
import re


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

    def get(self, content_flag=True):
        self.content_flag = content_flag
        self.json = requests.get(url=self.url, headers=self.headers, params=self.params, proxies=self.proxies).json()
        self.json["request"] = {
            "url":self.url,
            "params":self.params,
            "headers":self.headers,
            "proxies":self.proxies,
        }
        if self.content_flag:
            self.content = TweetURLtoDataContent(**self.json)
        return self

@dataclass
class TweetURLtoDataContent:
    request: dict = None
    in_reply_to_screen_name:str  = None
    in_reply_to_status_id_str:str  = None
    in_reply_to_user_id_str:str = None
    lang: str = None
    reply_count: int = 0
    retweet_count: int = 0
    favorite_count: int = 0
    self_thread: dict = None
    created_at: str = None
    display_text_range: dict = None
    entities: dict = None
    id_str: str = None
    text: str = None
    user: dict = None
    photos: dict = None
    video: dict = None
    conversation_count: int = None
    news_action_type: str = None
    quoted_tweet: dict = None
    parent: dict = None

    def __post_init__(self):
        self.created_at = datetime.datetime.fromisoformat(self.created_at.replace("Z", ""))
        self.entities = TweetURLtoDataEntities(**self.entities)
        self.user = TweetURLtoDataUser(**self.user)
        if self.photos != None:
            self.photos = [TweetURLtoDataPhoto(**photo) for photo in self.photos]
        if self.video != None:
            self.video = TweetURLtoDataVideo(**self.video)
        if self.quoted_tweet != None:
            self.quoted_tweet = TweetURLtoDataContent(**self.quoted_tweet)
        if self.parent != None:
            self.parent = TweetURLtoDataContent(**self.parent)
        if self.self_thread != None:
            self.self_thread = TweetURLtoDataSelfThread(**self.self_thread)

    def reply_to(self):
        if self.in_reply_to_status_id_str != None:
            data = TweetURLtoData("")
            data.url = self.request["url"]
            data.params = self.request["params"]
            data.params["id"] = self.in_reply_to_status_id_str
            data.headers = self.request["headers"]
            data.proxies = self.request["proxies"]
            return data.get().content

    def thread(self):
        if self.self_thread != None:
            data = TweetURLtoData("")
            data.url = self.request["url"]
            data.params = self.request["params"]
            data.params["id"] = self.in_reply_to_status_id_str
            data.headers = self.request["headers"]
            data.proxies = self.request["proxies"]
            return data.get().content

@dataclass
class TweetURLtoDataSelfThread:
    id_str: str = None

@dataclass
class TweetURLtoDataEntities:
    hashtags: dict = None
    urls: dict = None
    user_mentions: dict = None
    symbols: dict = None
    media: dict = None

    def __post_init__(self):
        if self.hashtags != None:
            self.hashtags = [TweetURLtoDataHashtag(**hashtag) for hashtag in self.hashtags]
        if self.user_mentions != None:
            self.user_mentions = [TweetURLtoDataMention(**mention) for mention in self.user_mentions]
        if self.media != None:
            self.media = [TweetURLtoDataMedia(**media) for media in self.media]

@dataclass
class TweetURLtoDataHashtag:
    indices: dict = None
    text: str = None


@dataclass
class TweetURLtoDataMention:
    id_str:str = None
    indices: dict = None
    name: str = None
    screen_name: str = None

@dataclass
class TweetURLtoDataMedia:
    display_url: str = None
    expanded_url: str = None
    indices: dict = None
    url: str = None

@dataclass
class TweetURLtoDataUser:
    id_str: str = None
    name: str = None
    profile_image_url_https: str = None
    screen_name: str = None
    verified: bool = None
    
@dataclass
class TweetURLtoDataPhoto:
    backgroundColor: dict = None
    cropCandidates: dict = None
    expandedUrl: str = None
    url: str = None
    width: int = None
    height: int = None
    def __post_init__(self):
        self.backgroundColor = TweetURLtoDataColor(**self.backgroundColor)
        self.cropCandidates = [TweetURLtoDataCandidates(**cropCandidates) for cropCandidates in self.cropCandidates]

@dataclass
class TweetURLtoDataColor:
    red: int = None
    green: int = None
    blue: int = None

@dataclass
class TweetURLtoDataCandidates:
    x: int = None
    y: int = None
    w: int = None
    h: int = None


@dataclass
class TweetURLtoDataVideo:
    aspectRatio: dict = None
    contentType: str = None
    durationMs: int = None
    mediaAvailability: dict = None
    poster: str = None
    variants: dict = None
    videoId: dict = None
    viewCount: int = None
    def __post_init__(self):
        self.mediaAvailability = TweetURLtoDataMediaAvailability(**self.mediaAvailability)
        self.videoId = TweetURLtoDataVideoId(**self.videoId)
        self.variants = [TweetURLtoDataVariants(**variants) for variants in self.variants]

@dataclass
class TweetURLtoDataVideoId:
    type: str = None
    id: str = None

@dataclass
class TweetURLtoDataVariants:
    type: int = None
    src: int = None


@dataclass
class TweetURLtoDataMediaAvailability:
    status: str = None
