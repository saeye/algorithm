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

# start를 인자로 받아 탐색을 시작하는 bfs 함수
def bfs_queue(start):
    visited = [start] # 방문 노드를 기록하는 리스트 visited에 start 노드 추가
    q = deque([start]) # 탐색 노드 q에 start 노드 추가

    # 큐가 비어있지 않으면 계속 반복
    while q:
        node = q.popleft() # 큐의 맨 왼쪽 값을 빼서 node에 저장
        # 현재 노드의 인접 노드들을 for문으로 반복
        for adj in graph[node]:
            # 만약 인접 노드가 방문한 노드 리스트에 없으면
            if adj not in visited:
                visited.append(adj) # 방문한 노드 리스트에 추가
                q.append(adj) # 큐에도 추가

    # 큐가 비어있으면 반복문을 끝내고 방문한 노드 리스트 반환
    return visited

print(bfs_queue(1))
