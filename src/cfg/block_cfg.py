import networkx as nx


def build_block_cfg(blocks):

    G = nx.DiGraph()

    for block in blocks:

        G.add_node(block.id)

    for i in range(len(blocks) - 1):

        G.add_edge(
            blocks[i].id,
            blocks[i + 1].id
        )

    return G