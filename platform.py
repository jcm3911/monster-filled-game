import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
screen_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(screen_size)

# Set the title
pygame.display.set_caption("2D Platformer")

# Set the background color
bg_color = (0, 0, 0)

# Load the player image
player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))
player_rect = player_image.get_rect()

# Load the platform image
platform_image = pygame.image.load("platform.png").convert_alpha()
platform_image = pygame.transform.scale(platform_image, (100, 20))
platform_rect = platform_image.get_rect()

# Load the coin image
coin_image = pygame.image.load("coin.png").convert_alpha()
coin_image = pygame.transform.scale(coin_image, (25, 25))
coin_rect = coin_image.get_rect()

# Load the enemy image
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
enemy_rect = enemy_image.get_rect()

# Set the player's starting position
player_rect.x = 100
player_rect.y = 100

# Set the player's horizontal velocity
player_velocity_x = 0

# Set the player's vertical velocity
player_velocity_y = 0

# Set the player's acceleration due to gravity
gravity = 0.5

# Set the player's jump velocity
jump_velocity = -10

# Set the player's speed
speed = 5

# Set the enemy's speed
enemy_speed = 2

# Set the number of coins the player has collected
coins_collected = 0

# Set the number of levels
num_levels = 2

# Set the current level
current_level = 1

# Set the level data for each level
levels = []
for level in range(num_levels):
    # Generate a random number of platforms
    num_platforms = random.randint(1, 5)
    platforms = []
    for i in range(num_platforms):
        # Generate a random platform position
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        platforms.append((x, y))

    # Generate a random number of coins
    num_coins = random.randint(1, 5)
    coins = []
    for i in range(num_coins):
        # Generate a random coin position
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        coins.append((x, y))

    # Generate a random
