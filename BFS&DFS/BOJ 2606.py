from collections import deque
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True
    cnt = 0
    while q:
        com = q.popleft()
        for i in net[com]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

n = int(input())
v = int(input())
net = [[] for _ in range(n+1)]
for i in range(v):
    a,b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)
visited = [False for _ in range(n+1)]
print(bfs(1))
