from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glRasterPos2f(-0.2, 0)  # Posición del texto
    for ch in "Hola Mundo":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch)) # type: ignore
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow(b"PyOpenGL - Hola Mundo y Puno")
glClearColor(0, 0, 0, 1)
glutDisplayFunc(display)
glutMainLoop()
