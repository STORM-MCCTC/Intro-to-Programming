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
pygame.display.set_caption("Fishie-Clicker-REAL|CRACKED.exe")

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
    title_text = font.render("FISH CLICKER", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))
    score_text = font.render(f"Fish: {score}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 50))
    bottom_text = font.render(sillymsg, True, BLACK)
    screen.blit(bottom_text, (SCREEN_WIDTH // 2 - bottom_text.get_width() // 2, 230))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the button image
    screen.blit(button_image, (150, 100))
    if score <= 100:
        sillymsg = "Rank: Dad"
    elif score <= 200:
        sillymsg = "Rank: Newby Angler"
    elif score <= 300:
        sillymsg = "Rank: Good Angler"
    elif score <= 400:
        sillymsg = "Rank: Greatest Angler"
    elif score <= 500:
        sillymsg = "Rank: Perfect Angler"
    elif score <= 600:
        sillymsg = "Rank: Master Angler"
    elif score <= 700:
        sillymsg = "Rank: Newby Fisher"
    elif score <= 800:
        sillymsg = "Rank: Good Fisher"
    elif score <= 900:
        sillymsg = "Rank: Greatest Fisher"
    elif score <= 1000:
        sillymsg = "Rank: Perfect Fisher"
    elif score <= 1100:
        sillymsg = "Rank: Master Fisher"
    elif score <= 1200:
        sillymsg = "Rank: Newby trawler"
    elif score <= 1300:
        sillymsg = "Rank: Good trawler"
    elif score <= 1400:
        sillymsg = "Rank: Greatest trawler"
    elif score <= 1500:
        sillymsg = "Rank: Perfect trawler"
    elif score <= 1600:
        sillymsg = "Rank: Master trawler"
    elif score <= 1700:
        sillymsg = "Rank: Newby baiter"
    elif score <= 1800:
        sillymsg = "Rank: Good baiter"
    elif score <= 1900:
        sillymsg = "Rank: Greatest baiter"
    elif score <= 2000:
        sillymsg = "Rank: Perfect baiter"
    elif score <= 2100:
        sillymsg = "Rank: Master baiter"
    else:
        sillymsg = "Rank: Master baiter"

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
            if 150 <= mouse_pos[0] <= 250 and 100 <= mouse_pos[1] <= 200:  # Check if click is inside image area
                score += 1  # Increment score on image click

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()