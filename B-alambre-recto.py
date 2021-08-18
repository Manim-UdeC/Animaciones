# By Nataly Ibarra https://github.com/nataly-nicole
from manimlib.imports import *
mu0 = 4.*np.pi *1e-7 #TmA^{-1}
#I = 1. #A
eps = 0.000001
#point = [1,0,0]

class vector3D():
    def __init__(self, point):
        [x, y, z] = point[0:3]
        self.vr = np.array([x, y, z]) 
        self.coordinate_x = x
        self.coordinate_y = y
        self.coordinate_z = z
#Cilindric Coordinates
        self.coordinate_rho = np.sqrt(eps**2+x**2 + y**2)
        self.coordinate_phi = np.arctan(y/x)
        self.vu_rho = np.array([x/self.coordinate_rho, y/self.coordinate_rho, 0])
        self.vu_phi = np.array([-y/self.coordinate_rho, x/self.coordinate_rho, 0])
#Spheric Coordinates
        self.coordinate_r = np.sqrt(x**2 + y**2 + z**2)
        self.coordinate_theta = np.arccos(z/self.coordinate_r)
        self.vu_r = self.vr/self.coordinate_r
        self.vu_theta = np.array([(z*x)/(self.coordinate_rho*self.coordinate_r), (z*y)/(self.coordinate_rho*self.coordinate_r), self.coordinate_rho/self.coordinate_r])

def MagneticField(point):
    I = 0.5e7 #A
    vec = vector3D(point)
    eps = 0.000001 #Parámetro ajustado para evitar dividir por cero
    return (mu0*I/(2.*np.pi*(eps+vec.coordinate_rho)))*vec.vu_phi

def B_rho(rho):
    I = 0.5e7 #A
    eps = 0.000001 #Parámetro ajustado para evitar dividir por cero
    return (mu0*I/(2.*np.pi*(eps+rho)))

class MagneticFieldWire3D(ThreeDScene):
    def construct(self):
        axes_config = {
            "x_min": -6.5,
            "x_max": 6.5,
            "delta_x": 0.5,
#            "x_axis_width": 15,
            "x_tick_frequency": 1,
            "x_leftmost_tick": 0,
            "x_labeled_nums": None,
            "x_axis_label": None,
#
            "y_min": -6.5,
            "y_max": 6.5,
            "delta_y": 0.5,
            "y_axis_height": 10,
            "y_tick_frequency": 1,
            "y_bottom_tick": None, 
            "y_labeled_nums": None,
            "y_axis_label": None,
#
            "z_min": -3.5,
            "z_max": 3.5,
            "delta_z": 0.5,
            "z_axis_height": 10,
#
        "axes_color": LIGHT_GREY,
        "light_source": 15 * DOWN + 7 * LEFT + 10 * OUT,
        }
#Se configura la cámara y los ejes cartesianos
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES, distance=16)
        axes = ThreeDAxes(**axes_config)
        axis_labels = axes.get_3axis_labels(x_edge=RIGHT, x_direction=RIGHT, y_edge=UP, y_direction=UP, z_edge=OUT, z_direction=RIGHT)
        self.add_fixed_orientation_mobjects(axis_labels[0])
        self.add_fixed_orientation_mobjects(axis_labels[1])
        self.add_fixed_orientation_mobjects(axis_labels[2])
#Se confifigura texto
        text3d = Text("Alambre Infinito" , font = 'Times New Roman')
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
#Se configura línea infinita y texto de la corriente
        line = Line([0, 0, -6], [0, 0, 6], stroke_width=10).set_color(BLUE).set_opacity(0)
        line2 = Line([0, 0, -15], [0, 0, 15], stroke_width=10).set_color(BLUE)
        text_current = TexMobject('I').next_to([0,0,1], RIGHT)
        self.add_fixed_orientation_mobjects(text_current)
#        self.add(axes, line, line2, text_current)
        self.add(axes, line2, text_current)
