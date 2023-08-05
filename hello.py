# manim -ql hello.py HelloWorld && firefox media/videos/hello/480p15/HelloWorld.mp4 &

from manim import *


class HelloWorld(Scene):
    def construct(self):

        # Intro

        self.wait()
        title = Text("Oral X-ens #1")
        title.scale(1.5)
        title.shift(UP*2)
        self.play(Write(title), run_time=1.5)
        self.play(ApplyMethod(title.shift, UP), run_time=2)
        self.wait()

        problem = Tex(r"Trouver $p,q \in \mathbb{C}$, tels que $X^8+X^4+1$ divise \\ $X^{8m}+pX^{4m}+q$, avec $m \in \mathbb{N}^*$ fixé.")
        self.play(Write(problem))
        self.wait(5)
        self.play(FadeOut(title),FadeOut(problem))

        # Racines 

        t1 = Tex(r"Soit $\omega \in \mathbb C$ une racine de $X^8+X^4+1$, \\ alors $X^8+X^4+1 ~|~ X^{8m}+pX^{4m}+q \Rightarrow \omega^{8m}+p\omega^{4m}+q = 0$.")
        t2 = Tex(r"Cherchons donc les racines de $X^8+X^4+1$.")
        t3 = MathTex(r"X^8+X^4+1 = 0 ")
        t4 = Tex(r"On pose $Y=X^4$,")
        t5 = MathTex(r"Y^2+Y+1 = 0")
        t6 = MathTex(r"\Delta = 1 - 4 ")
        t7 = MathTex(r"\Delta = -3 ")
        t8 = MathTex(r"Y = \frac{-1 \pm i \sqrt 3}{2}")
        t9 = Tex(r"$Y = j$ ou $Y=\bar{j}$ avec $j$ et $\bar{j}$ les racines $3$-ième de l'unité.")
        t10 = Tex(r"$\omega^4 = j$ ou $\omega^4 = \bar{j}$")
        t11 = Tex(r"On a donc :")
        t12 = MathTex(r"\omega^{8m}+p\omega^{4m}+q = 0 ")
        t13 = MathTex(r"(\omega^4)^{2m}+p(\omega^4)^{m}+q = 0 ")
        t14 = MathTex(r"j^{2m}+pj^{m}+q = \bar{j}^{2m}+p\bar{j}^{m}+q = 0 ")

        self.wait(2)
        self.play(Write(t1))
        self.wait(4)
        self.play(ApplyMethod(t1.to_edge, UP))
        self.wait()
        self.play(Write(t2.next_to(t1,DOWN)))
        self.wait(3)
        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4.next_to(t3,LEFT)))
        self.wait(2)
        self.play(Transform(t3,t5))
        self.wait(2)
        self.play(Write(t6.next_to(t3,DOWN)))
        self.play(Transform(t6,t7.next_to(t3,DOWN)))
        self.wait(2)
        self.play(FadeOut(t6))
        self.play(FadeOut(t3))
        self.play(Write(t8.next_to(t4,RIGHT)))
        self.wait(4)
        self.play(Transform(t8,t9.next_to(ORIGIN,DOWN)))
        self.play(ApplyMethod(t4.move_to, ORIGIN))
        self.wait(4)
        self.play(Transform(t2,t10.next_to(t1,DOWN)))
        self.play(FadeOut(t4),FadeOut(t8))
        self.play(Write(t11.to_edge(LEFT)))
        self.play(Write(t12.next_to(t11, direction=DOWN+RIGHT)))
        self.wait(2)
        self.play(Transform(t12,t13.next_to(t11,direction=DOWN+RIGHT)))
        self.wait(2)
        self.play(Transform(t12,t14.next_to(t11,direction=DOWN+RIGHT)))
        self.wait(5)


        # 3 | m

        t15 = Tex(r"Discutons selon la valeur de $m$ :")
        t16 = Tex(r"si $3~|~m$")
        t17 = MathTex(r"1 +p+q=1+p+q=0")
        t18 = MathTex(r"p + q = -1")
        t19 = MathTex(r"S = \{ (p,q) \in \mathbb C^2 ~|~ p+q = -1\}")

        self.play(FadeOut(t1),FadeOut(t2),FadeOut(t11),ApplyMethod(t12.move_to, ORIGIN))
        self.play(Write(t15.next_to(t12,UP)))
        self.wait()
        self.play(ApplyMethod(t15.to_edge, UP))
        self.play(ApplyMethod(t15.shift, LEFT))
        self.play(Write(t16.next_to(t15, RIGHT)))
        self.wait()
        self.remove(t12)
        self.play(TransformFromCopy(t12,t17.move_to(t12)))
        self.wait(2)
        self.play(Transform(t17,t18.move_to(t17)))
        self.wait(2)
        self.play(Transform(t17,t19.move_to(t17)))
        self.wait(4)
        self.play(FadeOut(t17))


        # sinon

        t20 = Tex(r"si $3~\nmid~m$")
        t21 = Tex(r"Soit $\mathbb U_n$ le groupe des racines $n$-ième de l'unité \\ pour la multiplication. On remarque que \\ $x \longmapsto x^m$ est un automorphisme de $\mathbb U_3$")
        t23 = Tex(r"$\dots$")
        t24 = Tex(r"et donc une permuation de $\{1,j,\bar j \}$ \\ dont $1$ est un de ses point fixe !")
        t25 = Tex(r"Nous pouvons donc écrire :")
        t26 = MathTex(r"\iff j^2 + pj + q = \bar j^2 + p \bar j^2 + q = 0")
        t27 = MathTex(r"\iff j^2 + pj + q = j + p j^2 + q = 0")
        t28 = Tex(r"(si vous n'avez pas suivi les calculs, écrivez $j$ et $\bar j$ sous forme expodentielle)").scale(0.75)
        t29 = MathTex(r"\Rightarrow p = q = 1")

        self.play(Transform(t16,t20.next_to(t15,RIGHT)))
        self.wait()
        self.play(Write(t12))
        self.wait(3)
        self.play(ApplyMethod(t12.to_edge, DOWN))
        self.play(Write(t21), run_time = 3)
        self.wait(4)
        self.play(Write(t23.next_to(t21, DOWN)))
        self.wait(2)
        self.play(FadeOut(t23))
        self.play(Write(t24.next_to(t21,DOWN)))
        self.wait(5)
        self.play(FadeOut(t24))
        self.play(FadeOut(t21))
        self.play(Write(t25.next_to(ORIGIN, UP)))
        self.play(ApplyMethod(t12.next_to, t25, DOWN))
        self.wait(2)
        self.play(Write(t26.next_to(t12,DOWN)))
        self.wait(3)
        self.play(Transform(t26, t27.move_to(t26)))
        self.wait(1)
        self.play(Write(t28.next_to(t26,DOWN)))
        self.wait(3)
        self.play(FadeOut(t28))
        self.wait()
        self.play(Write(t29.next_to(t26, DOWN)))
        self.wait(4)


        # Fin

        t30 = Text("Merci d'avoir regardé !")
        t31 = Text("Ma chaîne YouTube : mathemarthur").scale(0.6)
        t32 = Text("Mon site : mathemarthur.fr").scale(0.6)

        self.play(FadeOut(t29),FadeOut(t26),FadeOut(t12),FadeOut(t25),FadeOut(t15), FadeOut(t16), FadeOut(t20))
        self.clear()
        
        self.play(Write(t30))
        self.play(ApplyMethod(t30.shift, UP))
        self.play(Write(t31.next_to(t30,DOWN)))
        self.play(Write(t32.next_to(t31,DOWN)))
        self.wait(3)
        self.play(FadeOut(t31),FadeOut(t32))
        self.play(FadeOut(t30))



    


