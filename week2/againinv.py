def create(n, k):
    arr = [i + 1 for i in range(n)]

    if k == 0:
        return arr
    
    def swap(arr, k=k, start=0):
        for i in range(len(arr) - 1, start, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            k -= 1
            if k == 0:
                break

        if k > 0:
            swap(arr, k, start + 1)

    swap(arr)

    return arr


if __name__ == "__main__":
    print(create(10, 34)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]