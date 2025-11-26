from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glLineWidth(10)                     
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6.0, 6.0, -6.0, 6.0, -1.0, 1.0)  

def dibujar_letra_U(x):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  
    glVertex2f(x - 1.0, 2.0)
    glVertex2f(x - 1.0, -2.0)
    glVertex2f(x - 1.0, -2.0)
    glVertex2f(x + 1.0, -2.0)
    glVertex2f(x + 1.0, -2.0)
    glVertex2f(x + 1.0, 2.0)
    glEnd()

def dibujar_letra_N(x):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)  
    glVertex2f(x - 1.0, -2.0)
    glVertex2f(x - 1.0, 2.0)
    glVertex2f(x - 1.0, 2.0)
    glVertex2f(x + 1.0, -2.0)
    glVertex2f(x + 1.0, -2.0)
    glVertex2f(x + 1.0, 2.0)
    glEnd()

def dibujar_letra_A(x):
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)  
    glVertex2f(x - 1.0, -2.0)
    glVertex2f(x, 2.0)
    glVertex2f(x, 2.0)
    glVertex2f(x + 1.0, -2.0)
    glVertex2f(x - 0.5, 0.0)
    glVertex2f(x + 0.5, 0.0)
    glEnd()

def dibujar_palabra_UNA():
    glClear(GL_COLOR_BUFFER_BIT)
    dibujar_letra_U(-4.0)  # U a la izquierda
    dibujar_letra_N(0.0)   # N en el centro
    dibujar_letra_A(4.0)   # A a la derecha

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"UNA en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_palabra_UNA)
    glutMainLoop()

if __name__ == "__main__":
    main()
