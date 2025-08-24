import fasttext
from similarity.similarity import get_similarity
from visualize.heat_map import make_heat_map

if __name__ == "__main__":
    query_drugs = [
        # add a list of drugs here
        # the drugs here are case-insensitive but ensure no non-alphabet
        # characters exist
    ]

    semantic_weight = .8
    orthographic_weight = 1 - semantic_weight

    similarity = get_similarity(
        query_drugs, 
        fasttext.load_model("drug_embedding_model.bin"), 
        semantic_weight,
        orthographic_weight, 
    )

    make_heat_map(query_drugs, similarity)
