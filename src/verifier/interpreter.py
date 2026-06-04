class Interpreter:

    def __init__(self):

        self.variables = {}

    def get_value(self, token):

        if token.isdigit():
            return int(token)

        return self.variables[token]

    def execute(self, instructions):

        output = []

        for inst in instructions:

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
                    self.get_value(inst.arg1)
                    +
                    self.get_value(inst.arg2)
                )

            elif inst.op == "print":

                output.append(
                    str(
                        self.get_value(
                            inst.arg1
                        )
                    )
                )

        return output