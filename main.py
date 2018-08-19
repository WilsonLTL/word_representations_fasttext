# import fasttext
import logging
import gensim
from flask import Flask,jsonify,request
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# text classifier
# model = FastText('source/wiki_seg.txt', size=4, window=3, min_count=1, iter=10)
# model.save('source/word2vec.model')


# fast_model = fasttext.load_model('source/model.bin')
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.KeyedVectors.load_word2vec_format('source/model.vec')

@app.route('/gensim_single_text', methods = ['POST'])
def sin():
    text = request.json['text1']
    similar = model.most_similar(positive=[text], topn=10)
    print(similar)
    return jsonify(similar)

@app.route('/gensim_double_text', methods = ['POST'])
def dou():
    text1 = request.json['text1']
    text2 = request.json['text2']
    similar = model.similarity(text1,text2)
    print(similar)
    return jsonify(similar)

@app.route('/fasttext_single_text',methods= ['POST'])
def fasttext_sin():
    text = request.json['text1']


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)


