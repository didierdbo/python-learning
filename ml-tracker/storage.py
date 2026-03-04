from pathlib import Path
from models import Run
import json
import dataclasses

def load_runs(path: Path) -> list[Run]:   
    if not path.exists():
        return []
    
    with open(path, "r") as file:
        data = json.load(file)

    return [Run(**r) for r in data]
    

def save_runs(path: Path, runs: list[Run]) -> None:
    # convert each Run dataclass into a dict
    datas = []
    for run in runs:
        data = dataclasses.asdict(run)
        del data["sort_index"]
        datas.append(data)

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as file:
        json.dump(datas, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    num = 0
    runs = load_runs(Path("~/.ml-tracker/runs.json").expanduser())
    print(num, runs)
    num+=1
    r = Run(id=num, model="m", accuracy=0.1*num)
    runs.append(r)
    save_runs(Path("~/.ml-tracker/runs.json").expanduser(), runs=runs)
    runs = load_runs(Path("~/.ml-tracker/runs.json").expanduser())
    print(num, runs)
    num+=1
    r = Run(id=num, model="m", accuracy=0.1*num)
    runs.append(r)
    save_runs(Path("~/.ml-tracker/runs.json").expanduser(), runs=runs)
    runs = load_runs(Path("~/.ml-tracker/runs.json").expanduser())
    print(num, runs)
    
