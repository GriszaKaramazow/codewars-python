# This is the first part of this kata series. Second part is here.
#
# We want to create a simple interpreter of assembler which will support the following instructions:
#
# mov x y - copies y (either a constant value or the content of a register) into register x
# inc x - increases the content of register x by one
# dec x - decreases the content of register x by one
# jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward), but only if x (a
# constant or a register) is not zero
# Register names are alphabetical (letters only). Constants are always integers (positive or negative).
#
# Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous
# instruction, while an offset of 2 would skip over the next instruction.
#
# The function will take an input list with the sequence of the program instructions and will return a dictionary with
# the contents of the registers.
#
# Also, every inc/dec/jnz on a register will always be followed by a mov on the register first, so you don't need to
# worry about uninitialized registers.
#
# Example
# simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])
#
# ''' visualized:
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a
# ''''
# The above code will:
#
# set register a to 5,
# increase its value by 1,
# decrease its value by 2,
# then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
# and then increase its value by 1, leaving register a at 1
# So, the function should return
#
# {'a': 1}


def simple_assembler(program):
    result = dict()
    program_iter = 0
    while program_iter != len(program):
        step = program[program_iter].split()
        if step[0] == "mov" and step[2].isdigit():
            result[step[1]] = int(step[2])
            program_iter += 1
        elif step[0] == "mov" and step[2].isalpha():
            result[step[1]] = result[step[2]]
            program_iter += 1
        elif step[0] == "inc":
            if result[step[1]] < 409600:
                result[step[1]] += 1
            program_iter += 1
        elif step[0] == "dec":
            if result[step[1]] > -409600:
                result[step[1]] -= 1
            program_iter += 1
        elif step[0] == "jnz" and step[1].isdigit():
            program_iter += 1
        elif step[0] == "jnz" and result[step[1]] != 0:
            program_iter += int(step[2])
        elif step[0] == "jnz" and (result[step[1]] == 0 or step[1] == 0):
            program_iter += 1
    return result


tests = ((["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"], {'a': 1}),
         (["mov c 12", "mov b 0", "mov a 200", "dec a", "inc b", "jnz a -2", "dec c", "mov a b", "jnz c -5", "jnz 0 1",
           "mov c a"], {'a': 409600, 'c': 409600, 'b': 409600}))


for test in tests:
    test_outcome = simple_assembler(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))