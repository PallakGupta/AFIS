def dead_code_elimination(program):

    live = set()

    optimized = []

    for inst in reversed(program):

        keep = False

        if inst.op == "print":

            keep = True

            if inst.arg1:
                live.add(inst.arg1)

        elif inst.dest:

            if inst.dest in live:

                keep = True

                live.remove(inst.dest)

                if (
                    inst.arg1
                    and not inst.arg1.isdigit()
                ):
                    live.add(inst.arg1)

                if (
                    inst.arg2
                    and not inst.arg2.isdigit()
                ):
                    live.add(inst.arg2)

        else:

            keep = True

        if keep:
            optimized.append(inst)

    optimized.reverse()

    return optimized