def addr(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A]+reg[B]
    return reg


def addi(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A]+B
    return reg


def mulr(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A]*reg[B]
    return reg


def muli(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A]*B
    return reg


def banr(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A] & reg[B]
    return reg


def bani(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A] & B
    return reg


def borr(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A] | reg[B]
    return reg


def bori(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A] | B
    return reg


def setr(registers, A, B, C):
    reg = registers[:]
    reg[C] = reg[A]
    return reg


def seti(registers, A, B, C):
    reg = registers[:]
    reg[C] = A
    return reg


def gtir(registers, A, B, C):
    reg = registers[:]
    reg[C] = int(A > reg[B])
    return reg


def gtri(registers, A, B, C):
    reg = registers[:]
    reg[C] = int(reg[A] > B)
    return reg


def gtrr(registers, A, B, C):
    reg = registers[:]
    reg[C] = int(reg[A] > reg[B])
    return reg


def eqir(registers, A, B, C):
    reg = registers[:]
    reg[C] = int(A == reg[B])
    return reg


def eqri(registers, A, B, C):
    reg = registers[:]
    reg[C] = int(reg[A] == B)
    return reg


def eqrr(registers, A, B, C):
    reg = registers[:]
    reg[C] = int(reg[A] == reg[B])
    return reg
