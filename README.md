# TweetURLtoData

TwitterAPI を使わずにツイート内容を取得する<br>
そのうち JavaScript で Web クライアントのみで動作するの作る<br>

# import

```Console
pip install -r requirements.txt
```

現在使えません

# use

```Python
from TweetURLtoData import TweetURLtoData
TweetURLtoData("xxxxxxxxxxxxxxxxxxx")
```

```Python
from TweetURLtoData import TweetURLtoData,TweetURLExtractor
TweetURLtoData(TweetURLExtractor("https://twitter.com/xxxxxxxxxx/status/xxxxxxxxxxxxxxxxxxx")[0][1])
```

# License

TweetURLtoData is under MIT License
