from manim import *

# Allows us to change text color of equations
config.tex_template.add_to_preamble(r"\usepackage{xcolor}")

class CombiningPyramids(Scene):
    def construct(self):
        #-------------
        # Create axes
        #-------------
        combiAxes = Axes(
            x_range=[-2.5, 4.5, 1],  # x from -2.5 to 4.5 with step size 1
            y_range=[-0.5, 3.5, 1],  # y from -0.5 to 3.5 with step size 1
            axis_config={"color": WHITE},  # Make axes white for visibility
            tips=False
        ).shift(DOWN*0.8)

        #--------------------
        # Functions to graph
        #--------------------

        # Basic pyramid setup (-1,0) to (0, 1) to (1, 0)
        def combiFunc1(x):
            return (abs(x+1)+abs(x-1)-2*abs(x))/2
        
        # Basic pyramid setup, shifted right one unit (0, 0) to (1, 1) to (2, 0)
        def combiFunc2(x):
            return (abs(x)+abs(x-2)-2*abs(x-1))/2
        
        # Sum of combiFunc1, combiFunc2
        def combiFunc3(x):
            return (abs(x+1)-abs(x)-abs(x-1)+abs(x-2))/2
        
        # Copy of combiFunc3 so we can transform combiFunc1 into combiFunc3 and combiFunc2 into combiFunc3Copy and revert easier
        def combiFunc3Copy(x):
            return (abs(x+1)-abs(x)-abs(x-1)+abs(x-2))/2
        
        # Same as combiFunc1 but height * 2
        def combiFunc4(x):
            return abs(x+1)+abs(x-1)-2*abs(x)
        
        # Same as combiFunc2 but height * 3
        def combiFunc5(x):
            return 3*(abs(x)+abs(x-2)-2*abs(x-1))/2
        
        # Sum of combiFunc4 and combiFunc5
        def combiFunc6(x):
            return (2*abs(x+1)-abs(x)-4*abs(x-1)+3*abs(x-2))/2
        
        # Basic pyramid setup, where our scaling variable $s$ = 2
        def combiFunc7(x):
            return (abs(x+2)+abs(x-2)-2*abs(x))/2
        
        # combiFunc2 but scale variable $s$ = 2
        def combiFunc8(x):
            return (abs(x)+abs(x-4)-2*abs(x-2))/2
        
        def combiFunc9(x):
            return (abs(x+2)-abs(x)-abs(x-2)+abs(x-4))/2

        #-------------------------
        # Plot functions to graph
        #-------------------------

        combiPlot1 = combiAxes.plot(combiFunc1, color=YELLOW, x_range=[-1, 1, 0.01]) # YELLOW = yellow
        combiPlot2 = combiAxes.plot(combiFunc2, color=RED, x_range=[0, 2, 0.01]) # RED = #FC6255
        combiPlot3 = combiAxes.plot(combiFunc3, color=ORANGE, x_range=[-1, 2, 0.01]) # ORANGE = #FF862F

        combiPlot4 = combiAxes.plot(combiFunc4, color=YELLOW, x_range=[-1, 1, 0.01]) # YELLOW = yellow
        combiPlot5 = combiAxes.plot(combiFunc5, color=RED, x_range=[0, 2, 0.01]) # RED = #FC6255
        combiPlot6 = combiAxes.plot(combiFunc6, color=ORANGE, x_range=[-1, 2, 0.01]) # ORANGE = #FF862F

        # Copy of combiPlot6 so we can combine our 2 functions into "1" but it's really 2, so we can separate it easier.
        combiPlot6Copy = combiAxes.plot(combiFunc6, color=ORANGE, x_range=[-1, 2, 0.01]) # ORANGE = #FF862F
        # Copy of combiPlot1 so I can replace stuff later and "restore" back to this by more replacing
        combiPlot7 = combiAxes.plot(combiFunc1, color=YELLOW, x_range=[-1, 1, 0.01]) # YELLOW = yellow
        # Copy of combiFunc2 for the same reason as stated above, in combiFunc7
        combiPlot8 = combiAxes.plot(combiFunc2, color=RED, x_range=[0, 2, 0.01]) # RED = #FC6255

        combiPlot9 = combiAxes.plot(combiFunc7, color=YELLOW, x_range=[-2, 2, 0.01]) # YELLOW = yellow
        combiPlot10 = combiAxes.plot(combiFunc8, color=RED, x_range=[0, 4, 0.01]) # RED = #FC6255
        combiPlot11 = combiAxes.plot(combiFunc9, color=ORANGE, x_range=[-2, 4, 0.01]) # ORANGE = #FF862F

        #----------
        # Formulas
        #----------

        combiForm1 = MathTex(r"f(x) = \textcolor{yellow}{\frac{|x+1|+|x-1|-2|x|}{2}}").shift(UP * 3)
        combiForm2 = MathTex(r"f(x) = \textcolor{yellow}{\frac{|x+1|+|x-1|-2|x|}{2}}, g(x) = \textcolor[HTML]{FC6255}{\frac{|(x-1)+1|+|(x-1)-1|-2|(x-1)|}{2}}").shift(UP * 3).scale(0.75)
        combiForm3 = MathTex(r"(f+g)(x) = \textcolor[HTML]{FF862F}{\frac{|x+1|-|x|-|x-1|+|x-2|}{2}}").shift(UP * 3)
        combiForm4 = MathTex(r"j(x) = \textcolor{yellow}{|x+1|+|x-1|-2|x|}, k(x) = \textcolor[HTML]{FC6255}{\frac{3(|(x-1)+1|+|(x-1)-1|-2|(x-1)|)}{2}}").shift(UP * 3).scale(0.75)
        combiForm5 = MathTex(r"(j+k)(x) = \textcolor[HTML]{FF862F}{\frac{2|x+1|-|x|-4|x-1|+3|x-2|}{2}}").shift(UP * 3)

        # Copy of combiForm2 so we can replace our function with this one because I think I need to since I used a replacement on combiForm2
        combiForm6 = MathTex(r"f(x) = \textcolor{yellow}{\frac{|x+1|+|x-1|-2|x|}{2}}, g(x) = \textcolor[HTML]{FC6255}{\frac{|(x-1)+1|+|(x-1)-1|-2|(x-1)|}{2}}").shift(UP * 3).scale(0.75)

        # combiFunc9, combiFunc10
        combiForm7 = MathTex(r"p(x) = \textcolor{yellow}{\frac{|x+2|+|x-2|-2|x|}{2}}, q(x) = \textcolor[HTML]{FC6255}{\frac{|(x-2)+2|+|(x-2)-2|-2|(x-1)|}{2}}").shift(UP * 3).scale(0.75)

        # combiFunc9 + combiFunc10
        combiForm8 = MathTex(r"(p+q)(x) = \textcolor[HTML]{FF862F}{\frac{|x+2|-|x|-|x-2|+|x-4|}{2}}").shift(UP * 3)

        #-------------------
        # Animate the scene
        #-------------------

        # Create axes
        self.play(Create(combiAxes))

        # Add first function and write equation
        self.play(Create(combiPlot1), Write(combiForm1))
        self.wait(1.5)

        # Add second function, update equation
        self.play(Create(combiPlot2), ReplacementTransform(combiForm1, combiForm2))
        self.wait(1.5)

        # Save the state of these functions to restore later
        combiPlot1.save_state()
        combiPlot2.save_state()
        combiForm2.save_state()

        # Combine combiPlot1, combiPlot2 into combiPlot3, update equation
        self.play(
            Transform(combiPlot1, combiPlot3), 
            Transform(combiPlot2, combiPlot3), 
            Transform(combiForm2, combiForm3)
        )
        self.wait(1.5)

        # Separate the function back into it's 2 separate functions, reverting the equation to match
        self.play(
            Restore(combiPlot1), 
            Restore(combiPlot2), 
            Restore(combiForm2)
        ) 
        self.wait(1.5)

        # Change our pyramids to different heights to show how the slope connects our peaks no matter the height
        self.play(
            ReplacementTransform(combiPlot1, combiPlot4),
            ReplacementTransform(combiPlot2, combiPlot5),
            ReplacementTransform(combiForm2, combiForm4)
        )
        self.wait(1.5)

        # Combine combiPlot4 and combiPlot5 into combiPlot6, updating the equation
        self.play(
            ReplacementTransform(combiPlot4, combiPlot6),
            ReplacementTransform(combiPlot5, combiPlot6Copy),
            ReplacementTransform(combiForm4, combiForm5)
        )
        self.wait(1.5)

        #Revert back to the copies of our original save states since I suck at this
        self.play(
            ReplacementTransform(combiPlot6, combiPlot7),
            ReplacementTransform(combiPlot6Copy, combiPlot8),
            ReplacementTransform(combiForm5, combiForm6)
        )
        self.wait(1.5)

        # Scale the functions to 2 times their size
        self.play(
            ReplacementTransform(combiPlot7, combiPlot9),
            ReplacementTransform(combiPlot8, combiPlot10),
            ReplacementTransform(combiForm6, combiForm7)
        )
        self.wait(1.5)

        # Combine them into a single function
        self.play(
            ReplacementTransform(combiPlot9, combiPlot11),
            ReplacementTransform(combiPlot10, combiPlot11),
            ReplacementTransform(combiForm7, combiForm8)
        )
        self.wait(2.5)