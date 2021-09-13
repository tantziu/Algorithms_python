def is_route_available(graph, node1, node2):
        visited = set()
        stack = [node1]

        while stack:
            node = stack.pop()
            print(node)
            if node == node2:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)


if __name__ == '__main__':
    graph = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['6'],
        '4': [],
        '5': ['6'],
        '6': [],
        '7': []
    }

    print(is_route_available(graph, '1', '7'))
