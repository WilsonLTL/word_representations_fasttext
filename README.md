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
	"text1":"俄羅斯"
}
```

Result:
```json
[
    [
        "烏克蘭",
        0.8838913440704346
    ],
    [
        "俄羅斯共",
        0.8792405128479004
    ],
    [
        "白俄羅斯",
        0.8624948263168335
    ],
    [
        "保加利亞",
        0.8233727812767029
    ],
    [
        "蘇聯",
        0.8143762350082397
    ],
    [
        "俄羅斯聯邦",
        0.8128169775009155
    ],
    [
        "頓涅斯克",
        0.8087301254272461
    ],
    [
        "羅馬尼亞",
        0.7969573140144348
    ],
    [
        "俄國",
        0.7956230044364929
    ],
    [
        "東歐",
        0.7940972447395325
    ]
]
```


Double_words:/gensim_double_text
Key: <br >
text1 - string
text2 - string
```json
{
	"text1":"俄羅斯",
	"text2":"新加坡"
}
```

Result:
```json
{
    "similar": "0.41096044"
}
```

Single_words_fattext:/fasttext_single_text
key: <br >
text1:string
```json
{
	"text1":"俄羅斯"
}
```

Result:
```json
[
    {
        "key": "烏克蘭",
        "value": "0.883891"
    },
    {
        "key": "俄羅斯共",
        "value": "0.87924"
    },
    {
        "key": "白俄羅斯",
        "value": "0.862494"
    },
    {
        "key": "保加利亞",
        "value": "0.823373"
    },
    {
        "key": "蘇聯",
        "value": "0.814376"
    },
    {
        "key": "俄羅斯聯邦",
        "value": "0.812817"
    },
    {
        "key": "頓涅斯克",
        "value": "0.80873"
    },
    {
        "key": "羅馬尼亞",
        "value": "0.796955"
    },
    {
        "key": "俄國",
        "value": "0.795623"
    },
    {
        "key": "東歐",
        "value": "0.794096"
    }
]
```