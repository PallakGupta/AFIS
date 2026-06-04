from parser.parser import Parser

from cfg.block_builder import (
    build_blocks
)

from cfg.block_scheduler import (
    reorder_blocks
)

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

blocks = build_blocks(program)

print("Original Blocks")
print()

for block in blocks:
    print(block)

print("------------------")
print()

reordered = reorder_blocks(
    blocks
)

print("Reordered Blocks")
print()

for block in reordered:
    print(block)