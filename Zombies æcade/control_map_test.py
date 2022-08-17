import sys, os
import pygame


pygame.init()
screen = pygame.display.set_mode((1260, 840))

clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 40)
bg = pygame.image.load('images/background.jpg')
BG_COLOR = pygame.Color('gray12')
GREEN = pygame.Color('red')


def create_key_list(input_map):
    #A list of surfaces of the action names + assigned keys, rects and the actions.
    key_list = []
    for y, (action, value) in enumerate(input_map.items()):
        surf = FONT.render('{}: {}'.format(action, pygame.key.name(value)), True, GREEN)
        rect = surf.get_rect(topleft=(40, y*40+20))
        key_list.append([surf, rect, action])
    return key_list


def assignment_menu(input_map):
    #Allow the user to change the key assignments in this menu.

    #The user can click on an action-key pair to select it and has to press
    #a keyboard key to assign it to the action in the `input_map` dict.

    selected_action = None
    key_list = create_key_list(input_map)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            elif event.type == pygame.KEYDOWN:
                if selected_action is not None:
                    # Assign the pygame key to the action in the input_map dict.
                    input_map[selected_action] = event.key
                    selected_action = None
                    # Need to re-render the surfaces.
                    key_list = create_key_list(input_map)
                if event.key == pygame.K_ESCAPE:  # Leave the menu.
                    # Return the updated input_map dict to the main function.
                    return input_map
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_action = None
                for surf, rect, action in key_list:
                    # See if the user clicked on one of the rects.
                    if rect.collidepoint(event.pos):
                        selected_action = action

        screen.blit(bg,(0,0))
        # Blit the action-key table. Draw a rect around the
        # selected action.
        for surf, rect, action in key_list:
            screen.blit(surf, rect)
            if selected_action == action:
                pygame.draw.rect(screen, GREEN, rect, 2)

        pygame.display.flip()
        clock.tick(30)





def main():
    player = pygame.Rect(300, 220, 40, 40)
    # This dict maps actions to the corresponding key scancodes.
    input_map = {'move right': pygame.K_d, 'move left': pygame.K_a,
                 'move up': pygame.K_w, 'move down': pygame.K_s,
                 'quit': pygame.K_q, 'menu': pygame.K_m,
                 'weapon 1': pygame.K_1}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Enter the key assignment menu.
                    input_map = assignment_menu(input_map)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[input_map['move right']]:
            player.x += 3
        elif pressed_keys[input_map['move left']]:
            player.x -= 3
        elif pressed_keys[input_map['move up']]:
            player.y -= 3
        elif pressed_keys[input_map['move down']]:
            player.y += 3
        elif pressed_keys[input_map['quit']]:
            pygame.quit()
            sys.exit()
        elif pressed_keys[input_map['menu']]:
            os.system('main_menu.py')
        elif pressed_keys[input_map['weapon 1']]:
            print("pew")
        screen.blit(bg, (0,0))
        pygame.draw.rect(screen, GREEN, player)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
