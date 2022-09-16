import fileinput
import sys

import libcst as cst
from libcst.metadata import PositionProvider

SURROUNDING_LINES = 4
ANSI_RESET = '\033[0m'
ANSI_BOLD = '\033[1m'
ANSI_GREEN = '\033[92m'

cat = ''.join


class Visitor(cst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def visit_ConcatenatedString(self, node):
        code_range = self.get_metadata(PositionProvider, node)
        start = code_range.start.line
        end = code_range.end.line

        print(f'{ANSI_BOLD}{sys.argv[-1]}:{start}{ANSI_RESET}')
        print(cat(data[max(start-SURROUNDING_LINES-1, 0):start-1]), end='')
        print(ANSI_GREEN, end='')
        print(cat(data[start-1:end]), end='')
        print(ANSI_RESET, end='')
        print(cat(data[end:end+SURROUNDING_LINES]), end='')
        print()


data = list(fileinput.input())

try:
    module = cst.parse_module(cat(data))
    wrapper = cst.MetadataWrapper(module)
    wrapper.visit(Visitor())
except Exception as e:
    print(f"{ANSI_BOLD}{sys.argv[-1]}{ANSI_RESET}")
    raise e
