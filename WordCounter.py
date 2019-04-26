class WordCounter():
    def __init__(self):
        #{"word", num}
        self.counts_ = {}

    def addNumOfWord(self,word, num):
        if(word in self.counts_):
            self.counts_[word] += num
        else:
            self.counts_[word] = num

    def getRanking(self):
        return sorted(self.counts_.items(), key=lambda x:x[1], reverse=True)

    def printAll(self):
        print(self.counts_)

if __name__ == "__main__":
    hoge = WordCounter()
    hoge.addNumOfWord("aaa", 100)
    hoge.addNumOfWord("bbb", 100)
    hoge.addNumOfWord("aaa", 100)
    hoge.addNumOfWord("ccc", 150)
    print(hoge.getRanking())