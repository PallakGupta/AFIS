from optimizer.constant_propagation import (
    constant_propagation
)

from optimizer.constant_folding import (
    constant_fold
)

from optimizer.dead_code_elimination import (
    dead_code_elimination
)


def optimize(program):

    program = constant_propagation(
        program
    )

    program = constant_fold(
        program
    )

    program = dead_code_elimination(
        program
    )

    return program