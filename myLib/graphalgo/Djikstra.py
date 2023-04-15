class GraphAlgo:
    @staticmethod
    def dijkstra(graph, start_vertex):
        distances = [float('inf')] * graph.order
        distances[start_vertex] = 0
        visited = [False] * graph.order
        priority_queue = [(0, start_vertex)]  # (distance, vertex)

        while priority_queue:
            priority_queue.sort(key=lambda x: x[0])  # Sort based on distance
            current_distance, current_vertex = priority_queue.pop(0)
            if visited[current_vertex]:
                continue

            visited[current_vertex] = True
            for neighbor, weight in graph.graph_structure[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    priority_queue.append((new_distance, neighbor))

        return distances
