import random, pygame, sys, time
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (65, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)


def main():
    global DISPLAYSURF, FONT, FONTSIZE
    pygame.init()
    #DISPLAYSURF = fullScreen()
    DISPLAYSURF = pygame.display.set_mode((400, 300), RESIZABLE)

    FONTSIZE = fontAdj()
    FONT = pygame.font.Font('DS-DIGI.TTF', FONTSIZE)

    gameTitle()
    ans, problem = mathlogicplus()
    user_answer = ''

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
                FONTSIZE = fontAdj()
                FONT = pygame.font.Font('DS-DIGI.TTF', FONTSIZE)
                saveQuestion(problem, user_answer)
                onTimer = True

            elif event.type == KEYDOWN:
                if event.unicode.isnumeric():
                    user_answer += event.unicode
                elif event.key == K_BACKSPACE:
                    user_answer = user_answer[:-1]

                elif event.key == K_n:
                    terminate()
                elif event.key == K_y:
                    main()

                elif event.key == K_ESCAPE:
                    terminate()

            if onTimer == True:
                width, height = pygame.display.get_surface().get_size()
                DISPLAYSURF.fill(BLACK)
                secSurf = FONT.render(trackTime, True, GREEN)
                secRect = secSurf.get_rect()
                secRect.topright = (width, 0)
                DISPLAYSURF.blit(secSurf, secRect)
                pygame.display.update(secRect)  # [x,y, w,h] [340,6,57,36]
                clock.tick(100)
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    if counter > 0:
                        trackTime = str(counter).rjust(3)
                    else:
                        onTimer = False
                        displayMessage('Times Up', GREEN, 0)
                        pygame.time.wait(1500)
                        playAgain()

        if user_answer != '':
            'check if user_input is correct and show the corresponding user_answer'

            if str(ans) == str(user_answer):
                DISPLAYSURF.fill(BLACK)
                displayMessage('Correct', GREEN, FONTSIZE)
                saveQuestion(problem, user_answer)
                pygame.time.wait(1000)
                user_answer = ''
                ans, problem = mathlogicplus()
                saveQuestion(problem, user_answer)

            elif str(ans) != str(user_answer) and len(str(ans)) == len(user_answer):
                DISPLAYSURF.fill(BLACK)
                saveQuestion(problem, user_answer)
                displayMessage('Incorrect', RED, FONTSIZE)
                pygame.time.wait(1000)
                user_answer = ''

            elif len(str(ans)) < len(user_answer):
                DISPLAYSURF.fill(BLACK)
                saveQuestion(problem, user_answer)
                displayMessage('Incorrect', RED, 0)
                pygame.time.wait(1000)
                user_answer = ''


def mathlogicplus():
    oper = random.choice('+-*/')
    if oper == '+' or oper == '-':
        firstdigit = random.randint(1, 99)
        seconddigit = random.randint(1, 99)
        if oper == '+':
            ans = firstdigit + seconddigit
            problemtext = f'{firstdigit} + {seconddigit} = '
            return ans, problemtext
        elif oper == '-':
            if int(firstdigit) < int(seconddigit):
                ans = seconddigit - firstdigit
                problemtext = f'{seconddigit} - {firstdigit} = '
                return ans, problemtext
            else:
                ans = int(firstdigit) - int(seconddigit)
                problemtext = f'{firstdigit} - {seconddigit} = '
                return ans, problemtext
    elif oper == '*' or oper == '/':
        firstdigit = random.randint(1, 12)
        seconddigit = random.randint(1, 12)
        if oper == '*':
            ans = firstdigit * seconddigit
            problemtext = f'{firstdigit} * {seconddigit} = '
            return ans, problemtext
        elif oper == '/':
            dividend = firstdigit * seconddigit
            ans = int(dividend / seconddigit)
            problemtext = f'{dividend} / {seconddigit} = '
            return ans, problemtext

def displayMessage(textItem, colorItem, fontItem):
    'correct, incorrect, timesup'
    width, height = pygame.display.get_surface().get_size()
    DISPLAYSURF.fill(BLACK)
    displayText = textItem
    displayTextSurf = FONT.render(displayText, True, colorItem)
    displayTextRect = displayTextSurf.get_rect()
    displayTextRect.center = (width / 2, height / 2 - fontItem)
    DISPLAYSURF.blit(displayTextSurf, displayTextRect)
    pygame.display.update(displayTextRect)


def playAgain():
    width, height = pygame.display.get_surface().get_size()
    DISPLAYSURF.fill(BLACK)
    playText = 'Play again? [Y/N]'
    FONT = pygame.font.SysFont('georgia', 30)
    playSurf = FONT.render(playText, True, GREEN)
    playRect = playSurf.get_rect()
    playRect.center = (width / 2, height / 2)
    DISPLAYSURF.blit(playSurf, playRect)
    pygame.display.update()


def gameTitle():
    width, height = pygame.display.get_surface().get_size()
    titleText = 'MATH GAME'
    titleSurf = FONT.render(titleText, True, GREEN)
    titleRect = titleSurf.get_rect()
    titleRect.center = (width / 2, height / 2)
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


def terminate():
    pygame.quit()
    sys.exit()


def saveQuestion(problem, user_answer):
    width, height = pygame.display.get_surface().get_size()
    savequestion = str(problem) + str(user_answer)
    saveSurf = FONT.render(savequestion, True, GREEN)
    saveRect = saveSurf.get_rect()
    saveRect.center = (width / 2, height / 2)
    DISPLAYSURF.blit(saveSurf, saveRect)
    pygame.display.update()


def fontAdj():
    width, height = pygame.display.get_surface().get_size()
    FONTSIZE = int(height * 22 / 300)
    return FONTSIZE


if __name__ == '__main__':
    main()

'todo: correct/incorrect list, show final result?'
