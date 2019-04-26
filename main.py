import CsvAnalyze as reader
import MeCab
import WordCounter as counter
import WordCloud as wc

print("start")
data = reader.AllBooks("comments")
#print(data["comments"])
m_neologd = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/ -Ochasen")


def getWordList(str):
    word_list = []
    if not str == str :
        return word_list
    #TODO 名詞や形容詞や感動詞だけで絞り込む
    #ぽやしみ	ポヤシミ	おやすみ	名詞-固有名詞-一般
    mecab_return = m_neologd.parse(str).split('\n')

    for row in mecab_return:
        values = row.split("\t")
        if len(values) < 2:
            break
        if ("名詞" in values[3]) or ("形容詞" in values[3]) or ("感動詞" in values[3]):
            if not ("名詞-非自立" in values[3]):
                word_list.append(values[0])
    
    return word_list

def sumOfWords(title):
    count = counter.WordCounter()
    comments = reader.OutCommnet(data, title)
    for comment in comments:
        for word in getWordList(comment):
            count.addNumOfWord(word,1)
    #return count.getRanking()
    return count.counts_ 


"""
mytitles = [
"HUNTER×HUNTER",
"テニスの王子様",
"テラフォーマーズ",
"ボボボーボ・ボーボボ",
"幽★遊★白書",
"ONE PIECE",
"ハチワンダイバー",
"GANTZ",
"Dr.スランプ",
"DEATH NOTE",
"食戟のソーマ",
"NARUTO―ナルト―" ]
"""

mytitles = [
"遊☆戯☆王",
"ドラゴンボール超"
]

for i_title in mytitles :
  print(i_title)

  print(sumOfWords( i_title ))

  mydict = sumOfWords( i_title ) 
  hoge = wc.makeWordCloud()
  name = "out_wordcloud/" + i_title + ".png" 
  hoge.genPng( mydict , name_png = name )

