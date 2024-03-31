def count(a, b):
    num_dict = {}

    for i in range(len(a)):
        num_dict[a[i]] = i

    for i in range(len(b)):
        num = b[i]
        if num_dict[num] < i:
            num_dict[num] = -1

    count = 0
    for num in num_dict:
        if num_dict[num] == -1:
            count += 1

    return count

if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5