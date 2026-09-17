from dataclasses import dataclass


@dataclass(frozen=True)
class Evaluation:
    correctness: int
    clarity: int
    usefulness: int


def summarize(item: Evaluation) -> dict[str, object]:
    scores = (item.correctness, item.clarity, item.usefulness)
    if any(not 0 <= score <= 5 for score in scores):
        raise ValueError("each dimension must be from 0 to 5")
    weighted = item.correctness * 0.5 + item.clarity * 0.25 + item.usefulness * 0.25
    return {"score": weighted, "decision": "accept" if weighted >= 4 else "review"}
