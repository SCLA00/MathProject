import pygame, sys, random, time
from pygame.locals import *

displaysurf = pygame.display.set_mode((640, 480), RESIZABLE)
pygame.display.set_caption("Maths")

WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

def main():
    global fontobj, fontsize, clock, gameMode, time_left
    pygame.init()
    fontsize = font_adj()
    fontobj = pygame.font.Font('ds_digi.ttf', fontsize)
    clock = pygame.time.Clock()

    show_text_screen('Math Game')
    waitForReturn()

    while True:
        run_Game()
        show_text_screen('Bye')


def run_Game():
    user_input = ''
    ans, text= mathlogic()
    show_text_screen(f'{text} = {user_input}')

    timer = 30
    start_timer = pygame.time.get_ticks()

    while True:
        checkForQuit()
        seconds_passed = (pygame.time.get_ticks() - start_timer) // 1000
        time_left = max(0, timer - seconds_passed)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.unicode.isnumeric():
                    user_input += str(event.unicode)
                elif event.key == K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.key == K_RETURN:
                    if str(ans) == str(user_input):
                        display_message('Correct', GREEN, 72)
                        pygame.time.wait(1000)
                        ans, text = mathlogic()
                        user_input = ''
                    elif str(ans) != str(user_input):
                        display_message('Wrong', RED, 72)
                        pygame.time.wait(1000)
                        user_input = ''
                    else:
                        display_message('BROKEN', RED, 72)

        displaysurf.fill(BLACK)
        show_time(time_left)
        show_text_screen(f'{text} = {user_input}')
        pygame.display.update()


def show_text_screen(text):
    width, height = pygame.display.get_surface().get_size()
    text_surface_obj = fontobj.render(text, True, GREEN)
    text_rect_obj = text_surface_obj.get_rect()
    x_center = int(width / 2)
    y_center = int(height / 2)
    text_rect_obj.center = (x_center,y_center)
    displaysurf.blit(text_surface_obj, text_rect_obj)
    pygame.display.update()

def show_time(time_here):
    width, height = pygame.display.get_surface().get_size()
    sec_surf = fontobj.render(str(time_here), True, GREEN)
    sec_rect = sec_surf.get_rect()
    sec_rect.topright = (width, 0)
    displaysurf.blit(sec_surf, sec_rect)
    # pygame.display.update(sec_rect)  # [x,y, w,h] [340,6,57,36]


def display_message(text_item, color_item, font_item):
    #this function is for displaying the text cor/wro above the math problem.
    width, height = pygame.display.get_surface().get_size()
    display_text = text_item
    display_text_surf = fontobj.render(display_text, True, color_item)
    display_text_rect = display_text_surf.get_rect()
    display_text_rect.center = (int(width / 2), int(height / 2) - font_item)
    displaysurf.blit(display_text_surf, display_text_rect)
    pygame.display.update(display_text_rect)

def font_adj():
    width, height = pygame.display.get_surface().get_size()
    fontsize = int(height*40/300)
    return fontsize

def mathlogic():
    operation = random.choice('+-*/')
    if operation == '+' or operation == '-':
        first_value = random.randint(1, 99)
        second_value = random.randint(1, 99)
        if operation == '+':
            ans = first_value + second_value
            problem_text = f'{first_value} + {second_value}'
            return ans,problem_text
        elif operation == '-':
            if first_value < second_value:
                ans = second_value - first_value
                problem_text = f'{second_value} - {first_value}'
                return ans, problem_text
            else:
                ans = first_value - second_value
                problem_text = f'{first_value} - {second_value}'
                return ans, problem_text
    elif operation == '*' or operation == '/':
        first_value = random.randint(1, 12)
        second_value = random.randint(1, 12)
        if operation == '*':
            ans = first_value * second_value
            problem_text = f'{first_value} * {second_value}'
            return ans,problem_text
        elif operation == '/':
            dividend = first_value * second_value
            ans = int(dividend / first_value)
            problem_text = f'{dividend} / {first_value}'
            return ans,problem_text


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def waitForReturn():
    wait = True
    while wait:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
               if event.key == K_SPACE:
                   wait = False


def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()