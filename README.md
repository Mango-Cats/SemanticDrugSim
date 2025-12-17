# SemanticDrugSim

| Author          | GitHub                                         |               |
|-----------------|-----------------------------------------------|--------------------|
| Stephen Borja   | [@OutForMilks](https://github.com/OutForMilks) |                    |
| Erin Chua       | [@chua-e](https://github.com/chua-e)           |                    |
| Gideon Chua     | [@hootawsneaks](https://github.com/hootawsneaks)|                   |
| Zhean Ganituen | [@zrygan](https://github.com/zrygan)           | *Correspondence*   |
| Nathaniel Oco |                                               | Faculty Adviser   |


Public GitHub repository for computing semantic drug similarity by unsupervised
learning using PubMed corpus and a fastText model.

This work has been accepted as a conference proceeding of the **28th International Conference of Oriental COCOSDA** and
will be presented on November 12–14, 2025, at Universitas Kristen Duta Wacana (UKDW), Yogyakarta, Indonesia.

## Supplementary Heatmaps

The conference proceeding references additional heatmaps not included in the paper.  
These supplementary materials are available in the [heatmaps/](/heatmaps) directory.

## Getting Started

Simply clone the repository:

```bash
$ git clone https://github.com/Mango-Cats/SemanticDrugSim
```

This project uses [uv](https://docs.astral.sh/uv/guides/install-python/) for
package and project management. The provided `init.ps1` script handles setup:
it installs `uv` if necessary, creates a Python virtual environment, and adds
all dependencies. Simply run:

```pwsh
.\init.ps1
```

> What this does, is it checks if `uv` installed and downloads it if not. Then,
activate the Python virtual environments (venv) and adds all dependencies to it.

## Repository Structure

- `main.py` — entry point for running the project.
- `heatmaps/`
- `similarity/` — scripts for computing semantic and orthographic similarity.
- `train/` — scripts for training the fastText model.
- `visualize/` — scripts for creating heatmaps.
- `corpus/` — Go and PowerShell scripts for extracting and parsing the corpus.
- `vendor/` — fastText `.whl` file.

## Citation

BibTeX:
```bib
  @software{Ganituen2025Software,
    author    = {Ganituen, Zhean Robby and Borja, Stephen and Chua, Erin Gabrielle and Chua, Gideon},
    title     = {{SemanticDrugSim}}
  }

  @inproceedings{Ganituen2025,
    author    = {Ganituen, Zhean Robby and Borja, Stephen and Chua, Erin Gabrielle and Chua, Gideon and Oco, Nathaniel},
    title     = {Integrating Semantic and Orthographic Features for Drug Name Similarity Analysis},
    booktitle = {Proceedings of the 28th International Conference of Oriental COCOSDA},
    year      = {2025},
    address   = {Yogyakarta, Indonesia},
    month     = {November}
  }
```

Also see [`CITATION.cff`](CITATION.cff)
