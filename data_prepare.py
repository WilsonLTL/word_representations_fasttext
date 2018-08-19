import jieba
import os

# source location
basedir = "/home/li/corpus/news/"
# label
dir_list = ['affairs','constellation','economic','edu','ent','fashion','game','home','house','lottery','science','sports','stock']

ftrain = open("news_fasttext_train.txt","w")
ftest = open("news_fasttext_test.txt","w")

num = -1
for e in dir_list:
    num += 1
    indir = basedir + e + '/'
    files = os.listdir(indir)
    count = 0
    for fileName in files:
        count += 1
        filepath = indir + fileName
        with open(filepath,'r') as fr:
            text = fr.read()
        text = text.decode("utf-8").encode("utf-8")
        seg_text = jieba.cut(text.replace("\t"," ").replace("\n"," "))
        outline = " ".join(seg_text)
        outline = outline.encode("utf-8") + "\t__label__" + e + "\n"
#         print outline
#         break

        if count < 10000:
            ftrain.write(outline)
            ftrain.flush()
            continue
        elif count  < 20000:
            ftest.write(outline)
            ftest.flush()
            continue
        else:
            break

ftrain.close()
ftest.close()