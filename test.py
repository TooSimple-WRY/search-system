# dict1 = {'a':10}
# dict2 = {'b':20}
# dict3 = {'a':30}
# p = []
# p.append(dict1)
# p.append(dict2)
# p.append(dict3)

# p.append({'a':10})
# p.append({'b':20})
# p.append({'a':30})
#
# print(p)
#
# for i in p:
#     for j in i:
#         print(i[j])


# dict = {'a':3,'b':1,'c':2,'e':3}
# dict1 = {'a':10,'b':20,'c':30}
# print(dict)
# l = []
# l1 = []
# l2 = {}
# for i in dict:
#     l.append([dict[str(i)],1,dict1[str(i)]])

# i
# print(l1)

# with open('test.txt','w',encoding='utf-8') as fread:
#     for i in l:
#         for j in i:
#             fread.write(str(j)+' ')
#         fread.write('\n')
# fread.close()
# with open('test.txt',encoding='utf-8') as fread:
#     for i in fread:
#         i = i.strip().split()
#         l1.append(i)
# print(l1)
# for i in l1:
#     if i[0] == '2':
#         print(i)


# print(sorted(l1,key=lambda l1:l1[0]))

# with open('test1.txt','w',encoding='utf-8') as fread:
#     for i in dict:
#         fread.write(str(i)+' '+str(dict[str(i)]))
#         fread.write('\n')
# fread.close()
# with open('test1.txt',encoding='utf-8') as fread:
#     for i in fread:
#         i = i.strip().split()
#         l2[i[0]] = i[1]
# print(l2)

# print(dict.get('d',0)+1)
# print(len(dict))
# sentencelist = sorted(dict.items(), key=lambda x: x[1], reverse=True)
# dict2 = {}
# print(len(sentencelist))
# dict2['aa'] = sentencelist[:2]
# print(dict2)

# from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
# x_train = {'this is a good boy','he is a bad guy'}
# tv = TfidfVectorizer()
# train_data = tv.fit_transform(x_train)
# print(train_data)

# import jieba
# str1 = ['I am a cat.']
# k = 0
# words = {}
# for j in str1:
#     word = jieba.lcut(j)
#     sentence = []
#     for i in word:
#         k = j.find(i,k)
#         words[str(k)+' '+str(k+len(i))] = [i]
#         print(words)
#     if '0 1' in words:
#         print(words['0 1'])

import tensorflow as tf
version = tf.__version__
gpu_ok = tf.test.is_gpu_available()
print("tf version:",version,"\nuse GPU",gpu_ok)