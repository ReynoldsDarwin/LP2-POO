import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    """Dibuja una línea"""
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_fox():
    """Dibuja la cara del zorro solo con líneas rectas"""
    
    glColor3f(0.0, 0.0, 0.0)  # Negro para todas las líneas
    glLineWidth(2.0)
    
    # Oreja izquierda
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.35, 0.3)
    glVertex2f(-0.55, 0.7)
    glVertex2f(-0.15, 0.5)
    glEnd()
    
    # Interior oreja izquierda
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.35, 0.35)
    glVertex2f(-0.48, 0.62)
    glVertex2f(-0.22, 0.48)
    glEnd()
    
    # Oreja derecha
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.35, 0.3)
    glVertex2f(0.55, 0.7)
    glVertex2f(0.15, 0.5)
    glEnd()
    
    # Interior oreja derecha
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.35, 0.35)
    glVertex2f(0.48, 0.62)
    glVertex2f(0.22, 0.48)
    glEnd()
    
    # Contorno de la cara (forma hexagonal/octogonal)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.3, 0.35)   # Superior izquierdo
    glVertex2f(-0.4, 0.1)    # Izquierda alta
    glVertex2f(-0.4, -0.15)  # Izquierda baja
    glVertex2f(-0.25, -0.4)  # Inferior izquierdo
    glVertex2f(0.0, -0.45)   # Inferior centro
    glVertex2f(0.25, -0.4)   # Inferior derecho
    glVertex2f(0.4, -0.15)   # Derecha baja
    glVertex2f(0.4, 0.1)     # Derecha alta
    glVertex2f(0.3, 0.35)    # Superior derecho
    glVertex2f(0.0, 0.4)     # Superior centro
    glEnd()
    
    # Mejilla izquierda (forma triangular)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.28, -0.05)
    glVertex2f(-0.1, -0.18)
    glVertex2f(-0.15, 0.0)
    glEnd()
    
    # Mejilla derecha
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.28, -0.05)
    glVertex2f(0.1, -0.18)
    glVertex2f(0.15, 0.0)
    glEnd()
    
    # Hocico (forma pentagonal)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.15, -0.2)
    glVertex2f(-0.08, -0.35)
    glVertex2f(0.0, -0.38)
    glVertex2f(0.08, -0.35)
    glVertex2f(0.15, -0.2)
    glEnd()
    
    # Ojo izquierdo (forma hexagonal)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.2, 0.1)
    glVertex2f(-0.18, 0.15)
    glVertex2f(-0.12, 0.15)
    glVertex2f(-0.1, 0.1)
    glVertex2f(-0.12, 0.05)
    glVertex2f(-0.18, 0.05)
    glEnd()
    
    # Pupila izquierda (rombo)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.15, 0.12)
    glVertex2f(-0.13, 0.1)
    glVertex2f(-0.15, 0.08)
    glVertex2f(-0.17, 0.1)
    glEnd()
    
    # Ojo derecho
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.18, 0.15)
    glVertex2f(0.12, 0.15)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.12, 0.05)
    glVertex2f(0.18, 0.05)
    glEnd()
    
    # Pupila derecha
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.15, 0.12)
    glVertex2f(0.13, 0.1)
    glVertex2f(0.15, 0.08)
    glVertex2f(0.17, 0.1)
    glEnd()
    
    # Nariz (triángulo)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.0, -0.15)
    glVertex2f(-0.04, -0.2)
    glVertex2f(0.04, -0.2)
    glEnd()
    
    # Boca
    draw_line(0.0, -0.2, 0.0, -0.28)     # Línea vertical
    draw_line(0.0, -0.28, -0.08, -0.3)   # Sonrisa izquierda
    draw_line(0.0, -0.28, 0.08, -0.3)    # Sonrisa derecha
    
    # Bigotes
    glLineWidth(1.5)
    # Bigotes izquierdos
    draw_line(-0.25, -0.08, -0.45, -0.05)
    draw_line(-0.25, -0.12, -0.45, -0.12)
    draw_line(-0.25, -0.16, -0.45, -0.19)
    
    # Bigotes derechos
    draw_line(0.25, -0.08, 0.45, -0.05)
    draw_line(0.25, -0.12, 0.45, -0.12)
    draw_line(0.25, -0.16, 0.45, -0.19)

def display():
    """Función de visualización"""
    glClear(GL_COLOR_BUFFER_BIT)
    draw_fox()
    glFlush()

def init():
    """Inicialización de OpenGL"""
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Fondo blanco
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def main():
    """Función principal"""
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cara de Zorro 2D - Solo Lineas Rectas")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()