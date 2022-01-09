# TweetURLtoData

TwitterAPI を使わずにツイート内容を取得する<br>
ログイン: [TwitterFrontendFlow](https://github.com/fa0311/TwitterFrontendFlow) /
取得: [TweetURLtoData](https://github.com/fa0311/TweetURLtoData) /
スペース: [TwitterSpacesWiretap](https://github.com/fa0311/TwitterSpacesWiretap)

# import

```Console
pip install -r requirements.txt
```

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