#        self.add(axes, text_current)
#Se dibujan las cargas eléctricas de la corriente
        dot_m10 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -10])
        dot_m095 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -9.5])
        dot_m09 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -9])
        dot_m085 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -8.5])
        dot_m08 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -8])
        dot_m075 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -7.5])
        dot_m07 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -7])
        dot_m065 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -6.5])
        dot_m06 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -6])
        dot_m055 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -5.5])
        dot_m05 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -5])
        dot_m045 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -4.5])
        dot_m04 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -4])
        dot_m035 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -3.5])
        dot_m03 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -3])
        dot_m025 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -2.5])
        dot_m02 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -2])
        dot_m015 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -1.5])
        dot_m01 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -1])
        dot_m0055 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, -0.5])
        dot_00 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 0])
        dot_p0055 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 0.5])
        dot_p01 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 1])
        dot_p015 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 1.5])
        dot_p02 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 2])
        dot_p025 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 2.5])
        dot_p03 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 3])
        dot_p035 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 3.5])
        dot_p04 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 4])
        dot_p045 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 4.5])
        dot_p05 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 5])
        dot_p055 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 5.5])
        dot_p06 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 6])
        dot_p065 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 6.5])
        dot_p07 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 7])
        dot_p075 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 7.5])
        dot_p08 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 8])
        dot_p085 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 8.5])
        dot_p09 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 9])
        dot_p095 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 9.5])
        dot_p10 = Sphere(radius = 0.05).set_color(RED).move_to([0, 0, 10])
        group00 = (Group(dot_m10, dot_m095, dot_m09, dot_m085, dot_m08, dot_m075, dot_m07, dot_m065, dot_m06, dot_m055, dot_m05, dot_m045, dot_m04, dot_m035, dot_m03, dot_m025, dot_m02, dot_m015, dot_m01, dot_m0055, dot_00,
                 dot_p0055, dot_p01, dot_p015, dot_p02, dot_p025, dot_p03, dot_p035, dot_p04, dot_p045, dot_p05, dot_p055, dot_p06, dot_p065, dot_p07, dot_p075, dot_p08, dot_p085, dot_p09, dot_p095, dot_p10))
        self.add(group00)
        self.play(MoveAlongPath(group00, line), run_time=3, rate_func=linear)
#Se configura texto de la expresión del campo magnético
        text_field = TexMobject("\\vec{B} (\\vec{r}) = \\frac{\mu_{0}I}{2\pi \\rho} \\hat{\\varphi}")
        self.add_fixed_in_frame_mobjects(text_field)
        text_field.to_corner(UR)
########
#Se configura texto y campo magnético normalizado
        text_field_kind = Text("Campo Magnético normalizado" , font = 'Times New Roman')
        self.add_fixed_in_frame_mobjects(text_field_kind)
        text_field_kind.to_corner(DR)
        vector_field_norm = VectorField(MagneticField,
            delta_x = 0.5, delta_y = 0.5, delta_z = 0.8,
            x_min = -5.5, x_max = 5.5,
            y_min = -5.5, y_max = 5.5,
            z_min = -3.5,z_max = 3.5)
        self.play(MoveAlongPath(group00, line), ShowCreation(vector_field_norm), FadeOut(text_field_kind), run_time=3, rate_func=linear)
#Se configura texto y campo magnético no normalizado
        text_field_kind = Text("Campo Magnético no normalizado" , font = 'Times New Roman')
        self.add_fixed_in_frame_mobjects(text_field_kind)
        text_field_kind.to_corner(DR)
        vector_field_not_norm = VectorField(MagneticField,
            delta_x = 0.5, delta_y = 0.5, delta_z = 0.8,
            x_min = -5.5, x_max = 5.5,
            y_min = -5.5, y_max = 5.5,
            z_min = -3.5, z_max = 3.5,
            length_func=linear)
        self.play(MoveAlongPath(group00, line), ReplacementTransform(vector_field_norm, vector_field_not_norm), FadeOut(text_field_kind), run_time=3, rate_func=linear)
