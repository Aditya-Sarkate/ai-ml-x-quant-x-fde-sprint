from dataclasses import asdict, dataclass


@dataclass
class Expense:
    """Represent a single expense."""

    id: int
    amount: float
    category: str
    description: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            id=int(data["id"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
            description=str(data["description"]),
        )
