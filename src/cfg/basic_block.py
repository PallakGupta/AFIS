class BasicBlock:

    def __init__(
        self,
        block_id
    ):

        self.id = block_id

        self.instructions = []

    def add_instruction(
        self,
        instruction
    ):

        self.instructions.append(
            instruction
        )

    def __repr__(self):

        text = (
            f"Block {self.id}\n"
        )

        for inst in self.instructions:

            text += (
                f"  {inst}\n"
            )

        return text