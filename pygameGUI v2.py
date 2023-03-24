import random, pygame, sys, time
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (65, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)

def main():
    global DISPLAYSURF, FONT, numofquestion, numofcorrect
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Game')
    FONT = pygame.font.Font('freesansbold.ttf', 32)

    gameTitle()
    ans, problem = mathlogicplus()
    text = ''

    #Display Timer
    counter, trackTime = 60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()

    'trying to track the number and question and correct answers'
    numofquestion = 0
    numofcorrect = 0

    onTimer = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYUP:
                DISPLAYSURF.fill(BLACK)
                saveQuestion(problem, text)
                pygame.display.update()
                onTimer = True

            elif event.type == KEYDOWN:
                if event.key == K_1:
                    text += '1'
                elif event.key == K_2:
                    text += '2'
                elif event.key == K_3:
                    text += '3'
                elif event.key == K_4:
                    text += '4'
                elif event.key == K_5:
                    text += '5'
                elif event.key == K_6:
                    text += '6'
                elif event.key == K_7:
                    text += '7'
                elif event.key == K_8:
                    text += '8'
                elif event.key == K_9:
                    text += '9'
                elif event.key == K_0:
                    text += '0'
                elif event.key == K_BACKSPACE:
                    text = text[:-1]

            if onTimer == True:
                DISPLAYSURF.fill((BLACK))
                DISPLAYSURF.blit(FONT.render(trackTime, True, GREEN), (340, 10))
                pygame.display.update([339,6,57,36]) #[x,y, w,h]
                clock.tick(60)
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    if counter > 0:
                        trackTime = str(counter).rjust(3)
                    else:
                        onTimer = False
                        timeText()


        if text != '':
            if str(ans) == str(text):
                DISPLAYSURF.fill(BLACK)
                correct()
                saveQuestion(problem, text)
                pygame.display.update()
                pygame.time.wait(1000)
                text = ''
                ans,problem = mathlogicplus()
                saveQuestion(problem, text)
                pygame.display.update()

            elif str(ans) != str(text) and len(str(ans)) == len(text):
                DISPLAYSURF.fill(BLACK)
                saveQuestion(problem, text)
                incorrect()
                pygame.display.update()
                pygame.time.wait(1000)
                text = ''
                pygame.display.update()

            elif len(str(ans)) < len(text):
                DISPLAYSURF.fill(BLACK)
                saveQuestion(problem, text)
                incorrect()
                pygame.display.update()
                pygame.time.wait(1000)
                text = ''
                pygame.display.update()


def mathlogicplus():
    firstdigit = random.randint(1, 10)
    seconddigit = random.randint(1, 10)
    oper = random.choice('+-*/')

    if oper == '+':
        cor = firstdigit + seconddigit
        problemtext = str(firstdigit)+' + '+str(seconddigit)+' = '
        return cor, problemtext

    elif oper == '-':
        if firstdigit < seconddigit:
            cor = seconddigit - firstdigit
            problemtext = str(seconddigit) + ' - ' + str(firstdigit) + ' = '
            return cor, problemtext
        else:
            cor = firstdigit - seconddigit
            problemtext = str(firstdigit)+' - '+str(seconddigit)+' = '
            return cor, problemtext

    elif oper == '*':
        cor = firstdigit * seconddigit
        problemtext = str(firstdigit)+' * '+str(seconddigit)+' = '
        return cor, problemtext

    elif oper == '/':
        dividend = firstdigit * seconddigit
        cor = int(dividend / seconddigit)
        print(cor)
        problemtext = str(dividend) + ' / ' + str(seconddigit)+' = '
        return cor, problemtext


def incorrect():
    #DISPLAYSURF.fill(BLACK)
    incorrectText = 'Incorrect'
    incorrectSurf = FONT.render(incorrectText, True, RED)
    incorrectRect = incorrectSurf.get_rect()
    incorrectRect.center = (200, 100)
    DISPLAYSURF.blit(incorrectSurf, incorrectRect)


def correct():
    # DISPLAYSURF.fill(BLACK)
    correctText = 'Correct'
    correctSurf = FONT.render(correctText, True, GREEN)
    correctRect = correctSurf.get_rect()
    correctRect.center = (200, 100)
    DISPLAYSURF.blit(correctSurf, correctRect)


def helpme():
    # DISPLAYSURF.fill(BLACK)
    helpmeText = 'Some thing when wrong!'
    helpmeSurf = FONT.render(helpmeText, True, GREEN)
    helpmeRect = helpmeSurf.get_rect()
    helpmeRect.center = (200, 100)
    DISPLAYSURF.blit(helpmeSurf, helpmeRect)


def gameTitle():
    titleText = 'MATH GAME'
    titleSurf = FONT.render(titleText, True, GREEN)
    titleRect = titleSurf.get_rect()
    titleRect.center = (200,150)
    DISPLAYSURF.blit(titleSurf, titleRect)
    if checkForInput():
        pygame.event.get()
        return
    pygame.display.update()

def timeText():
    DISPLAYSURF.fill(BLACK)
    timesUpText = 'TIMES UP'
    timesUpSurf = FONT.render(timesUpText, True, GREEN)
    timesUpRect = timesUpSurf.get_rect()
    timesUpRect.center = (200, 150)
    DISPLAYSURF.blit(timesUpSurf, timesUpRect)
    pygame.display.update()


def checkForInput():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def terminate():
    pygame.quit()
    sys.exit()


def saveQuestion(x,text):
    savequestion = str(x) + str(text)
    saveSurf = FONT.render(savequestion, True, GREEN)
    saveRect = saveSurf.get_rect()
    saveRect.center = (200, 150)
    DISPLAYSURF.blit(saveSurf, saveRect)


if __name__ == '__main__':
    main()


'todo: add: timer, correct/incorrect list, show final result?'
'fix code to work with dynamic windows size'