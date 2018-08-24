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