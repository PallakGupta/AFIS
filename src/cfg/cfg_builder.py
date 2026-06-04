import networkx as nx


def build_cfg(program):

    G = nx.DiGraph()

    labels = {}

    for idx, inst in enumerate(program):

        if inst.op == "label":

            labels[inst.arg1] = idx

    for idx, inst in enumerate(program):

        G.add_node(idx)

        if inst.op == "goto":

            target = labels[
                inst.arg1
            ]

            G.add_edge(
                idx,
                target
            )

        elif inst.op == "ifgoto":

            target = labels[
                inst.arg2
            ]

            G.add_edge(
                idx,
                target
            )

            if idx + 1 < len(program):

                G.add_edge(
                    idx,
                    idx + 1
                )

        else:

            if idx + 1 < len(program):

                G.add_edge(
                    idx,
                    idx + 1
                )

    return G