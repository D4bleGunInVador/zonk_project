# graphics.py
from OpenGL.GL import *
from config import FACE_TILES, TILE_WIDTH, TILE_HEIGHT

def draw_cube(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)

    vertices = [
        [1,1,-1], [-1,1,-1], [-1,-1,-1], [1,-1,-1],
        [1,1,1], [-1,1,1], [-1,-1,1], [1,-1,1]
    ]

    faces = [(0,1,5,4),(3,2,6,7),(1,2,6,5),
             (0,3,7,4),(4,7,6,5),(0,1,2,3)]

    for i, face in enumerate(faces):
        tx, ty = FACE_TILES[i]
        u0 = tx * TILE_WIDTH
        v1 = 1 - ty * TILE_HEIGHT
        u1 = u0 + TILE_WIDTH
        v0 = v1 - TILE_HEIGHT
        tex = [(u0, v0), (u1, v0), (u1, v1), (u0, v1)]
        for j in range(4):
            glTexCoord2f(*tex[j])
            glVertex3fv(vertices[face[j]])

    glEnd()

def draw_ring(radius=1.3, segments=32):
    from math import cos, sin, pi
    glDisable(GL_TEXTURE_2D)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(segments + 1):
        angle = 2 * pi * i / segments
        x = radius * cos(angle)
        z = radius * sin(angle)
        glVertex3f(x, 0, z)
    glEnd()
    glEnable(GL_TEXTURE_2D)

def draw_table(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    size = 8
    glTexCoord2f(0, 0); glVertex3f(-size, -1.5, -size)
    glTexCoord2f(1, 0); glVertex3f(size, -1.5, -size)
    glTexCoord2f(1, 1); glVertex3f(size, -1.5, size)
    glTexCoord2f(0, 1); glVertex3f(-size, -1.5, size)
    glEnd()
