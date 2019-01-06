% NOTE(mcsalgado): this was generated by day16_prolog_generator.py.

:- use_module(library(clpfd)).

behaves_like(seti, 0).
behaves_like(eqir, 13).
behaves_like(gtri, 10).
behaves_like(eqri, 8).
behaves_like(gtir, 13).
behaves_like(addr, 4).
behaves_like(seti, 4).
behaves_like(addi, 6).
behaves_like(addr, 15).
behaves_like(bori, 15).
behaves_like(bori, 0).
behaves_like(addr, 0).
behaves_like(seti, 8).
behaves_like(gtir, 10).
behaves_like(gtrr, 10).
behaves_like(gtri, 2).
behaves_like(borr, 10).
behaves_like(mulr, 9).
behaves_like(addi, 14).
behaves_like(borr, 5).
behaves_like(eqir, 1).
behaves_like(eqrr, 13).
behaves_like(muli, 10).
behaves_like(gtri, 13).
behaves_like(gtrr, 2).
behaves_like(muli, 3).
behaves_like(eqri, 11).
behaves_like(addi, 10).
behaves_like(mulr, 5).
behaves_like(bori, 1).
behaves_like(mulr, 12).
behaves_like(seti, 9).
behaves_like(addi, 5).
behaves_like(gtrr, 13).
behaves_like(setr, 15).
behaves_like(muli, 15).
behaves_like(eqri, 15).
behaves_like(addr, 10).
behaves_like(bori, 10).
behaves_like(bori, 5).
behaves_like(gtrr, 15).
behaves_like(gtir, 15).
behaves_like(addi, 1).
behaves_like(borr, 4).
behaves_like(seti, 13).
behaves_like(eqir, 15).
behaves_like(seti, 2).
behaves_like(gtir, 0).
behaves_like(borr, 9).
behaves_like(bori, 9).
behaves_like(setr, 10).
behaves_like(borr, 0).
behaves_like(gtrr, 8).
behaves_like(gtri, 0).
behaves_like(muli, 12).
behaves_like(bani, 15).
behaves_like(addi, 9).
behaves_like(bori, 6).
behaves_like(muli, 5).
behaves_like(seti, 10).
behaves_like(addi, 0).
behaves_like(addr, 9).
behaves_like(gtrr, 0).
behaves_like(mulr, 7).
behaves_like(mulr, 10).
behaves_like(addi, 12).
behaves_like(eqrr, 1).
behaves_like(setr, 0).
behaves_like(addr, 5).
behaves_like(mulr, 14).
behaves_like(bani, 10).
behaves_like(banr, 10).
behaves_like(bori, 3).
behaves_like(addr, 12).
behaves_like(mulr, 3).
behaves_like(eqri, 13).
behaves_like(borr, 15).
behaves_like(eqri, 4).
behaves_like(seti, 11).
behaves_like(addi, 3).
behaves_like(eqir, 4).

solve(Opcodes) :-
    Instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr],
    same_length(Instructions, Opcodes),
    all_different(Opcodes),
    maplist(behaves_like, Instructions, Opcodes).
