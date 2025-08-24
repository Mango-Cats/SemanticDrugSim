# SemanticDrugSim

Stephen Borja    [@OutForMilks](https://github.com/OutForMilks)     <br>
Erin Chua        [@chua-e](https://github.com/chua-e)               <br>
Gideon Chua      [@hootawsneaks](https://github.com/hootawsneaks)   <br>
Zhean Ganituen*  [@zrygan](https://github.com/zrygan)               <br>
Nathaniel Oco†                                                      <br>

\* **Correspondence**. Talk to Zhean via [`zhean_robby_ganituen@dlsu.edu.ph`](mailto:zhean_robby_ganituen@dlsu.edu.ph). <br>
† **Faculty Adviser**.

Public GitHub repository for computing semantic drug similarity by unsupervised
learning using PubMed corpus and a fastText model.

## Getting Started

Simply clone the repository:

```bash
$ git clone https://github.com/Mango-Cats/SemanticDrugSim
```

This project uses [uv](https://docs.astral.sh/uv/guides/install-python/) for
package and project managing. Don't worry the `init.ps1` will handle 
everything for you. So, simply run:

```pwsh
$ .\init.ps1
```

What this does, is it checks if `uv` installed and downloads it if not. Then,
activate the Python virtual environments (venv) and adds all dependencies to it.

## Moving Around

What your interested in is inside `./main.py` this contains the code that you
probably want to run.

- `./similarity/`: contains scripts used to compute semantic and orthographic 
similarity.
- `./train/`: contains the scripts used to train the fastText model (you will
probably not use this).
- `./visualize/`: contains the script to create the heatmap (you will also 
probably not use this).

Other files in the repository are `uv` project files.

- `./corpus/`: contains a Go file and a powershell script for extracting and parsing
the corpus (you will also probably not use this).
- `./vendor/`: contains the fastText `.whl` file.
