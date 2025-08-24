import numpy as np
from strsimpy.ngram import NGram

def _get_mean_embedding(tokens, model):
    """
    Get the mean embedding of a token.
        If len(token) > 1, then get the average of each subtoken.
        If len(token) == 1, then get the embedding of that token.
    
    Args:
        token (STRING)         a word
        model (fastText Model) an unsupervised word embedding model
    """

    embeddings = np.array([model.get_word_vector(token) for token in tokens])
    mean_emb = embeddings.mean(axis=0)

    mean_emb /= np.linalg.norm(mean_emb) + 1e-12
    return mean_emb

def _bisim(s_1, s_2):
    """
    Get the BISIM of two strings [Kondrak].

    Args:
        s_1 (STRING) the first string
        s_2 (STRING) the second string
    """
    return 1 - NGram(2).distance(s_1, s_2)

def get_similarity(query_drugs, model, alpha, beta):
    """
    Get the pairwise weighted semantic (by cosine similarity) and orthographic 
    (by BISIM; Bigram similarity) similarity of two drugs from a sequence.

    Returns a matrix of similarities.

    Args:
        query_drugs ([]STRING)       a list of drug names
        model       (fastText Model) an unsupervised word embedding model
        alpha       ([0,1])          the weight of semantic similarity 
        beta        ([0,1])          the weight of orthographic similarity
    
    Ensure:
        alpha + beta = 1
        
    """

    drug_embeddings = np.array(
        [_get_mean_embedding(drug.split(), model) for drug in query_drugs]
    )

    n = len(query_drugs)
    sim_adj = np.zeros((n, n))

    # Compute adjusted similarity
    for i in range(n):
        for j in range(n):
            cos_sim = np.dot(drug_embeddings[i], drug_embeddings[j])
            ortho = _bisim(query_drugs[i].lower(), query_drugs[j].lower())
            if ortho > 0.8:
                sim_adj[i, j] = ortho

            sim_adj[i, j] = cos_sim * alpha + ortho * beta

    if len(query_drugs) == 2:
        return sim_adj[0][1]
    else:
        return sim_adj  
