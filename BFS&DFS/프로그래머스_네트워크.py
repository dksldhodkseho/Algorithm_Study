from collections import deque
def dfs(computers, visited, node):
    q = deque([node])
    visited[node] = True
    
    while q:
        x = q.pop()
        for i in range(len(computers)):
            if computers[x][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1         
    return answer
