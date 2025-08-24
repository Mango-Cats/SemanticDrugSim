import matplotlib.pyplot as plt
import seaborn as sns

def make_heat_map(drugs, similarity):
    """
    Create a heatmap of the drugs and each entry in the similarity matrix.
    
    Args:
        drugs      ([]STRING)  the list of drugs
        similarity ([][]FLOAT) the pairwise similarity of all drugs in drugs
    """
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        similarity,
        xticklabels=drugs,
        yticklabels=drugs,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
    )
    plt.title("Drug Similarity Heatmap")
    plt.show()