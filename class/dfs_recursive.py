graph = {
1: [2, 5, 9],
2: [3],
3: [4],
4: [],
5: [6, 8],
6: [7],
7: [],
8: [],
9: [10],
10: [],
}

# 현재 노드와 여태까지 방문한 노드 두가지가 필요
def dfs_recursive(node, visited):
    # 방문한 노드 기록 (여태까지 방문한 노드에 현재 노드 추가)
    visited.append(node)

    # 현재 노드의 모든 인접 노드를 방문하는 반복문
    for adj in graph[node]:
        # 인접 노드가 여태까지 방문했던 노드에 없으면 (즉, 첫 방문이면)
        if adj not in visited:
            # 인접노드를 시작 노드로 재귀함수 호출
            dfs_recursive(adj, visited)

    # 여태까지 방문했던 노드 리스트 반환
    return visited

print(dfs_recursive(1, []))