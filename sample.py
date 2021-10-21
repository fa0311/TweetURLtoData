from TweetURLtoData import TweetURLtoData,TweetURLExtractor


msg = """\
One day in summer, when a grasshopper was singing in the grassy meadow, a group of ants walked by.
https://twitter.com/elonmusk/status/1448558569922703363?t=xxxxxxxxx&s=00
"Hello, dear ants. What are you doing drenched in sweat?"
"Hello, grasshopper. We are conveying food."
"Hmm… I see. But as you can see, there is plenty of food around here.
https://twitter.com/BarackObama/status/1445464088335708160?t=xxxxxxxxx&s=00Why do you have to convey food to your home one by one?
Look at me. I eat things around here when I get hungry. I sing merrily orhttps://twitter.com/justinbieber/status/1446927989531451392have fun for the rest of the time."
"Listen, grasshopper.
We have plenty of food right now because it's summer, but once winter comes, there will be no food to eat here.
It is better to stock up food for winter or you may get in trouble later."
When the ants said so, the grasshopperhttp://twitter.com/katyperry/status/1443795730838134790laughed sniffily.
"Ha-ha-ha"
and he said,
"""


for url in TweetURLExtractor(msg):
    print(TweetURLtoData(url[1]).get().content.user.name) #Elon Musk  Barack Obama  Justin Bieber  KATY PERRY

option = TweetURLtoData("1448558569922703363")
print(option.get(False).json["user"]["name"]) #Elon Musk


option2 = TweetURLtoData("1448558569922703363")
option2.params["lang"] = "ja"
# option2.proxies = {
#     "http":"http://example.com/proxy.pac",
#     "https":"http://example.com/proxy.pac"
# }
print(option2.get().content.user.name) #Elon Musk