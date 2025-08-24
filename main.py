import fasttext
from .similarity.similarity import get_similarity
from .visualize.heat_map import make_heat_map

if __name__ == "__main__":
    query_drugs = [
        "paracetamol", "acetaminophen", "ibuprofen", "naproxen", "aspirin", "celecoxib",
        "morphine", "oxycodone", "hydrocodone", "fentanyl", "tramadol",
        "amoxicillin", "ampicillin", "penicillin", "cloxacillin", "dicloxacillin",
        "cephalexin", "cefuroxime", "ceftriaxone", "cefepime", "cefotaxime",
        "azithromycin", "clarithromycin", "erythromycin", "roxithromycin", "telithromycin",
        "lisinopril", "enalapril", "captopril", "ramipril", "benazepril",
        "atenolol", "metoprolol", "propranolol", "carvedilol", "bisoprolol",
        "metformin", "glipizide", "glyburide", "pioglitazone", "sitagliptin",
        "atorvastatin", "simvastatin", "rosuvastatin", "pravastatin", "lovastatin",
        "fluoxetine", "sertraline", "citalopram", "escitalopram", "paroxetine"
    ]

    alpha = 0.75
    beta = 1 - alpha

    similarity = get_similarity(
        query_drugs, 
        fasttext.load_model("models/pubmed_model.bin"), 
        alpha, 
        beta
    )

    make_heat_map(query_drugs, similarity)
