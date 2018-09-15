def it_can_be_trivially_correct():
    expect(1+2).to_be == 3


def it_can_be_tricky_because_floats_amirite():
    expect(.1+.2).to_be == .3


def it_can_be_ok_now():
    expect(.1 + .2).to_be != .3


def it_can_fail_more():
    try:
        import math
        math.sqrt(-1)
    except:
        1/0

import salgadospec
