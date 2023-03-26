import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Define constants
WIDTH = 800
HEIGHT = 600
DT = 0.01
SIGMA = 10.0
RHO = 28.0
BETA = 8.0 / 3.0

# Define initial conditions
x = 0.1
y = 0.0
z = 0.0

# Initialize Pygame and OpenGL
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
gluPerspective(45, (WIDTH/HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10.0)
glEnable(GL_DEPTH_TEST)

# Enable double-buffering
pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

# Define clock for controlling the frame rate
clock = pygame.time.Clock()
def update_lorenz(x, y, z):
    dx = SIGMA * (y - x)
    dy = x * (RHO - z) - y
    dz = x * y - BETA * z
    x += dx * DT
    y += dy * DT
    z += dz * DT
    return x, y, z

# Render Lorenz attractor
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    
    for i in range(10000):
        x, y, z = update_lorenz(x, y, z)
        glVertex3f(x, y, z)
    
    glEnd()
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(60)
