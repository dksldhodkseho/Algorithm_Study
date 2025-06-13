from collections import deque
def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([0,0,1])
    visited = set()
    while q:
        x, y, d = q.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1:
            return d
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 0 and (nx,ny) not in visited:
                q.append([nx,ny,d+1])
    return -1
