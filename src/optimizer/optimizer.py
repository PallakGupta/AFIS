from optimizer.constant_propagation import (
    constant_propagation
)

from optimizer.constant_folding import (
    constant_fold
)


def optimize(program):

    program = constant_propagation(
        program
    )

    program = constant_fold(
        program
    )

    return program