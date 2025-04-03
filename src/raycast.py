# raycast.py
from OpenGL.GL import *
from OpenGL.GLU import *

def get_ray(mx, my, display):
    x = 2.0 * mx / display[0] - 1.0
    y = 1.0 - 2.0 * my / display[1]

    proj = glGetDoublev(GL_PROJECTION_MATRIX)
    model = glGetDoublev(GL_MODELVIEW_MATRIX)
    view = glGetIntegerv(GL_VIEWPORT)

    start = gluUnProject(mx, display[1] - my, 0, model, proj, view)
    end = gluUnProject(mx, display[1] - my, 1, model, proj, view)
    direction = [end[i] - start[i] for i in range(3)]

    return start, direction

def ray_box_intersect(origin, direction, box_min, box_max):
    tmin = (box_min[0] - origin[0]) / direction[0] if direction[0] != 0 else -float('inf')
    tmax = (box_max[0] - origin[0]) / direction[0] if direction[0] != 0 else float('inf')
    if tmin > tmax: tmin, tmax = tmax, tmin
    for i in range(1, 3):
        t1 = (box_min[i] - origin[i]) / direction[i] if direction[i] != 0 else -float('inf')
        t2 = (box_max[i] - origin[i]) / direction[i] if direction[i] != 0 else float('inf')
        if t1 > t2: t1, t2 = t2, t1
        if t1 > tmin: tmin = t1
        if t2 < tmax: tmax = t2
    return tmax >= max(tmin, 0)
