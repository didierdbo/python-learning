from models import Run

def test_run_creation():
    run = Run(id=1, model="resnet", accuracy=0.95)
    assert run.id == 1
    assert run.model == "resnet"
    assert run.accuracy == 0.95

def test_sort_index_equals_accuracy():
    run = Run(id=1, model="resnet", accuracy=0.87)
    assert run.sort_index == run.accuracy

def test_ordering():
    run_a = Run(id=1, model="a", accuracy=0.80)
    run_b = Run(id=2, model="b", accuracy=0.95)
    assert max([run_a, run_b]) == run_b
