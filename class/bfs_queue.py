from collections import deque

graph = {
1: [2, 3, 4],
2: [5],
3: [6, 7],
4: [8],
5: [9],
6: [10],
7: [],
8: [],
9: [],
10: [],
}

# start를 인자로 받아 탐색을 시작하는 bfs 함수 정의
def bfs_queue(start):
    visited = [start] # 방문한 노드 리스트
    q = deque([start])

    # q가 비어있지 않으면 계속 반복
    while q:
        # 일단 q의 맨 왼쪽에서 노드를 꺼낸다.
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                q.append(adj)

    return visited

print(bfs_queue(1))
bfs_queue(1)