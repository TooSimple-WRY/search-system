import re


def get_sentences(doc):
    line_break = re.compile('[\r\n]')
    delimiter = re.compile('[，。？！；“”《》【】]')
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences
# words = []
# final = []
# k = 0
# with open('ir_corpus_1000_shuffled_new1.txt', encoding='utf-8') as fread:
#     for line in fread:
#         if k < 5:
#             k += 1
#         else:
#             break
#         line = line.strip()  # 去掉两端的空白字符，如空格、回车等
#         words.append(line)
# for i in words:
#     final.append(get_sentences(i))
# print(final)
