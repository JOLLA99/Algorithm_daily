from collections import deque
import queue


T = int(input()) #테스트 케이스 개수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    
    return

for i in range(T):

    N, M, K = map(int, input().split()) #가로길이, 세로길이, 배추 심어진 위치의 개수
    cnt = 0 
    graph = [[0]*M for _ in range(N)]

    for j in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt+=1
    
    print(cnt)
