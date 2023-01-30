import random, time

def simplemath():
    """use a timer to have the loop continuously give math problem.
    and track how many correct"""
    count = 0
    numberofsec = 10
    time_e = time.time() + numberofsec
    print(str(numberofsec) + ' sec on the clock')
    while time.time() < time_e:
        firstdig = random.randint(1, 9)
        seconddig = random.randint(1, 9)
        cor = firstdig + seconddig
        #print(cor)
        ans = input(str(firstdig) + ' + ' + str(seconddig) + ' = ')
        if int(ans) == cor:
            print('Correct')
            count += 1
        elif int(ans) != cor:
            print('Incorrect')
        else:
            print('something when wrong')
    print('number of correct: ' +str(count))


print(simplemath())



'''how to break the above to into parts'''