from search_engine.classification import Classification
from search_engine.invertedIndex import InvertedIndex
from search_engine.score_sort import Score_Sort
from search_engine.sentence import get_sentences

raw_file = 'ir_corpus_1000_shuffled_new1.txt'#存放和载入倒排索引的文件


i = InvertedIndex(raw_file)#建立倒排索引
termid = {}#词表
docid = {}#文档表
termiddoclist = []#词-文档-词频表
# i.build_index() #建立倒排索引
# i.write_to_disk() #将建好的倒排索引写入磁盘
i.load_from_disk(termid,docid,termiddoclist)#载入倒排索引


# k = 0
# for i in termid:
#     if k < 10:
#         k += 1
#     else:
#         break
#     print(i+':'+termid[str(i)])
# m = 0
# for i in docid:
#     if m < 10:
#         m += 1
#     else:
#         break
#     print(i+':'+docid[str(i)])
# n = 0
# for i in termiddoclist:
#     if n < 10:
#         n += 1
#     else:
#         break
#     print(i)



print('索引载入完毕')
classification = Classification()#文本分类
# classification.create_classification_model()#根据文本分类数据建模并用pickle工具将模型储存起来
# classification.get_model_score()#给建好的sklearn文本分类线性模型进行评分，如果要看评分请将上一行的建模函数一并取消注释
classification.load_model()#载入建好的模型
classificationdict = {}#用来存放分好类的文档-类别字典
while 1:
    print('请输入一个查询：')
    query = input().strip()
    if query == 'q':
        break
    p = Score_Sort(query,termid,docid,termiddoclist)
    p.build_words()
    # print(sorted(p.get_passage().items(),key = lambda x:x[1],reverse = True))
    # print(p.get_passage())
    result = sorted(p.get_passage().items(),key = lambda x:x[1],reverse = True)
    print('总共检索到%d篇文章'%len(result))
    num = 0
    #因为每篇文章分类都要花一点时间，我希望展示的内容能一步到位，所以就先对检索到的文档进行分类
    for i in result:
        classificationdict[i[0]] = classification.get_classification(i[0])[0]
    for i in result:
        num += 1
        print('第%d篇文章'%num)
        print('题目:' + get_sentences(i[0])[0])
        print('摘要:')
        text_summary = p.get_text_summary(i[0])
        for summary in text_summary:
            print(summary[0] + ' ' + str(summary[1]))
        print('评分:' + str(i[1]))
        print('主题标签:' + classificationdict[i[0]])
        print(i[0])