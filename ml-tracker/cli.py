

#  python cli.py add --model STR --accuracy FLOAT [--dataset STR] [--params STR] [--notes STR]
#  python cli.py list
#  python cli.py best
#  python cli.py delete --id INT


import argparse
from storage import load_runs, save_runs
from models import Run
from pathlib import Path
from datetime import datetime

def format_run(run: Run) -> str:
   return f"#{run.id}\t{run.model}\tacc={run.accuracy:.3f}\t{run.dataset}\t[{run.notes}]\t{datetime.fromisoformat(run.timestamp).strftime('%Y-%m-%d')}"

parser = argparse.ArgumentParser(description="ML Experiment Tracker")
parser.add_argument("action", type=str, choices=["add", "list", "best", "delete"])
parser.add_argument("--model", type=str, help="model name")
parser.add_argument("--accuracy", type=float, help="accuracy score")
parser.add_argument("--dataset", type=str, help="dataset", )
parser.add_argument("--params", type=str, help="params")
parser.add_argument("--notes", type=str, help="notes")
parser.add_argument("--id", type=int, help="the id of the model you want to delete")

args = parser.parse_args()

path = Path("~/.ml-tracker/runs.json").expanduser()

if( args.action == "add"):
    runs = load_runs(path)
    ids = [r.id for r in runs]

    if len(ids) == 0:
        id = 1
    else:
        id = max(ids) + 1
    
    r = Run(id=id, model=args.model, accuracy=args.accuracy,
        dataset=args.dataset or "",
        params=args.params or "",
        notes=args.notes or "")

    runs.append(r)
    save_runs(path=path, runs=runs)

elif( args.action == "list"):
    runs = load_runs(path)
    for run in runs:
        print(format_run(run))

elif( args.action == "best"):
    runs = load_runs(path)
    print(format_run(max(runs)))

elif( args.action == "delete"):
    id = args.id
    runs = [r for r in load_runs(path) if not r.id == id]
    save_runs(path=path, runs=runs)
    