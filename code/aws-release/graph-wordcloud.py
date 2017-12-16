from wordcloud import WordCloud
from os import path
from bs4 import BeautifulSoup

#f = urlopen('')
dirname = path.dirname(__file__)

release_file = '2017.htm'
releases = open(path.join(dirname,release_file), 'r').read()

words = ""
soup_releases = BeautifulSoup(releases,"html.parser")
for title in soup_releases.find_all('h3'):
    words += ' ' + title.text

wordcloud = WordCloud(background_color="white",
    font_path="/Library/Fonts/Arial Black.ttf",
    width=800,height=600).generate(words)

d = path.dirname(__file__)

wordcloud.to_file(path.join(d,"awsrelease-all-keywords.png"))
