import sys
from collections import deque, defaultdict

def determine_winner(n, x, edges):
    graph = defaultdict(list)
    degree = [0] * (n+1)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    queue = deque()
    visited = [False] * (n+1)
    
    for i in range(1, n+1):
        if degree[i] == 1:
            queue.append(i)
            visited[i] = True
            
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)
                    visited[neighbor] = True
    
    if visited[x]:
        remaining_nodes = n - len(queue) - 1
        if remaining_nodes % 2 == 0:
            return "Pyrmont"
        else:
            return "Xiaoyo"
    else:
        return "Draw"

input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0])
index = 1
results = []

for _ in range(T):
    n, x = map(int, data[index].split())
    index += 1
    edges = []
    for _ in range(n):
        u, v = map(int, data[index].split())
        edges.append((u, v))
        index += 1
    result = determine_winner(n, x, edges)
    results.append(result)

for res in results:
    print(res)
    