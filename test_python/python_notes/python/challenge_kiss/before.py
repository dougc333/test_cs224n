def count_fruits(fruits: list[str]) -> dict[str, int]:
    from collections import Counter
    return dict(Counter(fruits))



def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}
    # add more tests


if __name__ == "__main__":
    main()