#Se rota la cámara para mirar perpendicularmente al plano xy
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, distance=12, added_anims = [FadeOut(axis_labels[2], MoveAlongPath(group00, line)), FadeOut(line2), FadeOut(group00, text_current.move_to([1,1,0]))], run_time=3, rate_func=linear)
#        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, distance=12, added_anims = [FadeOut(axis_labels[2], MoveAlongPath(group00, line)), FadeOut(group00, text_current.move_to([1,1,0]))])
        self.wait(1)
#        self.add(line2)
#        self.add(group00)
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, distance=16, added_anims = [MoveAlongPath(group00, line), FadeIn(group00), FadeIn(axis_labels[2]), FadeIn(line), FadeIn(line2), FadeIn(group00, text_current.next_to([0,0,1], RIGHT)), MoveAlongPath(group00, line)], run_time=3, rate_func=linear)
#        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, distance=16, added_anims = [ShowCreation(line2), FadeIn(group00), MoveAlongPath(group00, line) ])
#        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, distance=16, added_anims = [MoveAlongPath(group00, line), FadeIn(axis_labels[2], text_current.next_to([0,0,1], RIGHT))])
#        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, distance=16, added_anims = [MoveAlongPath(group00, line), FadeIn(axis_labels[2], text_current.next_to([0,0,1], RIGHT))])
        self.play(MoveAlongPath(group00, line), run_time=3, rate_func=linear)
#
        grupo01 = Group(line, line2, group00, axes, axis_labels, text_current, vector_field_not_norm)
#        grupo01 = Group(line, group00, axes, axis_labels, text_current, vector_field_not_norm)
        grupo01_rot = Rotating(grupo01, radians=PI/2, axis=[1,0,0], about_point=[0,0,0])
        self.play(MoveAlongPath(group00, line), grupo01_rot, run_time=3, rate_func=linear)
#Se rota la cámara para ver la simetría axial
        self.begin_ambient_camera_rotation(rate =1)
        self.play(MoveAlongPath(group00, line), run_time=3, rate_func=linear)
        self.stop_ambient_camera_rotation()
#        self.wait()

class MagneticFieldWire2D(Scene):
    def construct(self):
        axes_config2 = {
            "x_min": -6.5,
            "x_max": 6.5,
            "delta_x": 0.5,
#            "x_axis_width": 15,
            "x_tick_frequency": 1,
            "x_leftmost_tick": 0,
            "x_labeled_nums": None,
            "x_axis_label": None,
#
            "y_min": -3.5,
            "y_max": 3.5,
            "delta_y": 0.5,
            "y_axis_height": 13,
            "y_tick_frequency": 1,
            "y_bottom_tick": None, # Change if different from y_min
            "y_labeled_nums": None,
            "y_axis_label": None,
#
            "axes_color": LIGHT_GREY,
            "graph_origin": 0 * DOWN + 0 * LEFT,
            "exclude_zero_label": True,
            "num_graph_anchor_points": 25,
            "default_graph_colors": GOLD,
            "default_derivative_color": GREEN,
            "default_input_color": YELLOW,
            "default_riemann_start_color": BLUE,
            "default_riemann_end_color": GREEN,
            "function_color": WHITE,
            "area_opacity": 0.8,
            "num_rects": 50,
            "light_source": 15 * DOWN + 7 * LEFT + 10 * OUT,
            "number_line_config": {"include_tip": False,},
            }
#Se configuran los ejes cartesianos
        axes = Axes(**axes_config2)
        axis_labels = axes.get_axis_labels(x_edge=RIGHT, x_direction=RIGHT, y_edge=UP, y_direction=UP)
#
        text3d = Text("Alambre Infinito" , font = 'Times New Roman')
        text3d.to_corner(UL)
