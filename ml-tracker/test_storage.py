import json
from pathlib import Path
from models import Run
from storage import load_runs, save_runs

def test_load_runs_missing_file(tmp_path):
    path = tmp_path / "runs.json"

    # pas de fichier → doit retourner []
    empty_runs = load_runs(Path(path).expanduser())
    assert len(empty_runs) == 0

def test_round_trip(tmp_path):
    path = tmp_path / "runs.json"
    runs = [Run(id=1, model="rf", accuracy=0.82)]
    save_runs(path, runs)
    loaded = load_runs(path)

    # vérifie id, model, accuracy du run chargé
    assert len(loaded) == 1
    run = loaded[0]
    assert run.id == 1
    assert run.model == "rf"
    assert run.accuracy == 0.82

def test_sort_index_not_in_json(tmp_path):
    path = tmp_path / "runs.json"
    save_runs(path, [Run(id=1, model="rf", accuracy=0.82)])
    data = json.loads(path.read_text())

    # vérifie que "sort_index" n'est pas dans data[0]
    assert "sort_index" not in data[0]
