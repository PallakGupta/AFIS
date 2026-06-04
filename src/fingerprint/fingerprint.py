import hashlib


def program_text(program):

    return "\n".join(
        str(inst)
        for inst in program
    )


def program_hash(program):

    text = program_text(program)

    return hashlib.sha256(
        text.encode()
    ).hexdigest()


def diversification_score(
    original_program,
    transformed_program
):

    original_hash = (
        program_hash(
            original_program
        )
    )

    transformed_hash = (
        program_hash(
            transformed_program
        )
    )

    score = 0

    for a, b in zip(
        original_hash,
        transformed_hash
    ):

        if a != b:
            score += 1

    return {
        "original_hash":
        original_hash,

        "transformed_hash":
        transformed_hash,

        "score":
        score
    }