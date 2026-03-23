def is_unique_bitmask_visualized(string):
    checker = 0
    width = max(ord(c) for c in string) + 1

    print(f"Input: '{string}'")
    print(f"{'char':<6} {'bit position':<14} {'checker (binary)'}")
    print("-" * 50)

    for char in string:
        bit = 1 << ord(char)
        if checker & bit:
            print(f"'{char}'    pos {ord(char):<10} DUPLICATE FOUND — return False")
            return False
        checker |= bit
        print(f"'{char}'    pos {ord(char):<10} {bin(checker)[2:].zfill(width)}")

    print("\nNo duplicates — return True")
    return True


if __name__ == "__main__":
    is_unique_bitmask_visualized("abc")
    print()
    is_unique_bitmask_visualized("abca")
