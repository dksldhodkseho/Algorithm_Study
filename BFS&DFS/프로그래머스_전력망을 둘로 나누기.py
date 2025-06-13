from collections import deque
def dfs(n,graph,node):
    visited = [False for _ in range(n+1)]
    q = deque([node])
    visited[node] = True
    cnt = 1
    while q:
        x = q.pop()
        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    answer = n
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        answer = min(abs(dfs(n,graph,x)-dfs(n,graph,y)), answer)
        graph[x].append(y)
        graph[y].append(x)
    return answer
