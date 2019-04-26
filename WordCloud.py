# coding: utf-8
from wordcloud import WordCloud

class makeWordCloud (): 

  def genPng ( self, mydict, name_png): 
    wordcloud = WordCloud(background_color="white",
        font_path="/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc", # Standard Japanese Font
        #font_path="/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf", # Standard Japanese Font
        width=800,height=600).fit_words( mydict ) 
    wordcloud.to_file( name_png )

if __name__ == "__main__":
  mydict = {"aaa":1, "bbb":2, "ccc":3, "嬉":1, "哀":2, "怒":3}
  hoge = makeWordCloud() 
  hoge.genPng( mydict , name_png = "out_wordcloud.png" )

#https://qiita.com/furipon308/items/be97abf25cf4caa0574e
#http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud.fit_words
