# Initialize the project for other people
# By: Zhean Ganituen (zrygan)
# On: August 2025

# uv is ok?
$uvCheck = Get-Command uv -ErrorAction SilentlyContinue

if (-not $uvCheck) {
    pip install uv
}

# venv is ok?
if (-not (Test-Path ".\venv")) {
    uv venv
}

& .venv\Scripts\activate
uv sync
uv pip list