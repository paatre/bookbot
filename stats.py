def count_characters(text: str) -> dict[str, int]:
    counts = {}
    for char in text:
        if not char.isalpha():
            continue
        c = char.lower()
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def sort_by_num(char_nums: list[dict[str, int]]):
    return char_nums["num"]


def get_sorted_character_counts(text: str) -> list[dict[str, int]]:
    char_nums = []
    counts = count_characters(text)
    for char in counts:
        if not char.isalpha():
            continue
        char_nums.append({"char": char, "num": counts[char]})
    char_nums.sort(key=sort_by_num, reverse=True)
    return char_nums
