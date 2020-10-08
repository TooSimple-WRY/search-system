import math
import jieba
import jieba.analyse
from search_engine.jieba_cut import Jieba
from search_engine.sentence import get_sentences
class Score_Sort:
    def __init__(self,sentence,termid,docid,termiddoclist):
        #用户输入的句子
        self.sentence = sentence
        #对用户输入的句子进行分词之后得到的词的集合
        self.word = []
        #用来返回排好序的文档字典，{文档：分数}
        self.final = {}
        #用来存放文档摘要，{文档：摘要}
        self.text_summary = {}
        #用来存放每个词的idf，{词：idf}
        self.word_idf = {}
        #词表
        self.termid = termid
        #文档表
        self.docid = docid
        #词-文档-词频表
        self.termiddoclist = termiddoclist
    def build_words(self):
        #用来存放摘要
        middle = {}
        #对用户输入的信息进行分词后得到的集合
        words = set()
        #存放停用词
        useless = []
        #中文分词
        with open('stoplist_utf8.txt', encoding='utf-8') as fread:
            for line in fread:
                line = line.strip()  # 去掉两端的空白字符，如空格、回车等
                useless.append(line)
        fread.close()
        word = jieba.lcut(self.sentence)
        for w in word:
            # 排除停用词且长度不能太低
            if (w not in useless and len(w) > 1):
                words.add(w)
        #选出候选文档，用TF-IDF对文档打分
        for w in words:
            df = 0
            if w in self.termid:
                #先算DF
                for p in self.termiddoclist:
                    if p[0] == self.termid[w]:
                        df += 1
                #存放每个词的idf
                self.word_idf[w] = math.log(6998/df)
                #计算TF-IDF
                for p in self.termiddoclist:
                    if p[0] == self.termid[w]:
                        for passage in self.docid:
                            if self.docid[str(passage)] == p[1]:
                                self.final[str(passage)] = self.final.get(str(passage),0) + int(p[2])*math.log(6998 / df)
        #求文本摘要
        for text in self.final:
            #清空临时字典，这个字典用于存放每个文档中各个句子的分数
            middle.clear()
            #对每个文档进行分句
            sentences = get_sentences(str(text))
            for sentence in sentences:
                for one in words:
                    if one in sentence:
                        middle[str(sentence)] = middle.get(str(sentence),0) + self.word_idf[str(one)]
            # 对所有摘要排序，如果摘要的数量大于5，就取排名靠前的5个摘要
            sentencelist = sorted(middle.items(), key=lambda x: x[1], reverse=True)
            if len(sentencelist) > 5:
                num = 5
            else:
                num = len(sentencelist)
            #将每个文档和相应的摘要以字典的形式存到self.text_summary中
            self.text_summary[str(text)] = sentencelist[:num]
    #返回文档和相应评分的字典
    def get_passage(self):
        return self.final
    #返回对应文档的摘要
    def get_text_summary(self,text):
        return self.text_summary[text]