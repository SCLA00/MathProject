import random
import operator
import time



def main():
    global ops, correctLog, IncorrectLog
    Toggle_Loop = True
    correctLog = []
    IncorrectLog = []
    numberofsec = 60
    time_end = time.time() + numberofsec
    while time.time() < time_end:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
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

    print(f'The number of correct: {len(correctLog)}')
    print(*correctLog,sep='\n')
    print(f'The number of correct: {len(IncorrectLog)}')
    print(*IncorrectLog,sep='\n')


def check(first, second, oper):
    Second_Loop = True
    question = ''
    while Second_Loop:
        answer = ops[oper](first, second)
        inputAnswer = input(f'{first} {oper} {second} = ')
        question = str(f'{first} {oper} {second} = {inputAnswer}')
        if answer == int(inputAnswer):
            Second_Loop = False
            correctLog.append(question)
            print('Correct')
        elif answer != int(inputAnswer):
            if question not in IncorrectLog:
                IncorrectLog.append(question)
            print('Incorrect')
        else:
            print('Send Help')

if __name__ == '__main__':
    print(main())