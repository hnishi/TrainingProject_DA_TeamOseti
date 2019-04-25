class WordCounter():
    #{"word", num}
    counts_ = {}

    def addNumOfWord(this,word, num):
        if(word in this.counts_):
            this.counts_[word] += num
        else:
            this.counts_[word] = num

    def getRanking(this):
        return sorted(this.counts_.items(), key=lambda x:x[1], reverse=True)

    def printAll(this):
        print(this.counts_)

if __name__ == "__main__":
    hoge = WordCounter()
    hoge.addNumOfWord("aaa", 100)
    hoge.addNumOfWord("bbb", 100)
    hoge.addNumOfWord("aaa", 100)
    hoge.addNumOfWord("ccc", 150)
    print(hoge.getRanking())