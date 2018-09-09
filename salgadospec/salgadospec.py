from tempfile import TemporaryFile
import time
import traceback

ANSI_RESET = '\x1b[0m'
ANSI_RED = '\x1b[31m'
ANSI_GREEN = '\x1b[32m'
ANSI_YELLOW = '\x1b[33m'

SKIPPED_MARK = f'{ANSI_YELLOW}*{ANSI_RESET}'
PASSED_MARK = f'{ANSI_GREEN}.{ANSI_RESET}'
FAILURE_MARK = f'{ANSI_RED}F{ANSI_RESET}'


class SalgadoSpecFailure(Exception):
    pass


class expect(object):
    def __init__(self, actual):
        self.actual = actual

    def __lt__(self, value):
        if not self.actual.__lt__(value):
            raise SalgadoSpecFailure(f'expected: < {value}',
                                     f'     got:   {self.actual}')

    def __le__(self, value):
        if not self.actual.__le__(value):
            raise SalgadoSpecFailure(f'expected: <= {value}',
                                     f'     got:    {self.actual}')

    def __eq__(self, value):
        if not self.actual.__eq__(value):
            raise SalgadoSpecFailure(f'expected: {value}',
                                     f'     got: {self.actual}')

    def __ne__(self, value):
        if not self.actual.__ne__(value):
            raise SalgadoSpecFailure(f'expected not: {value}',
                                     f'         got: {self.actual}')

    def __gt__(self, value):
        if not self.actual.__gt__(value):
            raise SalgadoSpecFailure(f'expected: > {value}',
                                     f'     got:   {self.actual}')

    def __ge__(self, value):
        if not self.actual.__ge__(value):
            raise SalgadoSpecFailure(f'expected: >= {value}',
                                     f'     got:    {self.actual}')

    @property
    def to_be(self):
        return self


def run_specs(locals_):
    examples = {fn: SKIPPED_MARK
                for fn_name, fn in locals_.items()
                if fn_name.startswith('it_') and callable(fn)}

    with TemporaryFile(mode='w+') as fp:
        def print_t(*args, **kwargs):
            print(*args, **kwargs, file=fp)

        tick = time.time()
        for example in examples.keys():
            print_t(f' - {example.__name__.replace("it_", "", 1)}', end=' ')
            try:
                example()
            except Exception as e:
                examples[example] = FAILURE_MARK
                print_t(f'{ANSI_RED}(FAILURE)')

                if isinstance(e, SalgadoSpecFailure) and e.args:
                    for arg in e.args:
                        print_t('  ', arg)

                traceback_lines = traceback.format_exc().splitlines()
                print_t('  ', traceback_lines[0])
                if isinstance(e, SalgadoSpecFailure):
                    traceback_lines = traceback_lines[:-3]
                for line in traceback_lines[3:]:
                    print_t('  ', line)
                print_t(ANSI_RESET, end='')

                continue

            examples[example] = PASSED_MARK
            print_t(f'{ANSI_GREEN}(OK){ANSI_RESET}')
        tack = time.time()

        print(''.join(examples.values()))
        print()

        fp.seek(0)
        print(fp.read())

    failures = [example
                for example, mark in examples.items()
                if mark == FAILURE_MARK]

    print(f'Finished in {tack-tick:.6f} seconds')

    if len(failures) == 0:
        print(ANSI_GREEN, end='')
    else:
        print(ANSI_RED, end='')
    print(f'{len(examples)} example{"s" if len(examples) > 1 else ""}, '
          f'{len(failures)} failure{"s" if len(failures) > 1 else ""}',
          end='')
    print(ANSI_RESET)
