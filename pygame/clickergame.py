import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cookie-Clicker-REAL|CRACKED.exe")

# Set up font
font = pygame.font.SysFont(None, 55)

# Game variables
score = 0

# Load the button image
button_image = pygame.image.load("button.png")
button_image = pygame.transform.scale(button_image, (100, 100))  # Resize image

pygame.display.set_icon(button_image)

# Function to display score
def display_score():
    title_text = font.render("COOKIE CLICKER", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))
    score_text = font.render(f"Cookies: {score}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 50))
    bottom_text = font.render(sillymsg, True, BLACK)
    screen.blit(bottom_text, (SCREEN_WIDTH // 2 - bottom_text.get_width() // 2, 230))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the button image
    screen.blit(button_image, (150, 100))

    if score == 69:
        sillymsg = "Nice"
    elif score == 420:
        sillymsg = "based"
    elif score == 10:
        sillymsg = "The Big One Zero"
    elif score == 0:
        sillymsg = "start clickin bud"
    elif score == 69420:
        sillymsg = "Very Nice"
    else:
        sillymsg = " "

    # Display the score
    display_score()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Cookie Clicked")
            if 150 <= mouse_pos[0] <= 250 and 100 <= mouse_pos[1] <= 200:  # Check if click is inside image area
                score += 1  # Increment score on image click

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()