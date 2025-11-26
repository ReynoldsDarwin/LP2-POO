from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)                    # Tamaño de puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Vista ortográfica de -5 a 5 en ambos ejes
    glOrtho(-5.0, 5.0, -5.0, 5.0, -1.0, 1.0)

def dibujar_cuadrado():
    """Dibuja un cuadrado usando GL_QUADS"""
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    # Colores en cada vértice para ver el degradado
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex2f(-2.5, -2.5)    # Inferior izquierda

    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex2f(2.5, -2.5)     # Inferior derecha

    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex2f(2.5, 2.5)      # Superior derecha

    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glVertex2f(-2.5, 2.5)     # Superior izquierda
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cuadrado en coordenadas 5.0 - OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_cuadrado)
    glutMainLoop()

if __name__ == "__main__":
    main()
