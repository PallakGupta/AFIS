from cfg.basic_block import (
    BasicBlock
)


def build_blocks(program):

    leaders = {0}

    labels = {}

    for idx, inst in enumerate(program):

        if inst.op == "label":

            labels[
                inst.arg1
            ] = idx

    for idx, inst in enumerate(program):

        if inst.op in [
            "goto",
            "ifgoto"
        ]:

            if idx + 1 < len(program):

                leaders.add(
                    idx + 1
                )

            if inst.op == "goto":

                leaders.add(
                    labels[
                        inst.arg1
                    ]
                )

            if inst.op == "ifgoto":

                leaders.add(
                    labels[
                        inst.arg2
                    ]
                )

    leaders = sorted(
        list(leaders)
    )

    blocks = []

    for i in range(
        len(leaders)
    ):

        start = leaders[i]

        if i + 1 < len(leaders):

            end = leaders[
                i + 1
            ]

        else:

            end = len(program)

        block = BasicBlock(i)

        for inst in program[
            start:end
        ]:

            block.add_instruction(
                inst
            )

        blocks.append(
            block
        )

    return blocks