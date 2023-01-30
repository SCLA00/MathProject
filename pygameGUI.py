import random, pygame, sys, time
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (65, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
numberkeys = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0]


def main():

    global DISPLAYSURF, FONT, problemSurf, problemRect, saveproblem
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Game')
    FONT = pygame.font.Font('freesansbold.ttf', 32)


    gameTitle()
    ans,problem = display()
    print(ans)
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYUP:
                DISPLAYSURF.fill(BLACK)
                saveQuestion(problem, text)
                pygame.display.update()

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


                # 'move this to saveQuestion ?'
                # textSurf = FONT.render(str(text), True, GREEN)
                # textRect = textSurf.get_rect()
                # textRect.center = (270, 150)
                # DISPLAYSURF.blit(textSurf, textRect)  # display tile before the loop
                # pygame.display.update()

        #check
        if ans == text:
            print(ans,text)
            correct()
        elif ans != text:
            incorrect()



def mathlogic():
    firstvalue = random.randint(1, 9)
    secondvalue = random.randint(1, 9)
    correct = firstvalue + secondvalue
    return firstvalue, secondvalue, correct


def display():
    'display math problem'
    x, y, z = mathlogic()
    DISPLAYSURF.fill(BLACK)
    problemtext = str(x) + ' + ' + str(y) + ' = '
    problemSurf = FONT.render(problemtext, True, GREEN)
    problemRect = problemSurf.get_rect()
    problemRect.center = (200, 150)
    DISPLAYSURF.blit(problemSurf, problemRect)
    return z, problemtext


def incorrect():
    #DISPLAYSURF.fill(BLACK)
    incorrectText = 'Incorrect'
    incorrectSurf = FONT.render(incorrectText, True, GREEN)
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


main()

# alist = ['cat', 'dog', 'bird']
# txt = random.choice(alist)
# txtSurf = FONT.render(txt, True, GREEN)
# txtRect = txtSurf.get_rect()
# txtRect.center = (200, 150)
# DISPLAYSURF.blit(txtSurf, txtRect)


'''use a start ui?'''
'''the text display has to be outside the game loop because it stack in the loop'''
'''To wait for a specific key to trigger the next event. the event as to be under the KEYDOWN.'''
'''add a waitforinput condition '''