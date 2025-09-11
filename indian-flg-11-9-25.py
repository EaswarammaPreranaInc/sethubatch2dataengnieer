import pygame
import math
import asyncio
import platform
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load and play anthem
pygame.mixer.music.load("jan.mp3")  # <-- Place your anthem file here
pygame.mixer.music.play(-1)  # Loop indefinitely

# Screen dimensions
WIDTH = 900
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Indian Flag Hoisting with Celebration")

# Colors
SAFFRON = (255, 153, 51)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
NAVY_BLUE = (0, 0, 128)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)

# Flag properties
FLAG_WIDTH = 300
FLAG_HEIGHT = 200
FLAG_X = 100
FLAG_Y = HEIGHT
POLE_HEIGHT = HEIGHT
POLE_WIDTH = 10
POLE_X = FLAG_X - 10
POLE_Y = 0

# Animation properties
hoist_speed = 6
wave_amplitude = 10
wave_frequency = 0.05
animation_state = "hoisting"  # States: hoisting, waving, celebrating
frame_count = 0

# Ashoka Chakra
CHAKRA_RADIUS = 30

# Font
font = pygame.font.SysFont("arial", 20)

# Ashoka Chakra 24 spokes meaning
chakra_text = [
    "The 24 spokes of the Ashoka Chakra represent:",
    "1. Love", "2. Courage", "3. Patience", "4. Peacefulness",
    "5. Magnanimity", "6. Goodness", "7. Faithfulness", "8. Gentleness",
    "9. Selflessness", "10. Self-Control", "11. Self Sacrifice", "12. Truthfulness",
    "13. Righteousness", "14. Justice", "15. Mercy", "16. Gracefulness",
    "17. Humility", "18. Empathy", "19. Sympathy", "20. Spiritual Knowledge",
    "21. Moral Values", "22. Spiritual Wisdom", "23. The Fear of God", "24. Faith or Belief"
]

# Crowd cheering
CROWD_SIZE = 40
crowd = [{"x": random.randint(50, WIDTH - 50),
          "y": HEIGHT - 50,
          "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
          "jump_height": random.randint(10, 40),
          "phase": random.random() * math.pi * 2} for _ in range(CROWD_SIZE)]

# Fireworks
fireworks = []

def create_firework():
    """Create a new firework with exploding particles"""
    x = random.randint(200, WIDTH - 200)
    y = random.randint(100, 300)
    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    particles = []
    for i in range(50):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        particles.append({
            "x": x, "y": y,
            "vx": speed * math.cos(angle),
            "vy": speed * math.sin(angle),
            "life": random.randint(30, 60),
            "color": color
        })
    fireworks.append(particles)

def update_fireworks():
    """Update and draw fireworks"""
    for particles in fireworks[:]:
        for p in particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.05  # gravity
            p["life"] -= 1
            if p["life"] > 0:
                pygame.draw.circle(screen, p["color"], (int(p["x"]), int(p["y"])), 3)
        particles[:] = [p for p in particles if p["life"] > 0]
        if not particles:
            fireworks.remove(particles)

def draw_flag(x, y):
    for i in range(FLAG_WIDTH):
        wave = wave_amplitude * math.sin(wave_frequency * i + frame_count * 0.1) if animation_state != "hoisting" else 0
        pygame.draw.rect(screen, SAFFRON, (x + i, y + wave, 1, FLAG_HEIGHT // 3))
        pygame.draw.rect(screen, WHITE, (x + i, y + FLAG_HEIGHT // 3 + wave, 1, FLAG_HEIGHT // 3))
        pygame.draw.rect(screen, GREEN, (x + i, y + 2 * FLAG_HEIGHT // 3 + wave, 1, FLAG_HEIGHT // 3))
    
    if animation_state != "hoisting" or FLAG_Y < HEIGHT - FLAG_HEIGHT:
        center_x = x + FLAG_WIDTH // 2
        center_y = y + FLAG_HEIGHT // 2
        pygame.draw.circle(screen, NAVY_BLUE, (center_x, center_y), CHAKRA_RADIUS, 2)
        for i in range(24):
            rad = math.radians(i * 15)
            end_x = center_x + CHAKRA_RADIUS * math.cos(rad)
            end_y = center_y + CHAKRA_RADIUS * math.sin(rad)
            pygame.draw.line(screen, NAVY_BLUE, (center_x, center_y), (end_x, end_y), 2)

def draw_text():
    for i, line in enumerate(chakra_text):
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (FLAG_X + FLAG_WIDTH + 50, 50 + i * 25))

def draw_crowd():
    if animation_state != "hoisting":
        for person in crowd:
            jump = math.sin(frame_count * 0.1 + person["phase"]) * person["jump_height"]
            pygame.draw.circle(screen, person["color"], (person["x"], int(person["y"] - jump)), 8)

def update_loop():
    global FLAG_Y, animation_state, frame_count
    screen.fill(SKY_BLUE)
    
    pygame.draw.rect(screen, BLACK, (POLE_X, POLE_Y, POLE_WIDTH, POLE_HEIGHT))
    
    if animation_state == "hoisting":
        FLAG_Y -= hoist_speed
        if FLAG_Y <= 50:
            FLAG_Y = 50
            pygame.time.wait(1000)
            animation_state = "waving"
    
    if animation_state == "waving" and frame_count % 50 == 0:
        create_firework()
    
    draw_flag(FLAG_X, FLAG_Y)
    draw_text()
    draw_crowd()
    update_fireworks()
    
    pygame.display.flip()
    frame_count += 1

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        update_loop()
        await asyncio.sleep(1.0 / 60)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
