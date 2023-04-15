class DFS:
    @staticmethod
    def dfs(graph, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for i in range(len(graph[vertex])):
            neighbor = graph[vertex][i]
            if not visited[neighbor]:
                DFS.dfs(graph, neighbor, visited)
