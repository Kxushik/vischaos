import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

edgesmod = (
    (0,1),
    (0,1),
    (0,1),
    (2,1),
    (2,1),
    (2,2),
    (6,2),
    (6,2),
    (6,2),
    (5,2),
    (5,3),
    (5,4)
    )
def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    clock = pygame.time.Clock()
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -10)
    max_fps = 0;
    min_fps = 100;
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        clock.tick()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)
        fps = clock.get_fps()
        if fps>max_fps:
            max_fps=fps
        elif fps<min_fps:
            min_fps=fps
        print(fps)
        print("MAX:"+str(max_fps))
        print("MIN:"+str(min_fps))
    

if __name__ == "__main__":
    main()