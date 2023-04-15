class BFS:
    @staticmethod
    def bfs(graph, start_vertex):
        visited = [False] * len(graph)
        queue = [start_vertex]

        visited[start_vertex] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in range(len(graph[vertex])):
                neighbor = graph[vertex][i]
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