#
        dot = Dot().set_color(BLUE)
        circle = Circle(radius=0.2, color=BLUE)
        text_current = TexMobject('I').next_to([0.1, -0.1, 0], DR)
        text_field = TexMobject("\\vec{B} (\\vec{r}) = \\frac{\mu_{0}I}{2\pi \\rho} \\hat{\\varphi}")
        text_field.to_corner(DL)
        self.add(axes, dot, circle, text_current, text3d, axis_labels, text_field)
##
        point = [2, 2, 0]
        dot = Dot(point).set_color(RED)
        vec = vector3D(point)
        arrow_vec = Arrow(ORIGIN, vec.vr, buff=0)
        arc_phi = Arc(start_angle=0, angle=vec.coordinate_phi, radius=1.2)
        arrow_vec_vu_rho = Arrow(vec.vr, vec.vr+vec.vu_rho, buff=0)
        arrow_vec_vu_phi = Arrow(vec.vr, vec.vr+vec.vu_phi, buff=0)
        text_vec = TexMobject('\\vec{r}').next_to([1,1,0], RIGHT)
        text_rho = TexMobject('\\rho').next_to([1,1,0], LEFT)
        text_phi = TexMobject('\\varphi').next_to([0.3,0.3,0], RIGHT)
        text_vu_rho = TexMobject('\hat{\\rho}').next_to(vec.vr+vec.vu_rho, UR)
        text_vu_phi = TexMobject('\hat{\\varphi}').next_to(vec.vr+vec.vu_phi, DL)
#
#        B_point = MagneticField(point)
        B_point = 4.*MagneticField(point)
        arrow_B = Arrow(vec.vr, vec.vr + B_point, buff = 0).set_color(GREEN)
        arrow_B.set_stroke_width_from_length()
        text_B = TexMobject('\\vec{B}(\\vec{r})').next_to(vec.vr + B_point, UR)
        circle = Circle(radius = vec.coordinate_r).set_color(GRAY)
        group01 = Group(dot, arrow_vec, text_vec, text_rho, arc_phi, text_phi, arrow_vec_vu_rho, text_vu_rho, arrow_vec_vu_phi, text_vu_phi, circle)
        self.play(ShowCreation(group01, run_time=3))
        group02 = Group(dot, arrow_vec, text_vec, text_rho, arrow_vec_vu_rho, text_vu_rho, arrow_vec_vu_phi, text_vu_phi, circle)
##
        text_field_kind = Text("Campo Magnético normalizado", font = 'Times New Roman')
        text_field_kind.to_corner(DR)
        vector_field_norm = VectorField(MagneticField,
            delta_x = 0.5,
            delta_y = 0.5,
            x_min = -10,
            x_max = 10,
            y_min = -4.5,
            y_max = 4.5,
            )
        self.play(ShowCreation(vector_field_norm), FadeOut(text_field_kind), run_time=3, rate_func=linear)
#
        text_field_kind = Text("Campo Magnético no normalizado", font = 'Times New Roman')
        text_field_kind.to_corner(DR)
        vector_field_not_norm = VectorField(MagneticField,
            delta_x = 0.5,
            delta_y = 0.5,
            x_min = -10,
            x_max = 10,
            y_min = -4.5,
            y_max = 4.5,
            length_func=linear)
##
        self.play(ReplacementTransform(vector_field_norm, vector_field_not_norm), FadeOut(text_field_kind), run_time=3, rate_func=linear)
        self.wait(3)

class MagneticFieldWire_Graphics(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0.1,
            x_max=10,
            y_min=-1,
            y_max=5,
            x_axis_label= r"$\rho$",
            y_axis_label= r"$B_{\varphi}(\rho)$",
            **kwargs
        )
        self.function_color = RED


    def construct(self):
        self.setup_axes(animate=False)
        func_graph = self.get_graph(B_rho, RED)
        self.add(func_graph)
        self.wait(1)

