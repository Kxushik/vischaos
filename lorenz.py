import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Lorenz attractor parameters
sigma = 8
beta = 8/3
rho = 25

# Initial conditions
x0 = 0.1
y0 = 0
z0 = 0

# Lorenz attractor function
def lorenz(x, y, z, sigma=sigma, beta=beta, rho=rho):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Initialize Pygame and OpenGL
pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF|pygame.OPENGL)
pygame.display.set_caption("Lorenz Attractor")
clock = pygame.time.Clock()
glViewport(0, 0, 640, 480)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, 640/480, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(0, 0, 125, 0, 0, 0, 0, 1, 0)

# Initialize variables
dt = 0.01
x, y, z = x0, y0, z0
points = []
color = [1, 1, 1]

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update Lorenz attractor
    dx_dt, dy_dt, dz_dt = lorenz(x, y, z)
    x += dx_dt * dt
    y += dy_dt * dt
    z += dz_dt * dt
    points.append([x, y, z])

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Draw Lorenz attractor
    glBegin(GL_LINE_STRIP)
    for i in range(len(points)):
        glColor3fv(color)
        glVertex3fv(points[i])
    glEnd()

    # Update display
    pygame.display.flip()
    clock.tick(60)
