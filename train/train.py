import os
import datetime
import sys
import fasttext

def train_model(corpus_file_name, save_model = False):
    """
    Trains a fastText Model from a corpus using unsupervised learning.

    Args:
        corpus_file_name (STRING) the file name of the corpus
        save_model       (BOOL)   save the model or no
            DEFAULT: False
    """
    
    if not os.path.isfile(corpus_file_name):
        print(f"Error: The file '{corpus_file_name}' does not exist.")
        sys.exit(1)
    if not corpus_file_name.endswith(".txt"):
        print(f"Error: The file '{corpus_file_name}' is not a text file.")
        sys.exit(1)

    # train model using fasttext
    model = fasttext.train_unsupervised(input=corpus_file_name)

    # shove the model in somewhere
    # <zrygan> I'm gonna be honest, i don't know what this fucking does
    # (more like, why save it for later) i'll just put it here for
    # bookkeeping purposes
    output_dir = "models"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model_file = os.path.join(output_dir, f"MODEL_{timestamp}.bin")

    assert model
    if save_model:
        model.save_model(model_file)

    return model