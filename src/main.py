# main.py
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from dice import Dice
from graphics import draw_table
from texture import load_texture
from config import CUBE_POSITIONS
from raycast import get_ray
from ui import draw_buttons, check_button_click, draw_score

def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("🎲 Зонк — Кубики на столі")

    # Ініціалізація шрифтів для кнопок і тексту
    font = pygame.font.SysFont("Arial", 24)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    dice_texture = load_texture("assets/Dice.png", repeat=False)
    table_texture = load_texture("assets/Wood_Panel.png", repeat=False)

    gluPerspective(45, display[0] / display[1], 0.1, 100.0)
    glTranslatef(0, -3, -20)
    glRotatef(60, 1, 0, 0)

    dice_list = [Dice(pos) for pos in CUBE_POSITIONS]
    clock = pygame.time.Clock()

    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                origin, direction = get_ray(mx, my, display)
                for die in dice_list:
                    if die.check_click(origin, direction):
                        die.toggle_selection()

                # Перевірка кліку по кнопках
                action = check_button_click((mx, my))
                if action == "throw":
                    # Реалізуємо "кидання" тільки не вибраних кубиків
                    pass  # Потрібно додати механіку для перекидання кубиків
                elif action == "end":
                    # Логіка завершення ходу (фіксація очок)
                    score += 100  # Додаємо випадкові очки для прикладу

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Малюємо стіл та кубики
        draw_table(table_texture)
        for die in dice_list:
            die.draw(dice_texture)

        # Тепер малюємо кнопки та очки в 2D, поверх 3D сцени
        draw_buttons(pygame.display.get_surface(), font)
        draw_score(pygame.display.get_surface(), font, score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
