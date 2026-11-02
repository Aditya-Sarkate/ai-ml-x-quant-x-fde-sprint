"""Day 1 Python practice functions."""


def sum_numbers(numbers: list[float]) -> float:
    return sum(numbers)


def find_min_max(numbers: list[float]) -> tuple[float, float]:
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return min(numbers), max(numbers)


def remove_duplicates(items: list) -> list:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def is_palindrome(text: str) -> bool:
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


def second_largest(numbers: list[int]) -> int:
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("at least two unique numbers are required")
    return unique_numbers[-2]


def highest_scoring_student(students: dict[str, float]) -> tuple[str, float]:
    if not students:
        raise ValueError("students cannot be empty")
    return max(students.items(), key=lambda item: item[1])


def statistics(numbers: list[float]) -> dict[str, float]:
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
    }


def safe_division(a: float, b: float) -> float | None:
    return None if b == 0 else a / b


if __name__ == "__main__":
    print(sum_numbers([1, 2, 3, 4]))
    print(find_min_max([5, 2, 9, 1]))
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    print(is_palindrome("Never odd or even"))
    print(second_largest([10, 5, 8, 10, 3]))
    print(highest_scoring_student({"Alice": 87, "Bob": 92, "Charlie": 89}))
    print(statistics([10, 20, 30, 40]))
    print(safe_division(10, 0))
