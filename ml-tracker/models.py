from dataclasses import dataclass, field
from datetime import datetime

@dataclass(order=True)
class Run:
    sort_index: float = field(init=False, repr=False)
    id: int
    model: str
    accuracy: float
    dataset: str = ""
    params: str = ""
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def __post_init__(self):
        self.sort_index = self.accuracy

