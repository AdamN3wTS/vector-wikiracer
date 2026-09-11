from fastembed import TextEmbedding
import numpy as np
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
def cos_similarity(v1,v2):
    return np.dot(v1,v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))
def vectorini(list_wiki,s_word,no_words):
    vectors = list(model.embed(list_wiki))
    word_vector = next(model.query_embed([s_word]))
    similarity=[]
    for word,vector in zip(list_wiki,vectors):
        value = cos_similarity(vector,word_vector)
        similarity.append({
            "word":word,
            "score":value
        })
    no_words_set = set(no_words)

    best_word, best_score = max(
        (
            (word, cos_similarity(vec, word_vector))
            for word, vec in zip(list_wiki, vectors)
            if word not in no_words_set
        ),
        key=lambda x: x[1],
        default=(None, -1.0)
    ) 
    return best_word,best_score


 
