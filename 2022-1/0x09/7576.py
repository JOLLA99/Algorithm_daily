from collections import deque

def bfs(): #너비우선탐색
    
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #위치를 벗어나지 않는지
            if N>nx>=0 and  M>ny >= 0 and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                
 

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
res = 0

#deque 생성
queue = deque([])
#이동방향 네가지방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)