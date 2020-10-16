import jieba
import jieba.analyse


def Jieba(sentence):
    words = []
    useless = []
    with open('stoplist_utf8.txt', encoding='utf-8') as fread:
        for line in fread:
            line = line.strip()  # 去掉两端的空白字符，如空格、回车等
            useless.append(line)
    fread.close()
    word = jieba.lcut(sentence)
    for w in word:
        # 排除停用词且长度不能太低
        if w not in useless and len(w) > 1:
            words.append(w)
    return words
