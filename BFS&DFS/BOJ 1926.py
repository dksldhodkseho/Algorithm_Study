from collections import deque
def bfs(x,y):
    picture[x][y] = 0
    q = deque()
    q.append([x,y])
    scale = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1:
                q.append([nx,ny])
                picture[nx][ny] = 0
                scale += 1
    return scale

n, m = map(int,input().split())
picture = [list(map(int,input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            cnt += 1
            result = max(bfs(i,j), result)
print(cnt)
print(result)
