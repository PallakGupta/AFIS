import random


def reorder_blocks(blocks):

    if len(blocks) <= 1:
        return blocks

    first = blocks[0]

    rest = blocks[1:]

    random.shuffle(rest)

    return [first] + rest