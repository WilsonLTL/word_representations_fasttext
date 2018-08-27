# sentence_similar
A NLP system basic on word_representation_fasttext

## setup
To make sure the system run, please modify the soure/fasttext-milk-tea, which is the google credentials to connect the firestore

## database structure
agents <br >
-system_id, agent_id <br >
--agent_id : int <br >
--agent_name : string <br >
    --intent : object <br >
    ---intent_name : string <br >
    ---response_text : string <br >
        ---pharse : object <br >
        ----check_phrases : array <br >
        ----train_phrases : array <br >

## API Format:
POST:insert_update_record <br >
Input:
```json
{
	"system_id":12312,
	"agent":[
		{
		"agent_id": 1290378912,
		"agent_name": "天氣資訊",
         "intents": [
            {
              "intent_name": "天氣資訊_麵包出爐時間",
              "training_phrases": [
                "麵包幾時會出爐","幾時有新鮮麵包食","菠蘿包幾時會出爐","新一輪麵包幾時會有"
              ],
              "response_text": ["新鮮麵包會喺下晝兩點鐘出爐"]
            },
            {
              "intent_name": "麵包舖_蛋糕訂購",
              "training_phrases": [
                "你哋麵包舖有咩蛋糕","你哋麵包舖可唔可以訂蛋糕","有冇得訂蛋糕","訂蛋糕幾多錢"
              ],
              "response_text": ["我哋鋪頭提供為客戶訂製蛋糕服務,如果有你有興趣,歡迎隨時同我哋聯絡"]
            },
            {
            	"intent_name": "麵包舖_地址",
              "training_phrases": [
                "你哋麵包舖地址喺邊度","麵包舖地址","點樣去你哋到"
              ],
              "response_text":["喺科學園3/4月台上車,15分鐘之後落車就到㗎啦"]
            },
            {
            	"intent_name": "麵包舖_麵包款式",
              "training_phrases": [
                "你哋有咩麵包款式","麵包舖有咩特色麵包","你哋有咩麵包"
              ],
              "response_text": ["基本上你諗到嘅都有,快啲嚟睇吓啦"]
            }
          ]}]
}
```
Output:<br >
```json
{
    "agent_id": 1290378912,
    "agent_name": "天氣資訊",
    "intents": [
        {
            "intent_name": "天氣資訊_麵包出爐時間",
            "pharse": [
                {
                    "check_phrases": [
                        "犬貓",
                        "出爐"
                    ],
                    "training_phrases": "麵包幾時會出爐"
                },
                {
                    "check_phrases": [
                        "新鮮",
                        "犬貓",
                        "食"
                    ],
                    "training_phrases": "幾時有新鮮麵包食"
                },
                {
                    "check_phrases": [
                        "菠蘿包",
                        "出爐"
                    ],
                    "training_phrases": "菠蘿包幾時會出爐"
                },
                {
                    "check_phrases": [
                        "新一輪",
                        "犬貓"
                    ],
                    "training_phrases": "新一輪麵包幾時會有"
                }
            ],
            "response_text": [
                "新鮮麵包會喺下晝兩點鐘出爐"
            ]
        },
        {
            "intent_name": "麵包舖_蛋糕訂購",
            "pharse": [
                {
                    "check_phrases": [
                        "哋",
                        "犬貓",
                        "舖",
                        "咩",
                        "蛋糕"
                    ],
                    "training_phrases": "你哋麵包舖有咩蛋糕"
                },
                {
                    "check_phrases": [
                        "哋",
                        "犬貓",
                        "舖",
                        "唔",
                        "訂",
                        "蛋糕"
                    ],
                    "training_phrases": "你哋麵包舖可唔可以訂蛋糕"
                },
                {
                    "check_phrases": [
                        "冇",
                        "會向北",
                        "蛋糕"
                    ],
                    "training_phrases": "有冇得訂蛋糕"
                },
                {
                    "check_phrases": [
                        "訂",
                        "蛋糕",
                        "幾多",
                        "錢"
                    ],
                    "training_phrases": "訂蛋糕幾多錢"
                }
            ],
            "response_text": [
                "我哋鋪頭提供為客戶訂製蛋糕服務,如果有你有興趣,歡迎隨時同我哋聯絡"
            ]
        },
        {
            "intent_name": "麵包舖_地址",
            "pharse": [
                {
                    "check_phrases": [
                        "哋",
                        "犬貓",
                        "舖",
                        "地址",
                        "喺",
                        "邊度"
                    ],
                    "training_phrases": "你哋麵包舖地址喺邊度"
                },
                {
                    "check_phrases": [
                        "犬貓",
                        "舖",
                        "地址"
                    ],
                    "training_phrases": "麵包舖地址"
                },
                {
                    "check_phrases": [
                        "點樣",
                        "哋"
                    ],
                    "training_phrases": "點樣去你哋到"
                }
            ],
            "response_text": [
                "喺科學園3/4月台上車,15分鐘之後落車就到㗎啦"
            ]
        },
        {
            "intent_name": "麵包舖_麵包款式",
            "pharse": [
                {
                    "check_phrases": [
                        "哋",
                        "咩",
                        "犬貓",
                        "款式"
                    ],
                    "training_phrases": "你哋有咩麵包款式"
                },
                {
                    "check_phrases": [
                        "犬貓",
                        "舖",
                        "咩",
                        "特色",
                        "犬貓"
                    ],
                    "training_phrases": "麵包舖有咩特色麵包"
                },
                {
                    "check_phrases": [
                        "哋",
                        "咩",
                        "犬貓"
                    ],
                    "training_phrases": "你哋有咩麵包"
                }
            ],
            "response_text": [
                "基本上你諗到嘅都有,快啲嚟睇吓啦"
            ]
        }
    ]
}
```

