from ir.instruction import Instruction


def constant_propagation(program):

    constants = {}

    optimized = []

    for inst in program:

        new_inst = Instruction(
            inst.op,
            inst.dest,
            inst.arg1,
            inst.arg2
        )

        if (
            new_inst.arg1
            and new_inst.arg1 in constants
        ):
            new_inst.arg1 = (
                constants[
                    new_inst.arg1
                ]
            )

        if (
            new_inst.arg2
            and new_inst.arg2 in constants
        ):
            new_inst.arg2 = (
                constants[
                    new_inst.arg2
                ]
            )

        if (
            new_inst.op == "assign"
            and new_inst.arg1.isdigit()
        ):
            constants[
                new_inst.dest
            ] = new_inst.arg1

        optimized.append(
            new_inst
        )

    return optimized