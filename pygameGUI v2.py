import random, pygame, sys, time
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (65, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)

def main():
    global DISPLAYSURF, FONT, FONTSIZE,text
    pygame.init()
    DISPLAYSURF = fullScreen()
    #DISPLAYSURF = pygame.display.set_mode((400,300), RESIZABLE)


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

            elif event.type == KEYUP or event.type == VIDEORESIZE:
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

                elif event.key == K_n:
                    pygame.quit()
                elif event.key == K_y:
                    main()

                elif event.key == K_ESCAPE:
                    pygame.quit()

            if onTimer == True:
                width, height = pygame.display.get_surface().get_size()
                DISPLAYSURF.fill(BLACK)
                FONTSIZE = fontAdj()
                FONT = pygame.font.Font('Gugi-Regular.ttf', FONTSIZE)
                secSurf = FONT.render(trackTime, True, GREEN)
                secRect = secSurf.get_rect()
                secRect.topright = (width, 0)
                DISPLAYSURF.blit(secSurf, secRect)
                pygame.display.update(secRect)  # [x,y, w,h] [340,6,57,36]
                #clock.tick(100)
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    if counter > 0:
                        trackTime = str(counter).rjust(3)
                    else:
                        onTimer = False
                        timeText()
                        time.sleep(1)
                        playAgain()

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
    firstdigit = random.randint(1, 12)
    seconddigit = random.randint(1, 12)
    oper = random.choice('+-*/')

    if oper == '+':
        cor = firstdigit + seconddigit
        problemtext = str(firstdigit)+' + '+str(seconddigit)+' = '
        return cor, problemtext

    elif oper == '-':
        'trying to avoid negative solution'
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
        problemtext = str(dividend) + ' / ' + str(seconddigit)+' = '
        return cor, problemtext


def incorrect():
    width, height = pygame.display.get_surface().get_size()
    incorrectText = 'Incorrect'
    incorrectSurf = FONT.render(incorrectText, True, RED)
    incorrectRect = incorrectSurf.get_rect()
    incorrectRect.center = (width/2, height/2-50)
    DISPLAYSURF.blit(incorrectSurf, incorrectRect)


def correct():
    width, height = pygame.display.get_surface().get_size()
    correctText = 'Correct'
    correctSurf = FONT.render(correctText, True, GREEN)
    correctRect = correctSurf.get_rect()
    correctRect.center = (width/2, height/2-50)
    DISPLAYSURF.blit(correctSurf, correctRect)


def gameTitle():
    width, height = pygame.display.get_surface().get_size()
    titleText = 'MATH GAME'
    FONTSIZE = fontAdj()
    FONT = pygame.font.Font('Gugi-Regular.ttf', FONTSIZE)
    titleSurf = FONT.render(titleText, True, GREEN)
    titleRect = titleSurf.get_rect()
    titleRect.center = (width/2, height/2)
    DISPLAYSURF.blit(titleSurf, titleRect)
    if checkForInput():
        pygame.event.get()
        return
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


def timeText():
    width, height = pygame.display.get_surface().get_size()
    DISPLAYSURF.fill(BLACK)
    timesUpText = 'TIMES UP'
    timesUpSurf = FONT.render(timesUpText, True, GREEN)
    timesUpRect = timesUpSurf.get_rect()
    timesUpRect.center = (width/2, height/2)
    DISPLAYSURF.blit(timesUpSurf, timesUpRect)
    pygame.display.update()


def terminate():
    pygame.quit()
    sys.exit()


def saveQuestion(x,text):
    width, height = pygame.display.get_surface().get_size()
    savequestion = str(x) + str(text)
    FONTSIZE = fontAdj()
    FONT = pygame.font.Font('Gugi-Regular.ttf', FONTSIZE)
    saveSurf = FONT.render(savequestion, True, GREEN)
    saveRect = saveSurf.get_rect()
    saveRect.center = (width/2, height/2)
    DISPLAYSURF.blit(saveSurf, saveRect)


def fontAdj():
    width, height = pygame.display.get_surface().get_size()
    FONTSIZE = int(height*32/300)
    return FONTSIZE


def playAgain():
    width, height = pygame.display.get_surface().get_size()
    DISPLAYSURF.fill(BLACK)
    playText = 'Play again? [Y/N]'
    playSurf = FONT.render(playText, True, GREEN)
    playRect = playSurf.get_rect()
    playRect.center = (width/2, height/2)
    DISPLAYSURF.blit(playSurf, playRect)
    pygame.display.update()

def fullScreen():
    d = pygame.display.Info()
    w = d.current_w
    h = d.current_h
    DISPLAYSURF = pygame.display.set_mode((w, h), RESIZABLE)
    return DISPLAYSURF

if __name__ == '__main__':
    main()


'todo: correct/incorrect list, show final result?'
