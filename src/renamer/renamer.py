import random
from ir.instruction import Instruction


def rename_program(program):

    mapping = {}

    renamed_program = []

    for inst in program:

        if inst.dest:

            if inst.dest not in mapping:

                mapping[inst.dest] = (
                    "r"
                    + str(
                        random.randint(
                            1,
                            999
                        )
                    )
                )

        new_dest = inst.dest
        new_arg1 = inst.arg1
        new_arg2 = inst.arg2

        if (
            new_arg1
            and not new_arg1.isdigit()
            and new_arg1 in mapping
        ):
            new_arg1 = mapping[new_arg1]

        if (
            new_arg2
            and not new_arg2.isdigit()
            and new_arg2 in mapping
        ):
            new_arg2 = mapping[new_arg2]

        if (
            new_dest
            and new_dest in mapping
        ):
            new_dest = mapping[new_dest]

        renamed_program.append(

            Instruction(
                inst.op,
                new_dest,
                new_arg1,
                new_arg2
            )
        )

    return renamed_program