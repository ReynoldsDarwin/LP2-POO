from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)  # muestra el rango visible
    glMatrixMode(GL_MODELVIEW)

def dibujar_texto(x, y, texto):
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))  # type: ignore

def dibujar_plano_cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Ejes
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    # Eje X
    glVertex2f(-4.0, 0.0)
    glVertex2f(4.0, 0.0)
    # Eje Y
    glVertex2f(0.0, -4.0)
    glVertex2f(0.0, 4.0)
    glEnd()

    # Marcas y números en eje X
    for i in range(-4, 5):
        glBegin(GL_LINES)
        glVertex2f(i, -0.1)
        glVertex2f(i, 0.1)
        glEnd()
        if i != 0:
            dibujar_texto(i - 0.1, -0.4, str(i))

    # Marcas y números en eje Y
    for j in range(-4, 5):
        glBegin(GL_LINES)
        glVertex2f(-0.1, j)
        glVertex2f(0.1, j)
        glEnd()
        if j != 0:
            dibujar_texto(0.2, j - 0.1, str(j))

    # Dibujar una parábola para referencia
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-2, 2, 200):
        y = x ** 2
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Plano cartesiano - Ejes de -4 a 4")
    inicializar()
    glutDisplayFunc(dibujar_plano_cartesiano)
    glutMainLoop()

if __name__ == "__main__":
    main()
