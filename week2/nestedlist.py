def count(t):
    total = 0

    for i in range(len(t)):
        try:
            if int(t[i]):
                total += 1
        except:
            total += count(t[i])

    return total

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8