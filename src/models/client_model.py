from dataclasses import dataclass

@dataclass
class Client:
    id: int = None
    name: str = ""
    email: str = ""