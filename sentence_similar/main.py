import jieba,gensim,ast,random,firebase_admin,json
from FastTextNN import NNLookup as NN
from flask import Flask,jsonify,request
from firebase_admin import credentials, firestore

app = Flask(__name__)

wiki_model = NN()
model = gensim.models.KeyedVectors.load_word2vec_format('../source/model.vec')
jieba.set_dictionary('jieba_dict/dict.txt.big')
stopword_set = set()
with open('jieba_dict/stopwords.txt', 'r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))


@app.route('/insert_update_record', methods=['POST'])
def insert_record():
    system_id = request.json['system_id']
    agents = request.json['agent']
    system = db.collection('agents')

    for agent in agents:
        item = {
            "agent_id": agent["agent_id"],
            "agent_name": agent["agent_name"],
            "intents": []
        }
        agent_item = system.document(str(system_id)+","+str(agent["agent_id"]))
        for intent in agent["intents"]:
            result = {
                    "intent_name": intent['intent_name'],
                    "pharse":[],
                    "response_text": intent['response_text'],
                }
            for train_phrase in intent["training_phrases"]:
                intents = []
                cut_text = jieba_cut(train_phrase)
                for ct in cut_text:
                    intents.append(ct)
                result["pharse"].append({"training_phrases":train_phrase,"check_phrases":intents})
            item["intents"].append(result)
        agent_item.set(item)
        serve_init()
    return jsonify(item)


@app.route('/check_similar_by_agent', methods=['POST'])
def check_similar_by_agent():
    system_id = request.json['system_id']
    agent_id = request.json['agent_id']
    text = jieba_cut(request.json['text'])
    result = {
        "Agent": "",
        "ImageURL": "",
        "Intent": "",
        "Reply": [],
        "ResolvedQuery": "",
        "Responses": [],
        "Result": [],
        "Score": 0,
        "Speech": "",
        "Success": True,
        "Threshold": 0.6
    }
    try:
        agent = load_json_db(str(system_id) + "," + str(agent_id))
        result["Agent"] = agent["agent_name"]
        for intent in agent["intents"]:
            for pharse in intent["pharse"]:
                source = check_similar(text,pharse["check_phrases"])/ len(text)
                result["Result"].append(
                    {
                        "Intent":intent["intent_name"],
                        "Source":source,
                        "phrase":pharse["training_phrases"]
                    }
                )
                if source > result["Score"]:
                    result["Score"] = source
                    result["Intent"] = intent["intent_name"]
                    result["Responses"] = intent["response_text"]
                    result["Speech"] = random.choice(intent["response_text"])
        return jsonify(result)
    except Exception as e:
        print('Exception:',e)
        return jsonify({"Success":False})


@app.route('/sentence_similar',methods=['POST'])
def sentence_similar():
    test_text1 = request.json['text1']
    test_text2 = request.json['text2']
    result = check_sentence_similar(test_text1,test_text2)
    return jsonify(result)


def jieba_cut(text):
    output = []
    check_output = []
    cut_text = jieba.cut(text, cut_all=False)

    for t in cut_text:
        if t not in stopword_set:
            output.append(t)
    print("Before check:", output)

    for op in output:
        try:
            model.most_similar(positive=[op], topn=10)
            check_output.append(op)
        except Exception as ex:
            similar = wiki_model.get_nn(op)
            check_output.append(similar[0]["key"])

    print("After check:", check_output)

    return check_output


def check_similar(check_output1,check_output2):
    total_source = 0
    for c_op1 in check_output1:
        source = 0
        for c_op2 in check_output2:
            t_source = model.similarity(c_op1, c_op2)
            source = t_source if t_source > source else source
        total_source += source
    return total_source


def check_sentence_similar(test_text1,test_text2):
    check_output1 = jieba_cut(test_text1)
    check_output2 = jieba_cut(test_text2)
    total_source = check_similar(check_output1,check_output2)
    print("Total source:", total_source / len(check_output1))
    return {
            "similar": total_source / len(check_output1)
            }


def serve_init():
    agents = db.collection('agents')
    agents = agents.get()
    for agent in agents:
        agent = db.collection('agents').document(agent.id)
        file_name = agent.id
        agent = ast.literal_eval(format(str(agent.get().to_dict())))
        write_json_db(file_name, agent)


def load_json_db(filename):
    with open('database/'+filename+'.json') as f:
        data = json.load(f)
        return data


def write_json_db(name, data):
    with open('database/' + name + '.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    cred = credentials.Certificate('/Users/wilsonlo/Desktop/word_representations_fasttext/source/fasttext-milk-tea.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    serve_init()
    app.run(host="127.0.0.1", port=5000)