POST:check_similar_by_agent
Input: <br >
```json
{
	"system_id":12312,
	"agent_id":1290378913,
	"text":"點樣去你哋鋪頭"
}
```

Output: <br >
```json
{
    "Agent": "麵包舖",
    "ImageURL": "",
    "Intent": "麵包舖_地址",
    "Reply": [],
    "ResolvedQuery": "",
    "Responses": [
        "喺科學園3/4月台上車,15分鐘之後落車就到㗎啦"
    ],
    "Result": [
        {
            "Intent": "麵包舖_麵包出爐時間",
            "Source": 0.26878772179285687,
            "phrase": "麵包幾時會出爐"
        },
        {
            "Intent": "麵包舖_麵包出爐時間",
            "Source": 0.33367232978343964,
            "phrase": "幾時有新鮮麵包食"
        },
        {
            "Intent": "麵包舖_麵包出爐時間",
            "Source": 0.3677930682897568,
            "phrase": "菠蘿包幾時會出爐"
        },
        {
            "Intent": "麵包舖_麵包出爐時間",
            "Source": 0.3010890980561574,
            "phrase": "新一輪麵包幾時會有"
        },
        {
            "Intent": "麵包舖_蛋糕訂購",
            "Source": 0.6848029394944509,
            "phrase": "你哋麵包舖有咩蛋糕"
        },
        {
            "Intent": "麵包舖_蛋糕訂購",
            "Source": 0.6848029394944509,
            "phrase": "你哋麵包舖可唔可以訂蛋糕"
        },
        {
            "Intent": "麵包舖_蛋糕訂購",
            "Source": 0.6057935059070587,
            "phrase": "有冇得訂蛋糕"
        },
        {
            "Intent": "麵包舖_蛋糕訂購",
            "Source": 0.453525314728419,
            "phrase": "訂蛋糕幾多錢"
        },
        {
            "Intent": "麵包舖_地址",
            "Source": 0.7016892731189728,
            "phrase": "你哋麵包舖地址喺邊度"
        },
        {
            "Intent": "麵包舖_地址",
            "Source": 0.38074665268262226,
            "phrase": "麵包舖地址"
        },
        {
            "Intent": "麵包舖_地址",
            "Source": 0.7556118071079254,
            "phrase": "點樣去你哋到"
        },
        {
            "Intent": "麵包舖_麵包款式",
            "Source": 0.6619700690110525,
            "phrase": "你哋有咩麵包款式"
        },
        {
            "Intent": "麵包舖_麵包款式",
            "Source": 0.47426729400952655,
            "phrase": "麵包舖有咩特色麵包"
        },
        {
            "Intent": "麵包舖_麵包款式",
            "Source": 0.6619700690110525,
            "phrase": "你哋有咩麵包"
        }
    ],
    "Score": 0.7556118071079254,
    "Speech": "喺科學園3/4月台上車,15分鐘之後落車就到㗎啦",
    "Success": true,
    "Threshold": 0.6
}
```