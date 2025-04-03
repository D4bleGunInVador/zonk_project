import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

# Розкладка текстури: 4х3 плитки по 16px
TILE_COLS = 4
TILE_ROWS = 3
TILE_WIDTH = 1.0 / TILE_COLS
TILE_HEIGHT = 1.0 / TILE_ROWS

# Правильне розташування граней згідно схеми
FACE_TILES = [
    (2, 0),  # top → 3
    (2, 2),  # bottom → 4
    (0, 1),  # left → 1
    (2, 1),  # front → 6
    (1, 1),  # right → 2
    (3, 1),  # back → 5
]


def load_texture(filename):
    image = Image.open(filename).convert("RGBA")
    image_data = image.tobytes("raw", "RGBA", 0, -1)
    width, height = image.size

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    return texture

def draw_cube(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)

    vertices = [
        [1, 1, -1],   # 0
        [-1, 1, -1],  # 1
        [-1, -1, -1], # 2
        [1, -1, -1],  # 3
        [1, 1, 1],    # 4
        [-1, 1, 1],   # 5
        [-1, -1, 1],  # 6
        [1, -1, 1]    # 7
    ]

    faces = [
        (0, 1, 5, 4),  # top
        (3, 2, 6, 7),  # bottom
        (1, 2, 6, 5),  # left
        (0, 3, 7, 4),  # front
        (4, 7, 6, 5),  # right
        (0, 1, 2, 3),  # back
    ]

    for i, face in enumerate(faces):
        tile_x, tile_y = FACE_TILES[i]
        u0 = tile_x * TILE_WIDTH
        v1 = 1.0 - tile_y * TILE_HEIGHT
        u1 = u0 + TILE_WIDTH
        v0 = v1 - TILE_HEIGHT

        tex_coords = [
            (u0, v0),  # top-left
            (u1, v0),  # top-right
            (u1, v1),  # bottom-right
            (u0, v1),  # bottom-left
        ]

        for j in range(4):
            glTexCoord2f(*tex_coords[j])
            glVertex3fv(vertices[face[j]])

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Кубик 🎲")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    texture = load_texture("Dice.png")  

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -6)

    clock = pygame.time.Clock()
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        angle += 1
        glRotatef(angle, 1, 1, 0)
        draw_cube(texture)
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
