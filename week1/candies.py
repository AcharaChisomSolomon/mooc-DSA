def count(a, b, c):
    min_val = min(a, b)
    max_val = max(a, b)
    remainder = c % min_val
    return (c // min_val) + (remainder // max_val)


if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4