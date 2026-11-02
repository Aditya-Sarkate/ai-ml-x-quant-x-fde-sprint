"""Small examples covering Python fundamentals."""


def calculate_average(numbers: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list."""
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)


def count_even_odd(numbers: list[int]) -> dict[str, int]:
    """Count even and odd integers."""
    result = {"even": 0, "odd": 0}
    for number in numbers:
        result["even" if number % 2 == 0 else "odd"] += 1
    return result


def word_frequency(text: str) -> dict[str, int]:
    """Count words, ignoring case."""
    frequency: dict[str, int] = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def safe_divide(a: float, b: float) -> float:
    """Divide two numbers, raising ValueError for zero divisor."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(calculate_average([10, 20, 30, 40]))
    print(count_even_odd([1, 2, 3, 4]))
    print(word_frequency("Python is useful and Python is powerful"))
    print(safe_divide(10, 2))
