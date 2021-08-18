from manim import *

class Resta(Scene):

	def construct(self):
		origin_shift  = 0.5*DOWN+2*LEFT
		vB = np.array([3,0,0])
		vA = np.array([2,3,0])
		vmB = -vB
		vR = vA-vB
		texto = Text("Resta de vectores").scale(0.5).shift(3.8*UP)

		lvA = Tex("$\\vec{A}$",color="green").shift(0.5*vA+0.3*LEFT+0.3*UP+origin_shift)
		lvR1 = Tex("$\\vec{A}+(-\\vec{B})$").shift(0.5*vR+0.3*DOWN+1.1*LEFT+origin_shift)
		lvR2 = Tex("$\\vec{A}-\\vec{B}$").shift(0.5*vR+0.3*DOWN+vB+1*RIGHT+origin_shift)

		lvB = Tex("$\\vec{B}$",color="red").shift(0.5*vB+0.5*DOWN+origin_shift)
		lvB2 = Tex("$\\vec{B}$",color="red").shift(0.5*vB+0.5*DOWN+origin_shift)
		lvmB = Tex("$-\\vec{B}$",color="red").shift(-0.5*vB+0.5*DOWN+origin_shift)
	
		vecAi = Vector(vA,color="green").shift(origin_shift)
		vecAid = DashedVMobject(vecAi)
		vecR = Vector(vR).shift(origin_shift)
		vecB = Vector(vB,color="red").shift(origin_shift)
		vecBd = DashedVMobject(vecB)

		vecmBd = DashedVMobject(Vector(vmB,color="red")).shift(origin_shift)
		vecBd = DashedVMobject(Vector(vB,color="red")).shift(origin_shift)
		vecRd = DashedVMobject(vecR).shift(origin_shift)

		self.play(Write(texto))
		self.wait(2)
		self.play(Create(vecAi))
		self.play(Create(lvA))
		self.play(Create(vecBd),Create(vecB))
		self.play(Create(lvB),Create(lvB2))
		self.wait(2)
		self.play(Transform(vecBd, vecmBd),Transform(lvB, lvmB))
		self.wait(2)
		self.play(ApplyMethod(vecBd.shift, vA),ApplyMethod(lvB.shift, vA+UP))
		self.play(Create(vecR))
		self.play(Create(lvR1))
		self.wait(2)
		self.play(ApplyMethod(vecR.shift,vB), Transform(lvR1,lvR2), FadeOut(vecBd), FadeOut(lvB))
		self.wait(4)

		vecmAd = DashedVMobject(Vector(-vA,color="green")).shift(origin_shift)
		lmA = Tex("$-\\vec{A}$",color="green").shift(-0.5*vA+0.5*LEFT+0.3*UP+origin_shift)
		lvA2 = Tex("$\\vec{A}$",color="green").shift(0.5*vA+0.3*LEFT+0.3*UP+origin_shift)

		self.play(Transform(vecAid,vecmAd), Transform(lvA2,lmA))
		self.wait(2)
		self.play(ApplyMethod(vecAid.shift,vB),ApplyMethod(lvA2.shift,vB))
		self.wait(2)

		vecR2 = Vector(-vR).shift(origin_shift)
		self.play(Create(vecR2))
		lvR3 = Tex("$\\vec{B}-\\vec{A}$").shift(-0.5*vR+0.3*DOWN+vB+4*LEFT+origin_shift)
		self.play(Create(lvR3))
		self.wait(2)
		self.play(ApplyMethod(vecR2.shift,0.95*vA),ApplyMethod(lvR3.shift,vA), FadeOut(vecAid), FadeOut(lvA2))
		self.wait(2)
		
