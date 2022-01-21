from collections import deque

def bfs(x, y): #너비우선탐색
    
    #deque 생성
    queue = deque()
    queue.append((x, y))

    #이동방향 네가지방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #위치를 벗어나지 않는지
            if nx<0 or nx>=n or ny <0 or ny>=m:
                continue
            #벽이라 못감
            if graph[nx][ny] == 0:
                continue
            #벽이 아니라 진행 가능
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

print(bfs(0, 0))
