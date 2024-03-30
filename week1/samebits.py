def count(string: str):
    return min(string.count('0'), string.count('1'))


if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4