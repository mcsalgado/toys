import ast
from collections.abc import Iterable
import fileinput
from functools import cache
import re
import sys

SURROUNDING_LINES = 4
ANSI_RESET = '\033[0m'
ANSI_BOLD = '\033[1m'
ANSI_GREEN = '\033[92m'

cat = ''.join

l = list(fileinput.input())


def visit(node):
    match node:
        case Iterable():
            for x in node:
                visit(x)
        case ast.AST(value=(ast.expr(elts=xs) | ast.Call(args=xs))):
            for x in xs:
                visit(x)
        case ast.AST(body=body):
            visit(body)
        case ast.Str():
            check_str(node)


@cache
def pattern(quotes):
    # TODO(mcsalgado): this pattern is not entirely correct but it's good enough for our purposes
    ret = re.compile(r'(?:^|\\\\|[^\\])' + quotes + r'''\s*["']''')
    return ret


def check_str(node):
    lit_list = [s.encode('utf-8') for s in l[node.lineno-1:node.end_lineno]]
    if len(lit_list) == 1:
        lit_list[0] = lit_list[0][node.col_offset:node.end_col_offset]
    else:
        lit_list[0] = lit_list[0][node.col_offset:]
        lit_list[-1] = lit_list[-1][:node.end_col_offset]

    lit = cat(b.decode('utf-8') for b in lit_list)

    if lit[0].isalpha():
        lit = lit[1:]

    if lit.startswith("'''") or lit.startswith('"""'):
        i = 3
    else:
        i = 1

    if lit.endswith("'''") or lit.endswith('"""'):
        j = 3
    else:
        j = 1

    if pattern(lit[:i]).search(lit[i:-j]):
        print(f'{ANSI_BOLD}{sys.argv[-1]}:{node.lineno}{ANSI_RESET}')
        print(cat(l[max(node.lineno-SURROUNDING_LINES-1, 0):node.lineno-1]), end='')
        print(ANSI_GREEN, end='')
        print(cat(l[node.lineno-1:node.end_lineno]), end='')
        print(ANSI_RESET, end='')
        print(cat(l[node.end_lineno:node.end_lineno+SURROUNDING_LINES]), end='')
        print()


try:
    visit(ast.parse(cat(l)))
except Exception as e:
    print(f'{ANSI_BOLD}{sys.argv[-1]}{ANSI_RESET}')
    raise e