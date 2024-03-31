def create(n):
    arr = [i + 1 for i in range(n)]
    output = []
    # print('original',arr)

    if n == 1:
        return arr
    
    def circle(arr, output, start=1):
        # print(arr, output, start)
        if len(arr) <= 1:
            output += arr
            return
        
        for i in range(start, len(arr), 2):
            output.append(arr[i])

        # print(output[-1], arr[-1])
        prev_arr = arr[:]
        if start == 1:
            arr = arr[::2]
            if output[-1] != prev_arr[-1]:
                start = 0
            else:
                start = 1
        else:
            arr = arr[1::2]
            if output[-1] != prev_arr[-1]:
                start = 0
            else:
                start = 1

        circle(arr, output, start)

    circle(arr, output)

    return output


if __name__ == "__main__":
    # print(create(1)) # [1]
    print(create(8)) # [2,1,3]
    # print(create(9)) # [2,4,6,1,5,3,7]