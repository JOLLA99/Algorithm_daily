from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
f_queue, j_queue = deque(), deque()
f_visited, j_visited = [[0]*C for _ in range(R)], [[0]*C for _ in range(R)]

#이동방향 네가지방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(): #너비우선탐색
    
    # 불의 경로
    while f_queue:
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #위치를 벗어나지 않는지
            if R>nx>=0 and  C>ny >= 0:
                if not f_visited[nx][ny] and graph[nx][ny] != '#':
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append([nx, ny])

    
    # 지훈의 경로
    while j_queue:
        x, y = j_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #위치를 벗어나지 않는지
            if R>nx>=0 and  C>ny >= 0:
                if not j_visited[nx][ny] and graph[nx][ny] != '#':
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))                 
            else:
                return j_visited[x][y] + 1 #탈출
    
    return 'IMPOSSIBLE'

for i in range(R):
    for j in range(C):
        if graph[i][j]=='F':
            f_queue.append((i, j))
        elif graph[i][j]=='J':
            j_queue.append((i, j))

print(bfs())
