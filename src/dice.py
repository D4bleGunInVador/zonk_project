# dice.py
from graphics import draw_cube, draw_ring
from raycast import ray_box_intersect
from config import DICE_ROTATIONS

class Dice:
    def __init__(self, pos):
        import random
        self.pos = pos
        self.value = random.randint(1, 6)
        self.selected = False

    def toggle_selection(self):
        self.selected = not self.selected

    def draw(self, texture_id):
        from OpenGL.GL import glPushMatrix, glTranslatef, glRotatef, glPopMatrix, glColor4f
        glPushMatrix()
        glTranslatef(*self.pos)
        rx, ry, rz = DICE_ROTATIONS[self.value]
        glRotatef(rx, 1, 0, 0)
        glRotatef(ry, 0, 1, 0)
        glRotatef(rz, 0, 0, 1)
        draw_cube(texture_id)
        glPopMatrix()

        if self.selected:
            self.draw_ring()

    def draw_ring(self):
        from OpenGL.GL import glPushMatrix, glTranslatef, glPopMatrix, glColor4f
        x, y, z = self.pos
        glPushMatrix()
        glTranslatef(x, -0.95, z)
        glColor4f(1, 0, 0, 0.3)
        draw_ring(1.3)
        glColor4f(1, 1, 1, 1)
        glPopMatrix()

    def check_click(self, ray_origin, ray_direction):
        x, y, z = self.pos
        min_b = [x - 1, y - 1, z - 1]
        max_b = [x + 1, y + 1, z + 1]
        return ray_box_intersect(ray_origin, ray_direction, min_b, max_b)
