import networkx as nx


def build_graph(program):

    G = nx.DiGraph()

    last_write = {}

    for idx, inst in enumerate(program):

        G.add_node(idx)

        reads = []

        if inst.arg1:
            reads.append(inst.arg1)

        if inst.arg2:
            reads.append(inst.arg2)

        for var in reads:

            if var in last_write:

                G.add_edge(
                    last_write[var],
                    idx
                )

        if inst.dest:

            last_write[
                inst.dest
            ] = idx

    return G