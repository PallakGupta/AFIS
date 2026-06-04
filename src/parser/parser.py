import re

from ir.instruction import Instruction


class Parser:

    def parse_line(self, line):

        line = line.strip()

        if not line:
            return None

        if line.startswith("print"):

            value = line.split()[1]

            return Instruction(
                "print",
                arg1=value
            )

        arithmetic = re.match(
            r'(\w+)\s*=\s*(\w+)\s*([\+\-\*/])\s*(\w+)',
            line
        )

        if arithmetic:

            dest, left, op, right = arithmetic.groups()

            return Instruction(
                op,
                dest,
                left,
                right
            )

        assign = re.match(
            r'(\w+)\s*=\s*(\w+)',
            line
        )

        if assign:

            dest, value = assign.groups()

            return Instruction(
                "assign",
                dest,
                value
            )

        raise Exception(
            f"Cannot parse: {line}"
        )

    def parse_file(self, filename):

        instructions = []

        with open(filename) as f:

            for line in f:

                inst = self.parse_line(line)

                if inst:
                    instructions.append(inst)

        return instructions