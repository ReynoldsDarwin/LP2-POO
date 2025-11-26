from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Teapot3D:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.mouse_down = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_sensitivity = 0.5 
        self.distance = -5.0
        self.min_distance = -10.0
        self.max_distance = -2.0  

        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(600, 600)
        glutCreateWindow(b"Tetera 3D - Rotacion y Zoom con Mouse")

        self.init_lighting()

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.2, 0.3, 0.4, 1.0) 

        glutDisplayFunc(self.display)
        glutSpecialFunc(self.keyboard_special)
        glutMouseFunc(self.mouse_click)
        glutMotionFunc(self.mouse_motion)
        glutMouseWheelFunc(self.mouse_wheel)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 50)
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    def init_lighting(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        
        light_position = [5.0, 5.0, 5.0, 1.0]
        light_ambient = [0.2, 0.2, 0.2, 1.0]
        light_diffuse = [0.8, 0.8, 0.8, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

        mat_ambient = [1.0, 0.5, 0.0, 1.0]
        mat_diffuse = [1.0, 0.5, 0.0, 1.0]
        mat_specular = [1.0, 1.0, 1.0, 1.0]
        mat_shininess = [50.0]

        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, self.distance) 
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0) 

        glutSolidTeapot(1.0)
        glutSwapBuffers()

    def keyboard_special(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.angle_y += 5
        elif key == GLUT_KEY_LEFT:
            self.angle_y -= 5
        elif key == GLUT_KEY_UP:
            self.angle_x -= 5
        elif key == GLUT_KEY_DOWN:
            self.angle_x += 5
        glutPostRedisplay() 

    def mouse_click(self, button, state, x, y):
        """Manejador para clics de mouse (Rotación)"""
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                self.mouse_down = True
                self.last_mouse_x = x
                self.last_mouse_y = y
            elif state == GLUT_UP:
                self.mouse_down = False

    def mouse_motion(self, x, y):
        """Manejador para movimiento del mouse (Rotación)"""
        if self.mouse_down:
            delta_x = x - self.last_mouse_x
            delta_y = y - self.last_mouse_y
            
            self.angle_y += delta_x * self.mouse_sensitivity
            self.angle_x += delta_y * self.mouse_sensitivity
            
            self.last_mouse_x = x
            self.last_mouse_y = y
            
            glutPostRedisplay()

    def mouse_wheel(self, wheel, direction, x, y):
        """Manejador para la rueda del mouse (Zoom)"""
        self.distance += direction * 0.5 
        self.distance = max(self.min_distance, min(self.max_distance, self.distance))
        glutPostRedisplay()

if __name__ == "__main__":
    Teapot3D()