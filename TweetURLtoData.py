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
    card: dict = None
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
        if self.card != None:
            self.card = TweetURLtoDataCard(**self.card)
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

@dataclass
class TweetURLtoDataCard:
    card_platform: dict = None
    name: str = None
    url: str = None
    binding_values: dict = None
    def __post_init__(self):
        self.card_platform = TweetURLtoDataCardPlatform(**self.card_platform)
        self.binding_values = TweetURLtoDataBinding(**self.binding_values)
        
@dataclass
class TweetURLtoDataCardPlatform:
    platform: dict = None
    def __post_init__(self):
        self.platform = TweetURLtoDataPlatform(**self.platform)

@dataclass
class TweetURLtoDataPlatform:
    audience:str = None
    device:str = None

@dataclass
class TweetURLtoDataPlatformAudience:
    name:str = None

@dataclass
class TweetURLtoDataPlatformDevice:
    name:str = None
    version:str = None

@dataclass
class TweetURLtoDataBinding:
    photo_image_full_size_large: dict = None
    thumbnail_image: dict = None
    description: dict = None
    domain: dict = None
    thumbnail_image_large: dict = None
    summary_photo_image_small: dict = None
    thumbnail_image_original: dict = None
    site: dict = None
    photo_image_full_size_small: dict = None
    summary_photo_image_large: dict = None
    thumbnail_image_small: dict = None
    thumbnail_image_x_large: dict = None
    photo_image_full_size_original: dict = None
    vanity_url: dict = None
    photo_image_full_size: dict = None
    thumbnail_image_color: dict = None
    title: dict = None
    summary_photo_image_color: dict = None
    summary_photo_image_x_large: dict = None
    summary_photo_image: dict = None
    photo_image_full_size_color: dict = None
    photo_image_full_size_x_large: dict = None
    card_url: dict = None
    summary_photo_image_original: dict = None
    def __post_init__(self):
        self.photo_image_full_size_large = TweetURLtoDataImage(**self.photo_image_full_size_large)
        self.thumbnail_image = TweetURLtoDataImage(**self.thumbnail_image)
        self.description = TweetURLtoDataString(**self.description)
        self.domain = TweetURLtoDataString(**self.domain)
        self.thumbnail_image_large = TweetURLtoDataImage(**self.thumbnail_image_large)
        self.summary_photo_image_small = TweetURLtoDataImage(**self.summary_photo_image_small)
        self.thumbnail_image_original = TweetURLtoDataImage(**self.thumbnail_image_original)
        self.site = TweetURLtoDataSite(**self.site)
        self.photo_image_full_size_small = TweetURLtoDataImage(**self.photo_image_full_size_small)
        self.summary_photo_image_large = TweetURLtoDataImage(**self.summary_photo_image_large)
        self.thumbnail_image_small = TweetURLtoDataImage(**self.thumbnail_image_small)
        self.thumbnail_image_x_large = TweetURLtoDataImage(**self.thumbnail_image_x_large)
        self.photo_image_full_size_original = TweetURLtoDataImage(**self.photo_image_full_size_original)
        self.vanity_url = TweetURLtoDataVanity(**self.vanity_url)
        self.photo_image_full_size = TweetURLtoDataImage(**self.photo_image_full_size)
        self.thumbnail_image_color = TweetURLtoDataImageColor(**self.thumbnail_image_color)
        self.title = TweetURLtoDataString(**self.title)
        self.summary_photo_image_color = TweetURLtoDataImageColor(**self.summary_photo_image_color)
        self.summary_photo_image_x_large = TweetURLtoDataImage(**self.summary_photo_image_x_large)
        self.summary_photo_image = TweetURLtoDataImage(**self.summary_photo_image)
        self.photo_image_full_size_color = TweetURLtoDataImageColor(**self.photo_image_full_size_color)
        self.photo_image_full_size_x_large = TweetURLtoDataImage(**self.photo_image_full_size_x_large)
        self.card_url = TweetURLtoDataVanity(**self.card_url)
        self.summary_photo_image_original = TweetURLtoDataImage(**self.summary_photo_image_original)

@dataclass
class TweetURLtoDataImage:
    image_value: dict = None
    type:str = None
    def __post_init__(self):
        self.image_value = TweetURLtoDataImageValue(**self.image_value)
    
@dataclass
class TweetURLtoDataImageValue:
    height:int = None
    width:int = None
    url:str = None

@dataclass
class TweetURLtoDataString:
    string_value: str = None
    type: str = None

@dataclass
class TweetURLtoDataSite:
    scribe_key:str = None
    type:str = None
    user_value:dict = None
    def __post_init__(self):
        self.user_value = TweetURLtoDataSiteUser(**self.user_value)
    
@dataclass
class TweetURLtoDataSiteUser:
    id_str:str = None
    path: dict = None

@dataclass
class TweetURLtoDataVanity:
    scribe_key:str = None
    string_value:str = None
    type:str = None

@dataclass
class TweetURLtoDataImageColor:
    image_color_value:str = None
    type:str = None

@dataclass
class TweetURLtoDataImageColorValue:
    palette:dict = None
    def __post_init__(self):
        self.palette = [TweetURLtoDataPalette(**palette) for palette in self.palette]

@dataclass
class TweetURLtoDataPalette:
    rgb:dict = None
    percentage:int = None
    def __post_init__(self):
        self.rgb = TweetURLtoDataColor(**self.rgb)