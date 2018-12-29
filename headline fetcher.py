import feedparser
d = feedparser.parse('https://www.hindustantimes.com/rss/topnews/rssfeed.xml')#paste the link of web rss here to fetch the feed from site.
print (d.feed.title)
#FUNCTION TO GET HEADLINES FROM SITE AND STORE IT TO LIST BY ITERATINTING THROUGH FEED
def getHeadlines( d ):
    headlines = []
    for newsitem in d['items']:
        headlines.append(newsitem['title'])
    return headlines
#PRINTING THE FEED TO TERMINAL WITH ENUMERATION TO EACH LINE
for count,hl in enumerate(getHeadlines(d),start=1):
    print(count,hl)
#WRITING THE FEED TO A CSV FILE WITH ENUMERATION TO EACH FEED    
with open("myfile.csv","w") as f:
    for count,hl in enumerate(getHeadlines(d),start=1):
        f.writelines('%d.'%count)
        f.writelines(hl+'\n')
        
