import collections


def dfs_recursion(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursion(graph, neighbour, visited)


def bfs_recursion(graph, queue=None, visited=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = ['1']

    if queue:
        node = queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
        bfs_recursion(graph, queue, visited)


def dfs_with_stack(graph, node):
    visited = set()
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)

        if node not in visited:
            visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)


def bfs_with_queue(graph, node):
    visited = set()
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
        if node in graph.keys():
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


def get_adjacency_list(edges):
    result = collections.defaultdict(list)
    for source, destination in edges:
        # if result.get(source) is None:
        #     result[source] = [destination]
        # else:
        result[source].append(destination)
    return result


def from_adjacency_list_to_tree():
    return


def bfs_for_tree():
    return


if __name__ == '__main__':
    graph = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['6'],
        '4': [],
        '5': ['6'],
        '6': []
    }

    edges = [
        (1, 2),
        (1, 3),
        (2, 4),
        (2, 5),
        (3, 6),
        (5, 6)
    ]

    # dfs_recursion(graph, '1')
    # dfs_with_stack(graph, '1')
    # bfs_with_queue(graph, '1')
    # bfs_recursion(graph)

    # print(get_adjacency_list(edges))
