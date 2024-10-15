import sys
from collections import deque

def bfs(s, start, targets):
    n = len(s)
    queue = deque([(start, 0)])
    visited = [False] * n
    visited[start] = True
    found_targets = set()

    while queue:
        pos, steps = queue.popleft()
        if s[pos] in targets:
            found_targets.add(s[pos])
            if len(found_targets) == 1:
                return steps
        for next_pos in [pos-1, pos+1]:
            if 0 <= next_pos < n and not visited[next_pos] and s[next_pos] != '#':
                visited[next_pos] = True
                queue.append((next_pos, steps+1))
                
    return -1

s = input().strip()
r_s = s.index('R')
b_s = s.index('B')
g_s = s.index('G')

r_steps = bfs(s, r_s, {'B', 'G'})
b_steps = bfs(s, b_s, {'R', 'G'})
g_steps = bfs(s, g_s, {'R', 'B'})

print(r_steps, b_steps, g_steps)
