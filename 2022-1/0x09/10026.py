from collections import deque

N = int(input().rstrip())
graph = [list(map(str, input())) for _ in range(N)]
graph_t = [[0]*N for _ in range(N)]


def bfs(i, j, color, arr):
    queue = deque()
    queue.append((i, j))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    arr[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if arr[nx][ny] == color:
                arr[nx][ny] = 0
                queue.append((nx, ny))


for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            graph_t[i][j] = 'R'
        else:
            graph_t[i][j] = 'B'

ans = 0
ans_f = 0

for i in range(N):
    for j in range(N):
        #적록색약 아닌 사람
        if graph[i][j] != 0:
            bfs(i, j, graph[i][j], graph)
            ans+=1
        #적록색약 사람
        if graph_t[i][j] != 0:
            bfs(i, j, graph_t[i][j], graph_t)
            ans_f+=1

print(ans, ans_f)

        