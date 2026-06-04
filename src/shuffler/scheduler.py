import random


def random_topological_sort(graph):

    indegree = dict(
        graph.in_degree()
    )

    ready = [
        node
        for node, degree
        in indegree.items()
        if degree == 0
    ]

    result = []

    while ready:

        chosen = random.choice(
            ready
        )

        ready.remove(chosen)

        result.append(chosen)

        for child in graph.successors(
            chosen
        ):

            indegree[child] -= 1

            if indegree[child] == 0:

                ready.append(child)

    return result