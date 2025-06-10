from collections import deque
def bfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    home[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and home[nx][ny] == 1:
                home[nx][ny] = 0
                q.append([nx,ny])
                cnt += 1
    return cnt

n = int(input())
home = [list(map(int,input())) for _ in range(n)]
q = deque()
cnt_home = []
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            q.append([i,j])
            cnt_home.append(bfs(i,j))
cnt_home.sort()
print(len(cnt_home))
for i in cnt_home:
    print(i)
