from wordcloud import WordCloud
from os import path
from bs4 import BeautifulSoup

#f = urlopen('')
dirname = path.dirname(__file__)

release_file = 'release-2019.html'
releases = open(path.join(dirname,release_file), 'r').read()

words = ""
soup_releases = BeautifulSoup(releases,"html.parser")
#print(len(soup_releases.find_all('h3')))
for title in soup_releases.find_all("li", attrs={"class", "whats-new"}):
    print("%s: %s" %(title.contents[3].string, title.contents[1].string))

'''
for title in soup_releases.find_all('h3'):
    words += ' ' + title.text

wordcloud = WordCloud(background_color="white",
    font_path="/Library/Fonts/ipaexg.ttf",
    width=800,height=600).generate(words)

d = path.dirname(__file__)

wordcloud.to_file(path.join(d,"awsrelease-all-keywords-2019-ja.png"))
'''
