import sys
import sys
# If you need to import additional packages or classes, please import here.

def func(n, arr):
    arr.sort(key=lambda x:x[0])
    total_range_start = arr[0][0]
    total_range_end = max(t[1] for t in arr)

    curr_end = total_range_start
    max_end = total_range_start
    count = 0
    i = 0

    while curr_end < total_range_end:
        while i < n and arr[i][0] <= curr_end:
            max_end = max(max_end, arr[i][1])
            i += 1
        if max_end == curr_end:
            return -1
        curr_end = max_end
        count += 1
    return count

if __name__ == "__main__":
    # input = sys.stdin.read().strip().split(' ')
    # n = int(input[0])

    # arr = []
    # for i in range(1, len(input), 2):
    #     t = [int(input[i]), int(input[i+1])]
    #     arr.append(t)
    n = 2
    arr = [[0, 4], [2, 5], [6, 7]]
        
    print(func(n, arr))
