import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

def draw_line():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glVertex3f(-1.0, 0.0, 0.0)  # Start point
    glVertex3f(1.0, 1.0, 1.0)   # End point
    glEnd()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_line()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()

