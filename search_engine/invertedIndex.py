import jieba
import jieba.analyse


class InvertedIndex:
    def __init__(self, raw_file):
        # 用来生成倒排索引的文档
        self.raw_file_path = raw_file
        # 对于单个文档统计词频
        self.freq = {}
        # 词表
        self.termid = {}
        # 文档表
        self.docid = {}
        # 词-文档-词频表
        self.termiddoclist = []

    def build_index(self):
        i = 1
        j = 1
        # k = 0
        useless = []
        with open('stoplist_utf8.txt', encoding='utf-8') as fread:
            for line in fread:
                line = line.strip()  # 去掉两端的空白字符，如空格、回车等
                useless.append(line)
        fread.close()
        with open(self.raw_file_path, encoding='utf-8') as fread:
            for line in fread:
                # if k < 5:
                #     k += 1
                # else:
                #     break
                line = line.strip()  # 去掉两端的空白字符，如空格、回车等
                self.freq.clear()
                self.docid[line] = i
                i += 1
                word = jieba.lcut(line)
                for w in word:
                    # 排除停用词且长度不能太低
                    if (w not in useless and len(w) > 1):
                        # 如果w不在词表里就将w加入词表中
                        if w not in self.termid:
                            self.termid[w] = j
                            j += 1
                        # 统计词频，用于创建termiddoclist
                        self.freq[w] = self.freq.get(w, 0) + 1
                for oneword in self.freq:
                    self.termiddoclist.append([self.termid[str(oneword)], i - 1, self.freq[str(oneword)]])
            termiddoclist = self.termiddoclist
            self.termiddoclist = sorted(termiddoclist, key=lambda termiddoclist: termiddoclist[0])
            # print(self.termid)
            # print(self.docid)
            # print(self.termiddoclist)
        fread.close()

    def write_to_disk(self):
        with open('termid.txt', 'w', encoding='utf-8') as fread:
            # with open('t.txt', 'w', encoding='utf-8') as fread:
            for i in self.termid:
                fread.write(str(i) + ' ' + str(self.termid[str(i)]))
                fread.write('\n')
        fread.close()
        with open('docid.txt', 'w', encoding='utf-8') as fread:
            # with open('d.txt', 'w', encoding='utf-8') as fread:
            for i in self.docid:
                fread.write(str(i) + ' ' + str(self.docid[str(i)]))
                fread.write('\n')
        fread.close()
        with open('termiddoclist.txt', 'w', encoding='utf-8') as fread:
            # with open('td.txt', 'w', encoding='utf-8') as fread:
            for i in self.termiddoclist:
                for j in i:
                    fread.write(str(j) + ' ')
                fread.write('\n')

    def load_from_disk(self, termid, docid, termiddoclist):
        with open('termid.txt', encoding='utf-8') as fread:
            # with open('t.txt', encoding='utf-8') as fread:
            for i in fread:
                i = i.strip().split()
                termid[i[0]] = i[1]
        with open('docid.txt', encoding='utf-8') as fread:
            # with open('d.txt', encoding='utf-8') as fread:
            for i in fread:
                i = i.strip().split()
                docid[i[0]] = i[1]
        with open('termiddoclist.txt', encoding='utf-8') as fread:
            # with open('td.txt', encoding='utf-8') as fread:
            for i in fread:
                i = i.strip().split()
                termiddoclist.append(i)
