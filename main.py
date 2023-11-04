import pygame
import random

pygame.init()
pygame.font.init()

WIN_WIDTH, WIN_HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RECT_WIDTH, RECT_HEIGHT = (20, 150)

LEFT_RECT_Y = 200
RIGHT_RECT_Y = 200

CIRCLE_X = 450
CIRCLE_Y = 290
CIRCLE_RADIUS = 20

MOVING_VELOCITY = 0.2
HORIZONTAL_BALL_VELOCITY = random.choice([0.1, -0.1])
VERTICAL_BALL_VELOCITY = random.choice([0.1, -0.1])


def restart_game():
    global LEFT_RECT_Y, RIGHT_RECT_Y, CIRCLE_X, CIRCLE_Y, HORIZONTAL_BALL_VELOCITY, VERTICAL_BALL_VELOCITY
    LEFT_RECT_Y = 200
    RIGHT_RECT_Y = 200

    CIRCLE_X = 450
    CIRCLE_Y = 290

    HORIZONTAL_BALL_VELOCITY = random.choice([0.1, -0.1])
    VERTICAL_BALL_VELOCITY = random.choice([0.1, -0.1])


def draw_left_rect():
    rect_color = WHITE
    rect_position = (0, LEFT_RECT_Y)
    rect_size = (RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(WIN, rect_color, (rect_position, rect_size))


def draw_right_rect():
    rect_color = WHITE
    rect_position = (WIN_WIDTH - RECT_WIDTH, RIGHT_RECT_Y)
    rect_size = (RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(WIN, rect_color, (rect_position, rect_size))


def draw_ball():
    global CIRCLE_X, CIRCLE_Y
    circle_color = WHITE
    circle_center = (CIRCLE_X, CIRCLE_Y)
    circle_radius = CIRCLE_RADIUS
    pygame.draw.circle(WIN, circle_color, circle_center, circle_radius)
    CIRCLE_X += HORIZONTAL_BALL_VELOCITY
    CIRCLE_Y += VERTICAL_BALL_VELOCITY


def draw_restart_button():
    button_color = (0, 128, 255)  # Blue color in RGB
    button_rect = pygame.Rect(400, 280, 100, 40)  # X, Y, Width, Height
    font = pygame.font.Font(None, 36)  # Font for button text
    text_color = (255, 255, 255)  # White color for text
    button_text = font.render("Restart", True, text_color)
    pygame.draw.rect(WIN, button_color, button_rect)
    WIN.blit(button_text, (button_rect.x + 7, button_rect.y + 7))


def check_if_ball_is_out_of_bounds():
    global HORIZONTAL_BALL_VELOCITY, VERTICAL_BALL_VELOCITY
    if CIRCLE_X + CIRCLE_RADIUS >= WIN_WIDTH:
        HORIZONTAL_BALL_VELOCITY = 0
        VERTICAL_BALL_VELOCITY = 0
        draw_restart_button()
    elif CIRCLE_X - CIRCLE_RADIUS <= 0:
        HORIZONTAL_BALL_VELOCITY = 0
        VERTICAL_BALL_VELOCITY = 0
        draw_restart_button()
    elif CIRCLE_Y - CIRCLE_RADIUS < 0 or CIRCLE_Y + CIRCLE_RADIUS > WIN_HEIGHT:
        VERTICAL_BALL_VELOCITY = -VERTICAL_BALL_VELOCITY


def check_for_collision():
    global HORIZONTAL_BALL_VELOCITY
    ball_rect = pygame.Rect(CIRCLE_X - CIRCLE_RADIUS, CIRCLE_Y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
    left_rect = pygame.Rect(0, LEFT_RECT_Y, RECT_WIDTH, RECT_HEIGHT)
    right_rect = pygame.Rect(WIN_WIDTH - RECT_WIDTH, RIGHT_RECT_Y, RECT_WIDTH, RECT_HEIGHT)
    if ball_rect.colliderect(left_rect):
        HORIZONTAL_BALL_VELOCITY = abs(HORIZONTAL_BALL_VELOCITY)
    if ball_rect.colliderect(right_rect):
        HORIZONTAL_BALL_VELOCITY = -abs(HORIZONTAL_BALL_VELOCITY)


def draw_window():
    WIN.fill(BLACK)
    draw_left_rect()
    draw_right_rect()
    check_if_ball_is_out_of_bounds()
    draw_ball()
    check_for_collision()
    pygame.display.update()


def main():
    global LEFT_RECT_Y, RIGHT_RECT_Y, CIRCLE_Y, CIRCLE_X, HORIZONTAL_BALL_VELOCITY, VERTICAL_BALL_VELOCITY
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                button_rect = pygame.Rect(400, 280, 100, 40)
                if button_rect.collidepoint(event.pos):
                    restart_game()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            LEFT_RECT_Y -= MOVING_VELOCITY
            if LEFT_RECT_Y <= 0:
                LEFT_RECT_Y = 0
        if keys[pygame.K_s]:
            LEFT_RECT_Y += MOVING_VELOCITY
            if LEFT_RECT_Y + RECT_HEIGHT >= WIN_HEIGHT:
                LEFT_RECT_Y = WIN_HEIGHT - RECT_HEIGHT
        if keys[pygame.K_i]:
            RIGHT_RECT_Y -= MOVING_VELOCITY
            if RIGHT_RECT_Y <= 0:
                RIGHT_RECT_Y = 0
        if keys[pygame.K_k]:
            RIGHT_RECT_Y += MOVING_VELOCITY
            if RIGHT_RECT_Y + RECT_HEIGHT >= WIN_HEIGHT:
                RIGHT_RECT_Y = WIN_HEIGHT - RECT_HEIGHT

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
