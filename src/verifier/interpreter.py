class Interpreter:

    def __init__(self):

        self.variables = {}

    def get_value(self, token):

        if token.isdigit():
            return int(token)

        return self.variables[token]

    def execute(self, instructions):

        output = []

        labels = {}

        for idx, inst in enumerate(
            instructions
        ):

            if inst.op == "label":

                labels[
                    inst.arg1
                ] = idx

        pc = 0

        while pc < len(instructions):

            inst = instructions[pc]

            if inst.op == "assign":

                self.variables[
                    inst.dest
                ] = self.get_value(
                    inst.arg1
                )

            elif inst.op == "+":

                self.variables[
                    inst.dest
                ] = (
                    self.get_value(
                        inst.arg1
                    )
                    +
                    self.get_value(
                        inst.arg2
                    )
                )

            elif inst.op == "-":

                self.variables[
                    inst.dest
                ] = (
                    self.get_value(
                        inst.arg1
                    )
                    -
                    self.get_value(
                        inst.arg2
                    )
                )

            elif inst.op == "*":

                self.variables[
                    inst.dest
                ] = (
                    self.get_value(
                        inst.arg1
                    )
                    *
                    self.get_value(
                        inst.arg2
                    )
                )

            elif inst.op == "/":

                self.variables[
                    inst.dest
                ] = (
                    self.get_value(
                        inst.arg1
                    )
                    //
                    self.get_value(
                        inst.arg2
                    )
                )

            elif inst.op == "print":

                output.append(
                    str(
                        self.get_value(
                            inst.arg1
                        )
                    )
                )

            elif inst.op == "goto":

                pc = labels[
                    inst.arg1
                ]

                continue

            elif inst.op == "ifgoto":

                if self.get_value(
                    inst.arg1
                ) != 0:

                    pc = labels[
                        inst.arg2
                    ]

                    continue

            pc += 1

        return output