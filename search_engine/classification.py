import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from search_engine.jieba_cut import Jieba
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
class Classification:
    def __init__(self):
        #用来生成稀疏矩阵
        self.tv = None
        #用来生成sklearn中的文本报告
        self.y_pre_svm = None
        #用来存放模型
        self.model_svc = None
        #被分为训练数据的文档
        self.tv_train = None
        #被分为测试数据的文档
        self.tv_test = None
        #被分为训练数据的标签
        self.y_train = None
        #被分为测试数据的标签
        self.y_test = None
        #用于生成稀疏矩阵
        self.tv_data = None
        #存放所有标签，这个过程不去重
        self.labels = []
        #用来存放对文档进行预处理之后的内容
        self.tmp = []
        #用来存放所有文档
        self.data_after = []
    def create_classification_model(self):
        with open('classification_corpus_800_new.txt', encoding='utf-8') as fread:
            # k = 0
            for line in fread:
                # k += 1
                # if k > 1000:
                #     break
                line = line.strip().split('\t')  # 去掉两端的空白字符，如空格、回车等并以\t来分割
                self.labels.append(line[0])
                self.data_after.append(Jieba(line[1]))
        #对文档进行预处理
        for i in self.data_after:
            self.tmp.append(' '.join(i))
        # texts = ["dog cat fish", "dog cat cat", "fish bird", 'bird']
        self.tv = TfidfVectorizer()
        self.tv_data = self.tv.fit_transform(self.tmp)
        pk_file = open(r'tv.pkl', 'wb')
        pickle.dump(self.tv, pk_file)
        pk_file.close()
        # print(self.tv_data[0])
        # print(self.tv_data.toarray())
        #将训练数据和测试数据分开，80%为训练数据，20%为测试数据
        self.tv_train,self.tv_test,self.y_train,self.y_test = train_test_split(
            self.tv_data,self.labels,test_size=0.2,random_state=100
        )
        #进行建模
        self.model_svc = LinearSVC(max_iter=100000).fit(X=self.tv_train,y=self.y_train)
        # 存放建好的模型
        pk_file = open(r'model_svc.pkl', 'wb')
        pickle.dump(self.model_svc,pk_file)
        pk_file.close()
    #从.pkl文件中载入模型
    def load_model(self):
        pk = open('model_svc.pkl', 'rb+')
        self.model_svc = pickle.load(pk)
        pk.close()
        pk = open('tv.pkl', 'rb+')
        self.tv = pickle.load(pk)
        pk.close()
    def get_model_score(self):
        self.y_pre_svm = self.model_svc.predict(self.tv_test)
        print('模型评分：'+ str(self.model_svc.score(self.tv_test,self.y_test)))
        print('文本报告：\n' + classification_report(y_true=self.y_test,y_pred=self.y_pre_svm))
    #对文档text进行分类
    def get_classification(self,text):
        tmp = []
        words = Jieba(text)
        tmp.append(' '.join(words))
        tv_data = self.tv.transform(tmp)
        return self.model_svc.predict(tv_data)
# i = Classification()
# # i.create_classification_model()
# # i.get_model_score()
# i.load_model()
# k = 0
# with open('ir_corpus_1000_shuffled_new1.txt', encoding='utf-8') as fread:
#     texts = []
#     for line in fread:
#         k += 1
#         if k > 10:
#             break
#         line = line.strip()  # 去掉两端的空白字符，如空格、回车等
#         i.get_classification(line)