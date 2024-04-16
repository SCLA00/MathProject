import random
import operator


def main():
    logged_Question = []
    Toggle_Loop = True
    while Toggle_Loop:
        global ops
        # ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        ops = {'-': operator.sub}
        randomOp = random.choice(list(ops.keys()))
        firstvalue = random.randint(1,12)
        secondvalue = random.randint(1,12)

        if randomOp == '+':
            check(firstvalue, secondvalue, randomOp)
        elif randomOp == '-':
            if firstvalue > secondvalue:
                check(firstvalue, secondvalue, randomOp)
        elif randomOp == '*':
            if len(str(firstvalue)) == 1 or len(str(secondvalue)) == 1:
                check(firstvalue, secondvalue, randomOp)
        elif randomOp == '/':
            if firstvalue > secondvalue and firstvalue % secondvalue == 0 and firstvalue != 0:
                check(firstvalue, secondvalue, randomOp)


def check(first, second, oper):
    '''
    Create a log variable to track the question asked ?
    does the log need to be global?
    ADD list of all the question asked and note if user enter the correct or wrong answer.
    '''
    #input is the enter number that need to be compared to output
    Second_Loop = True
    while Second_Loop:
        answer = ops[oper](first, second)
        inputAnswer = input(f'{first} {oper} {second} = ')
        if answer == int(inputAnswer):
            Second_Loop = False
            print('Correct')
        elif answer != int(inputAnswer):
            print('Incorrect')
        else:
            print('Send Help')


if __name__ == '__main__':
    print(main())