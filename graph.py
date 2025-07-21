# graph.py
import heapq

class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, start, end, wt):
        self.g.setdefault(start, []).append((end, wt))
        self.g.setdefault(end, []).append((start, wt))

    def dijkstra(self, start, end):
        dist = {city: float('inf') for city in self.g}
        dist[start] = 0
        prev = {}
        pq = [(0, start)]

        while pq:
            d, city = heapq.heappop(pq)
            for neighbor, wt in self.g[city]:
                if dist[city] + wt < dist[neighbor]:
                    dist[neighbor] = dist[city] + wt
                    prev[neighbor] = city
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        path = []
        at = end
        while at in prev:
            path.append(at)
            at = prev[at]
        if start != end:
            path.append(start)
        return path[::-1], dist[end]
