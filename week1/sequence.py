def generate(n: int):
    count = 0
    i = 1
    while True:
        if len(str(i)) == 1 or str(i)[0] == str(i)[-1]:
            count += 1
            if count == n:
                return i
            
        i += 1


if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141