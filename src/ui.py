# ui.py
import pygame


# Розміри та позиції кнопок
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 50
MARGIN = 30


# Прямокутники кнопок
button_throw = pygame.Rect(MARGIN, 700, BUTTON_WIDTH, BUTTON_HEIGHT)
button_end = pygame.Rect(1000 - BUTTON_WIDTH - MARGIN, 700, BUTTON_WIDTH, BUTTON_HEIGHT)

def draw_buttons(surface, font):
    pygame.draw.rect(surface, (0, 200, 0), button_throw)
    pygame.draw.rect(surface, (200, 0, 0), button_end)

    text_throw = font.render("Кинути ще", True, (255, 255, 255))
    text_end = font.render("Завершити хід", True, (255, 255, 255))

    surface.blit(text_throw, (button_throw.x + 20, button_throw.y + 10))
    surface.blit(text_end, (button_end.x + 10, button_end.y + 10))

def check_button_click(pos):
    if button_throw.collidepoint(pos):
        return "throw"
    elif button_end.collidepoint(pos):
        return "end"
    return None

def draw_score(surface, font, score, x=30, y=30):
    text = font.render(f"Очки: {score}", True, (255, 255, 0))
    surface.blit(text, (x, y))
