import pygame
import random
import os

# Initialize Pygame
pygame.init()
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'mushroom.png')

# Screen dimensions
screen_width = 500
screen_height = 500
cell_size = 50
mushroom_image = pygame.image.load(image_path)
##mushroom_size = 

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Mushroom Destroyer Game")

# Colors
background_color = (0, 80, 0)
line_color = (0, 80, 0)
mushroom_color = (255, 0, 0)
text_color = (255, 255, 255)

# Game variables
grid_size = 10
array = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
score = 0

# Timer variables
timer = 30  # Start with 30 seconds
font = pygame.font.Font(None, 36)  # Font for rendering the timer and other texts
timer_event = pygame.USEREVENT + 1  # Custom event for timer countdown
pygame.time.set_timer(timer_event, 1000)  # Set the timer to trigger every second

def draw_grid():
    for x in range(0, screen_width, cell_size):
        for y in range(0, screen_height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, line_color, rect, 1)

def draw_mushrooms():
    for i in range(grid_size):
        for j in range(grid_size):
            if array[i][j] == 1:
                ##pygame.draw.circle(screen, mushroom_color, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2), cell_size // 2 - 5)
                screen.blit(mushroom_image, (j * cell_size, i * cell_size))

def draw_timer():
    timer_text = font.render(f"Time: {timer}", True, text_color)
    screen.blit(timer_text, (10, 10))

def draw_score():
    score_text = font.render(f"Score: {score}", True, text_color)
    screen.blit(score_text, (screen_width - 150, 10))

def reset_array():
    for i in range(grid_size):
        for j in range(grid_size):
            array[i][j] = 0

def spawn_mushroom():
    global mushroom_position
    mushroom_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    array[mushroom_position[0]][mushroom_position[1]] = 1

def destroy_mushroom(x, y):
    global score
    if array[x][y] == 1:
        array[x][y] = 0
        spawn_mushroom()
        score += 1  # Increase score by 1

def entry_screen():
    screen.fill(background_color)
    title_text = font.render("Mushroom Destroyer Game", True, text_color)
    instruction_text = font.render("Press SPACE to Start", True, text_color)
    screen.blit(title_text, (screen_width // 4, screen_height // 3))
    screen.blit(instruction_text, (screen_width // 4, screen_height // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def exit_screen():
    screen.fill(background_color)
    final_score_text = font.render(f"Final Score: {score}", True, text_color)
    exit_text = font.render("Press ESC to Exit", True, text_color)
    screen.blit(final_score_text, (screen_width // 3, screen_height // 3))
    screen.blit(exit_text, (screen_width // 3, screen_height // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting = False

def main():
    global timer, score
    entry_screen()
    reset_array()
    spawn_mushroom()
    run = True
    while run:
        screen.fill(background_color)
        draw_grid()
        draw_mushrooms()
        draw_timer()
        draw_score()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_y // cell_size
                grid_y = mouse_x // cell_size
                destroy_mushroom(grid_x, grid_y)
            elif event.type == timer_event:
                timer -= 1
                if timer <= 0:
                    run = False  # End the game when the timer reaches zero
       
        pygame.display.flip()
   
    exit_screen()
    pygame.quit()

if __name__ == "__main__":
    main()
