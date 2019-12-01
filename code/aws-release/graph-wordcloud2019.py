from wordcloud import WordCloud
from os import path
from bs4 import BeautifulSoup

dirname = path.dirname(__file__)

release_file = 'release-2019.html'
releases = open(path.join(dirname,release_file), 'r').read()
words = ""
soup_releases = BeautifulSoup(releases,"html.parser")

for title in soup_releases.find_all("li", attrs={"class", "whats-new"}):
    if "開始" and "一般" in title.contents[1].string:
        print("- " + title.contents[1].string)


'''
# 文字を数えるだけ
words_list = ["開始", "追加","簡素化", "改善", "発表", "利用可能に", "サポート", "拡大"]
def word_count(text, words_list):
    for word in words_list:
        print(word + ": " + str(text.count(word)))
#文字の出現率を探す
for title in soup_releases.find_all("li", attrs={"class", "whats-new"}):
    if "開始" and "一般" in title.contents[1].string:
        words += ' ' + title.contents[1].string
#word_count(words, words_list)
'''


'''
#WordCloudで画像を作る
for title in soup_releases.find_all('h3'):
    words += ' ' + title.text

wordcloud = WordCloud(background_color="white",
    font_path="/Library/Fonts/ipaexg.ttf",
    width=800,height=600).generate(words)

d = path.dirname(__file__)

wordcloud.to_file(path.join(d,"awsrelease-all-keywords-2019-ja.png"))
'''
