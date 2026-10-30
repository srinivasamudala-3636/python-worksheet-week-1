def calculate_statistics(numbers):
    if len(numbers) == 0:
        return {
            "mean": 0,
            "max": None,
            "min": None,
            "count": 0
        }

    result = {
        "mean": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "count": len(numbers)
    }

    return result

print(calculate_statistics([10, 20, 30, 40, 50]))
print(calculate_statistics([]))