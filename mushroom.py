import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500
cell_size = 50

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Mushroom Destroyer Game")

# Colors
background_color = (00, 80, 00)
line_color = (00, 80, 00)
mushroom_color = (255, 0, 0)
highlight_color = (0, 255, 0)

# Game variables
grid_size = 10
array = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
mushroom_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
array[mushroom_position[0]][mushroom_position[1]] = 1

# Timer variables
timer = 30  # Start with 30 seconds
font = pygame.font.Font(None, 36)  # Font for rendering the timer
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
                pygame.draw.circle(screen, mushroom_color, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2), cell_size // 2 - 5)

def draw_timer():
    timer_text = font.render(f"Time: {timer}", True, (0, 0, 0))
    screen.blit(timer_text, (10, 10))

def reset_array():
    for i in range(grid_size):
        for j in range(grid_size):
            array[i][j] = 0

def spawn_mushroom():
    global mushroom_position
    mushroom_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    array[mushroom_position[0]][mushroom_position[1]] = 1

def destroy_mushroom(x, y):
    global timer
    if array[x][y] == 1:
        array[x][y] = 0
        spawn_mushroom()
        timer += 1  # Increase timer by 5 seconds

# Main game loop
run = True
while run:
    screen.fill(background_color)
    draw_grid()
    draw_mushrooms()
    draw_timer()
    
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

pygame.quit()