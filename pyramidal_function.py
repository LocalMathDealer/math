from manim import *

config.tex_template.add_to_preamble(r"\usepackage{xcolor}")

class PyramidalFunction(Scene):
    def construct(self):
        # Create the axis
        introAxes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"color": WHITE},
            tips=False
        ).shift(DOWN * 0.8)

        # Function definitions
        def introFunc1(x):
            return -abs(x) + 1

        def introFunc2(x):
            return -abs(x + 1)

        def introFunc3(x):
            return -abs(x - 1)

        def introFunc4(x):
            return -abs(x) - 1
        
        # Simplified with artificial graphs
        def introFunc5(x):
            return -abs(x) + 1
        
        def introFunc6(x):
            return abs(x) - 1
        
        def introFunc7(x):
            return abs(x-1)+abs(x+1)-2*abs(x)
        
        def introFunc8(x):
            return (abs(x-1)+abs(x+1)-2*abs(x))/2

        introForm1 = MathTex(r"f(x) = \textcolor{yellow}{-|x| + 1}").shift(UP * 3)
        introForm2 = MathTex(r"f(x) = (\textcolor{yellow}{-|x|+1}) - (\textcolor[HTML]{FC6255}{-|x+1|})").shift(UP * 3)
        introForm3 = MathTex(r"f(x) = (\textcolor{yellow}{-|x|+1}) - (\textcolor[HTML]{FC6255}{-|x+1| + -|x-1|})").shift(UP * 3)
        introForm4 = MathTex(r"f(x) = (\textcolor{yellow}{-|x|+1}) - ((\textcolor[HTML]{FC6255}{-|x+1| + -|x-1|})-(\textcolor[HTML]{58C4DD}{-|x|-1}))").shift(UP * 3)
        introForm5 = MathTex(r"f(x) = |x+1| + |x-1| - 2|x|").shift(UP * 3)
        introForm6 = MathTex(r"f(x) = \frac{|x+1| + |x-1| - 2|x|}{2}").shift(UP * 3)

        # Graphs with matching colors (just plotting the line, no area filling)
        introGraph1 = introAxes.plot(introFunc1, color=YELLOW, x_range=[-3, 3, 0.01])
        introGraph2 = introAxes.plot(introFunc2, color="#FC6255", x_range=[-3, 3, 0.01])  # Match red shade
        introGraph3 = introAxes.plot(introFunc3, color="#FC6255", x_range=[-3, 3, 0.01])
        introGraph4 = introAxes.plot(introFunc4, color=BLUE, x_range=[-3, 3, 0.01])

        introGraph5 = introAxes.plot(introFunc5, color=YELLOW, x_range=[-1, 1, 0.01])
        introGraph6 = introAxes.plot(introFunc6, color=RED, x_range=[-1, 1, 0.01])
        introGraph7 = introAxes.plot(introFunc7, color=YELLOW, x_range=[-1, 1, 0.01])
        introGraph8 = introAxes.plot(introFunc8, color=YELLOW, x_range=[-1, 1, 0.01])

        # Scene animation
        self.add(introAxes)

        # Animate the creation of the first graph and equation
        self.play(Create(introGraph1), Write(introForm1))
        self.wait(1.5)

        # Animate the creation of the second graph and update the equation
        self.play(Create(introGraph2), ReplacementTransform(introForm1, introForm2))
        self.wait(1.5)

        # Animate the creation of the third graph and update the equation
        self.play(Create(introGraph3), ReplacementTransform(introForm2, introForm3))
        self.wait(1.5)

        # Animate the creation of the fourth graph and update the equation
        self.play(Create(introGraph4), ReplacementTransform(introForm3, introForm4))
        self.wait(1.5)

        # Finally, create the smaller graphs and add to the scene
        self.play(Create(introGraph5), Create(introGraph6))

        # Fade out the first 4 graphs
        self.play(
            FadeOut(introGraph1, introGraph2, introGraph3, introGraph4)
        )
        self.wait(1.5)  # Give a little time before the scene ends
        self.play(
            ReplacementTransform(introForm4, introForm5),
            ReplacementTransform(introGraph5, introGraph7),
            ReplacementTransform(introGraph6, introGraph7)
        )
        self.wait(1.5)
        self.play(
            ReplacementTransform(introForm5, introForm6),
            ReplacementTransform(introGraph7, introGraph8)
        )
        self.wait(2.5)