from parser.parser import Parser

from cfg.block_builder import (
    build_blocks
)

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

blocks = build_blocks(
    program
)

for block in blocks:

    print(block)