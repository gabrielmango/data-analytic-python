from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Info:
    """Stores information for generating SQL scripts."""

    name: str
    path: str
    locate: str
    script: str = field(default_factory=str)
    components: List[str] = field(default_factory=list)
