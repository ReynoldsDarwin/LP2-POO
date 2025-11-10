from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import sys
import os 

class Cube3D:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.mouse_down = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_sensitivity = 0.5 
        self.distance = -6.0
        self.min_distance = -15.0
        self.max_distance = -3.0
        self.texture_ids = []
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.init_window()
        print("Cargando texturas...")
        nombres_texturas = [
            "1.jpg", "2.png", "3.jpg",
            "4.png", "5.png", "6.png"
        ]
        
        for nombre in nombres_texturas:
            tex_id = self.cargar_textura(nombre) 
            if tex_id == 0:
                print(f"Error fatal: No se pudo cargar '{nombre}'. Saliendo.")
                sys.exit()
            self.texture_ids.append(tex_id)
        
        print("Texturas cargadas exitosamente.")
        
        glutMainLoop()
    
    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(600, 600)
        glutCreateWindow(b"Cubo 3D con Texturas y Transparencia")
        self.init_lighting()
        glEnable(GL_DEPTH_TEST) 
        glClearColor(0.4, 0.1, 1, 1.0) 
        glutDisplayFunc(self.display)
        glutSpecialFunc(self.keyboard_special)
        glutMouseFunc(self.mouse_click)
        glutMotionFunc(self.mouse_motion)
        glutMouseWheelFunc(self.mouse_wheel)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 50)
        glMatrixMode(GL_MODELVIEW)

    def init_lighting(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_CULL_FACE) 
        light_position = [5.0, 5.0, 5.0, 1.0]
        light_ambient = [0.2, 0.2, 0.2, 1.0]
        light_diffuse = [0.8, 0.8, 0.8, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
        mat_ambient = [1.0, 1.0, 1.0, 1.0]
        mat_diffuse = [1.0, 1.0, 1.0, 1.0]
        mat_specular = [1.0, 1.0, 1.0, 1.0]
        mat_shininess = [50.0]
        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)


    def cargar_textura(self, ruta_imagen):
        """Carga una imagen (JPG o PNG) y la prepara como textura."""
        ruta_completa = os.path.join(self.script_dir, ruta_imagen)
        
        try:
            img = Image.open(ruta_completa) 
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img_data = img.convert("RGBA").tobytes() 
            
            textura_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, textura_id)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 
                           0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
            
            return textura_id
        
        except FileNotFoundError:
            print(f"ERROR: No se encontró el archivo de textura en: {ruta_completa}")
            return 0

    def draw_cube(self):
        s = 1.0
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[0])
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-s, -s, s)
        glTexCoord2f(1.0, 0.0); glVertex3f( s, -s, s)
        glTexCoord2f(1.0, 1.0); glVertex3f( s,  s, s)
        glTexCoord2f(0.0, 1.0); glVertex3f(-s,  s, s)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[1])
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, -1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(-s, -s, -s)
        glTexCoord2f(1.0, 1.0); glVertex3f(-s,  s, -s)
        glTexCoord2f(0.0, 1.0); glVertex3f( s,  s, -s)
        glTexCoord2f(0.0, 0.0); glVertex3f( s, -s, -s)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[2])
        glBegin(GL_QUADS)
        glNormal3f(-1.0, 0.0, 0.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-s, -s, -s)
        glTexCoord2f(1.0, 0.0); glVertex3f(-s, -s,  s)
        glTexCoord2f(1.0, 1.0); glVertex3f(-s,  s,  s)
        glTexCoord2f(0.0, 1.0); glVertex3f(-s,  s, -s)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[3])
        glBegin(GL_QUADS)
        glNormal3f(1.0, 0.0, 0.0)
        glTexCoord2f(1.0, 0.0); glVertex3f( s, -s, -s)
        glTexCoord2f(1.0, 1.0); glVertex3f( s,  s, -s)
        glTexCoord2f(0.0, 1.0); glVertex3f( s,  s,  s)
        glTexCoord2f(0.0, 0.0); glVertex3f( s, -s,  s)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[4])
        glBegin(GL_QUADS)
        glNormal3f(0.0, 1.0, 0.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(-s,  s, -s)
        glTexCoord2f(0.0, 0.0); glVertex3f(-s,  s,  s)
        glTexCoord2f(1.0, 0.0); glVertex3f( s,  s,  s)
        glTexCoord2f(1.0, 1.0); glVertex3f( s,  s, -s)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[5])
        glBegin(GL_QUADS)
        glNormal3f(0.0, -1.0, 0.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(-s, -s, -s)
        glTexCoord2f(0.0, 1.0); glVertex3f( s, -s, -s)
        glTexCoord2f(0.0, 0.0); glVertex3f( s, -s,  s)
        glTexCoord2f(1.0, 0.0); glVertex3f(-s, -s,  s)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, self.distance) 
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0) 
        self.draw_cube()
        glutSwapBuffers()

    def keyboard_special(self, key, x, y):
        if key == GLUT_KEY_RIGHT: self.angle_y += 5
        elif key == GLUT_KEY_LEFT: self.angle_y -= 5
        elif key == GLUT_KEY_UP: self.angle_x -= 5
        elif key == GLUT_KEY_DOWN: self.angle_x += 5
        glutPostRedisplay() 

    def mouse_click(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                self.mouse_down = True
                self.last_mouse_x = x
                self.last_mouse_y = y
            elif state == GLUT_UP:
                self.mouse_down = False

    def mouse_motion(self, x, y):
        if self.mouse_down:
            delta_x = x - self.last_mouse_x
            delta_y = y - self.last_mouse_y
            self.angle_y += delta_x * self.mouse_sensitivity
            self.angle_x += delta_y * self.mouse_sensitivity
            self.last_mouse_x = x
            self.last_mouse_y = y
            glutPostRedisplay()

    def mouse_wheel(self, wheel, direction, x, y):
        self.distance += direction * 0.5
        self.distance = max(self.min_distance, min(self.max_distance, self.distance))
        glutPostRedisplay()

if __name__ == "__main__":
    print("Iniciando aplicación...")
    Cube3D()