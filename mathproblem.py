import random

def main():
    while True:
        firstdigit = random.randint(1, 144)
        seconddigit = random.randint(1, 144)

        oper = random.choice('+-*/')
        #oper = '/'

        if oper == '+':
            cor = firstdigit + seconddigit
            ans = input(str(firstdigit)+' + '+str(seconddigit)+' = ')
            check(cor,ans)

        elif oper == '-':
            if firstdigit > seconddigit:
                cor = firstdigit - seconddigit
                ans = input(str(firstdigit)+' - '+str(seconddigit)+' = ')
                check(cor,ans)

        elif oper == '*':
            if len(str(firstdigit)) == 1 and len(str(seconddigit)) == 1:
                cor = firstdigit * seconddigit
                ans = input(str(firstdigit)+' * '+str(seconddigit)+' = ')
                check(cor,ans)

        elif oper == '/':
            if firstdigit > seconddigit and firstdigit % seconddigit == 0 and firstdigit != 0:
                cor = firstdigit / seconddigit
                ans = input(str(firstdigit) + ' / ' + str(seconddigit)+' = ')
                check(cor,ans)

def check(output, input):
    #input is the enter number that need to be compare to output
    if output == int(input):
        print('correct')
    elif output != int(input):
        print('incorrect')
    else:
        print('help')



main()



