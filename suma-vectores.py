from manim import *

class Suma(Scene):
	def construct(self):

		texto = Text("Suma de vectores: método del paralelógramo").scale(0.5).shift(3.5*UP)
		origin_shift  = 2*DOWN+2.5*LEFT
		v1 = np.array([3,0,0])
		v2 = np.array([2,3,0])
		v3 = v1+v2
		lv1i = Tex("$\\vec{B}$",color="red").shift(0.5*v1+0.5*DOWN+origin_shift)
		lv1f = Tex("$\\vec{B}$",color="red").shift(0.5*v1+0.5*DOWN+v2+origin_shift)
		lv2 = Tex("$\\vec{A}$",color="green").shift(0.5*v2+0.3*LEFT+0.3*UP+origin_shift)
		lv3 = Tex("$\\vec{A}+\\vec{B}$").shift(0.5*v3+0.3*DOWN+0.6*RIGHT+origin_shift)

		vec1i = Vector(v1,color="red").shift(origin_shift)
		vec1id = DashedVMobject(vec1i)
		vec2i = Vector(v2,color="green").shift(origin_shift)
		vec2id = DashedVMobject(vec2i)
		vec3 = Vector(v3).shift(origin_shift)
		vec1fd = DashedVMobject(Vector(v1,color="red")).shift(v2+origin_shift)
		vec2fd = DashedVMobject(Vector(v2,color="green")).shift(v1+origin_shift)
		vec3d = DashedVMobject(vec3)

		self.play(Write(texto))
		self.wait(2)
		self.play(Create(vec2id),Create(vec2i))
		self.play(Create(lv2))
		self.play(Create(vec1id),Create(vec1i))
		self.play(Create(lv1i))
		self.wait(2)
		self.play(Transform(vec1id, vec1fd))
		self.wait(2)
		self.play(Create(vec3),Create(lv3))
		S1 = VGroup(vec2id,vec1id,vec3d,lv3)
		S1b = VGroup(vec1i,vec2i,lv1i,lv2) 
		self.wait(3)
		self.play(ApplyMethod(S1.shift, 3*LEFT), ApplyMethod(S1b.shift, 3*RIGHT), FadeOut(vec3))
		self.wait(3)

	# segunda suma
		vec1i = Vector(v1,color="red").shift(3*RIGHT+origin_shift)
#		vec1id = DashedVMobject(vec1i)
		vec2i = Vector(v2,color="green").shift(3*RIGHT+origin_shift)
		vec2id = DashedVMobject(vec2i)
		lv32 = Tex("$\\vec{B}+\\vec{A}$").shift(0.5*v3+0.3*DOWN+0.6*RIGHT+origin_shift)
		#self.play(Create(vec1id))
		#self.play(Create(vec2id))
		self.play(Transform(vec2id, vec2fd.shift(3*RIGHT)))
		self.wait(2)
		self.play(Create(vec3.shift(3*RIGHT)),Create(lv32.shift(3*RIGHT)))
		self.wait(2)
		S2 = VGroup(S1b,vec2id,vec3)
		self.play(ApplyMethod(S1.shift, 3*RIGHT), ApplyMethod(S2.shift, 3*LEFT), ApplyMethod(lv32.shift,1*LEFT))		
		igual = Tex("$=$").shift(0.5*v3+0.35*DOWN+1.6*RIGHT+origin_shift)
		self.play(Create(igual))
		self.wait(3)