import sys
from collections import deque,defaultdict

def assign_groups(n, arr):
    graph = defaultdict(list)
    for i in range(n):
        for neighbor in arr[i]:
            graph[i].append(neighbor)
            graph[neighbor].append(i)
    group = [-1] * n
    
    def bfs(start):
        queue = deque([start])
        group[start] = 0
        while queue:
            node = queue.popleft()
            curr_group = group[node]
            next_group = 1 - curr_group
            for neighbor in graph[node]:
                if group[neighbor] == -1:
                    group[neighbor] = next_group
                    queue.append(neighbor)
                elif group[neighbor] == curr_group:
                    return False
        return True

    for i in range(n):
        if group[i] == -1:
            if not bfs(i):
                return -1
    
    group1 = []
    group2 = []
    for i in range(n):
        if group[i] == 0:
            group1.append(i)
        else:
            group2.append(i)

    if group1 > group2:
        group1, group2 = group2, group1
    
    return group1, group2
    
if __name__ == "__main__":
    input = sys.stdin.read().strip().split('\n')
    n = int(input[0])

    arr = []
    for i in range(1, len(input)):
        t = [int(x) for x in input[i].split(' ')]
        arr.append(t)
    
    result = assign_groups(n, arr)
    if result == -1:
        print(result)
    else:
        group1, group2 = result
        a = ""
        b = ""
        for x in group1:
            a = a + str(x) + " "
        for x in group2:
            b = b + str(x) + " "
        print(a[:-1])
        print(b[:-1])