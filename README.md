# word_representations_fasttext
A word representations base on fasttext

## setup
1.FastTextNN.py -> Modify FASTTEXT_PATH, NUM_NEIGHBORS <br >
2.Run docker file or pip install -r requirements.txt

## json format
Single_words:/gensim_single_text <br >
Key: <br >
text1 - string
```json
{
	"text1":"足球"
}
```


Double_words:/gensim_double_text
Key: <br >
text1 - string
text2 - string
```json
{
	"text1":"足球",
	"text2":"籃球"
}
```

Single_words_fattext:/fasttext_single_text
key: <br >
text1:string
```json
{
	"text1":"足球"
}
```
