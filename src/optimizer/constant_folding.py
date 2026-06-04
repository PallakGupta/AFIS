from ir.instruction import Instruction


def constant_fold(program):

    optimized = []

    for inst in program:

        if (
            inst.op in ["+", "-", "*", "/"]
            and inst.arg1.isdigit()
            and inst.arg2.isdigit()
        ):

            left = int(inst.arg1)
            right = int(inst.arg2)

            if inst.op == "+":
                value = left + right

            elif inst.op == "-":
                value = left - right

            elif inst.op == "*":
                value = left * right

            elif inst.op == "/":
                value = left // right

            optimized.append(
                Instruction(
                    "assign",
                    inst.dest,
                    str(value)
                )
            )

        else:

            optimized.append(inst)

    return optimized