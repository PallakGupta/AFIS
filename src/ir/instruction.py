class Instruction:

    def __init__(
        self,
        op,
        dest=None,
        arg1=None,
        arg2=None
    ):
        self.op = op
        self.dest = dest
        self.arg1 = arg1
        self.arg2 = arg2

    def __repr__(self):

        if self.op == "assign":

            return (
                f"{self.dest} = "
                f"{self.arg1}"
            )

        elif self.op in [
            "+",
            "-",
            "*",
            "/"
        ]:

            return (
                f"{self.dest} = "
                f"{self.arg1} "
                f"{self.op} "
                f"{self.arg2}"
            )

        elif self.op == "print":

            return (
                f"print "
                f"{self.arg1}"
            )

        return self.op