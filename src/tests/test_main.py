import pytest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Мокаємо всі OpenGL/pygame-функції, які не працюють у CI середовищі
@patch("OpenGL.GL.glEnable")
@patch("OpenGL.GL.glTexParameteri")
@patch("OpenGL.GL.glBindTexture")
@patch("OpenGL.GL.glTexImage2D")
@patch("OpenGL.GL.glGenTextures", return_value=1)
@patch("OpenGL.GL.glClear")
@patch("OpenGL.GL.glPushMatrix")
@patch("OpenGL.GL.glRotatef")
@patch("OpenGL.GL.glPopMatrix")
@patch("OpenGL.GL.glTranslatef")
@patch("OpenGL.GLU.gluPerspective", return_value=None)
@patch("pygame.display.set_mode")
@patch("pygame.display.set_caption")
@patch("pygame.display.flip")
@patch("pygame.event.get", return_value=[])
@patch("pygame.init")
@patch("pygame.quit")
@patch("pygame.time.Clock")
def test_example(
    mock_clock,
    mock_quit,
    mock_init,
    mock_event_get,
    mock_flip,
    mock_caption,
    mock_set_mode,
    mock_gluPerspective,
    mock_translate,
    mock_pop,
    mock_rotate,
    mock_push,
    mock_clear,
    mock_gen_textures,
    mock_tex_image,
    mock_bind_texture,
    mock_tex_param,
    mock_enable
):
    import pygame
    from pygame.locals import DOUBLEBUF, OPENGL
    from OpenGL.GL import GL_DEPTH_TEST, GL_TEXTURE_2D

    from src.texture import load_texture
    from src.graphics import draw_cube

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Кубик 🎲")

    from OpenGL.GL import glEnable, glTranslatef
    from OpenGL.GLU import gluPerspective

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    texture = load_texture("assets/Dice.png")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -6)

    draw_cube(texture)
