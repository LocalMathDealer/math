from manim import *

# Allows us to change text color of equations
config.tex_template.add_to_preamble(r"\usepackage{xcolor}")

class Integration(Scene):
    def construct(self):
        #-------------
        # Create axes
        #-------------
        inteAxes = Axes(
            x_range=[-4.5, 4.5, 1],  # x from -2.5 to 4.5 with step size 1
            y_range=[-0.5, 1.5, 1],  # y from -0.5 to 3.5 with step size 1
            axis_config={"color": WHITE},  # Make axes white for visibility
            tips=False
        ).shift(DOWN*0.8)

        inteAxesSquared = Axes(
            x_range=[-4.5, 4.5, 1],  # x from -2.5 to 4.5 with step size 1
            y_range=[-0.25, 9.5, 1],  # y from -0.5 to 3.5 with step size 1
            axis_config={"color": WHITE},  # Make axes white for visibility
            tips=False
        ).shift(DOWN*0.8)

        # Custom y-ticks at 1, 4, and 9
        y_tick_values = [1, 4, 9]
        y_ticks = VGroup(*[
            inteAxesSquared.get_y_axis().get_tick(y, size=0.1) for y in y_tick_values
        ])

        # Labels for those ticks
        y_labels = VGroup(*[
            Text(str(y), font_size=24).next_to(inteAxesSquared.c2p(0, y), LEFT, buff=0.2)
            for y in y_tick_values
        ])

        #-----------
        # Functions
        #-----------

        #
        # Pyramidal functions w/ height of 1 (left to right)
        #

        # x={-4, -2}
        def inteFunc1(x):
            return (abs(x+4)+abs(x+2)-2*abs(x+3))/2
        # x={-3, -1}
        def inteFunc2(x):
            return (abs(x+3)+abs(x+1)-2*abs(x+2))/2
        # x={-2, 0}
        def inteFunc3(x):
            return (abs(x+2)+abs(x)-2*abs(x+1))/2
        # x={-1, 1}
        def inteFunc4(x):
            return (abs(x+1)+abs(x-1)-2*abs(x))/2
        # x={0, 2}
        def inteFunc5(x):
            return (abs(x)+abs(x-2)-2*abs(x-1))/2
        # x={1, 3}
        def inteFunc6(x):
            return (abs(x-1)+abs(x-3)-2*abs(x-2))/2
        # x={2, 4}
        def inteFunc7(x):
            return (abs(x-2)+abs(x-4)-2*abs(x-3))/2
        
        # Sum of all of our pyramids. Trapezoidal function w/ vertices (-4, 0), (-3, 1), (3, 1), (4, 0)
        # This will be used to create smoother animations where our pyramids combine into the line above them as opposed to the whole function
        # - Create the equation for the line
        # - Assign a variable that plots specific ranges (matching the pyramidal functions)
        # - Transform each pyramid into the line above it

        def basicSum(x):
            functions = [inteFunc1, inteFunc2, inteFunc3, inteFunc4, inteFunc5, inteFunc6, inteFunc7]
            return sum(f(x) for f in functions)

        #
        # Variables needed for Approx. Integral of x^2
        #

        # x^2
        def inteFuncSquared(x):
            return x*x
        
        # (-3)^2 * pyramid centered at x={-3}
        def inteFuncSquared1(x):
            return 9 * inteFunc1(x)
        # (-2)^2 * pyramid centered at x={-2}
        def inteFuncSquared2(x):
            return 4 * inteFunc2(x)
        # (-1)^2 * pyramid centered at x={-1}
        def inteFuncSquared3(x):
            return 1 * inteFunc3(x)
        # 0 * pyramid centered at x={0}
        def inteFuncSquared4(x):
            return 0 * inteFunc4(x)
        # (1)^2 * pyramid centered at x={1}
        def inteFuncSquared5(x):
            return 1 * inteFunc5(x)
        # (2)^2 * pyramid centered at x={2}
        def inteFuncSquared6(x):
            return 4 * inteFunc6(x)
        # (3)^2 * pyramid centered at x={3}
        def inteFuncSquared7(x):
            return 9 * inteFunc7(x)
        # (4)^2 * pyramid centered at x={4}
        def inteFuncSquared(x):
            return x*x
        
        # Sum of these pyramids
        def squareSum(x):
            functions = [inteFuncSquared1, inteFuncSquared2, inteFuncSquared3, inteFuncSquared4, inteFuncSquared5, inteFuncSquared6, inteFuncSquared7]
            return sum(f(x) for f in functions)

        #-------------------------
        # Plot functions to graph
        #-------------------------

        # Basic Pyramids
        intePlot1 = inteAxes.plot(inteFunc1, color=YELLOW, x_range=[-4, -2, 0.01])
        intePlot2 = inteAxes.plot(inteFunc2, color=YELLOW, x_range=[-3, -1, 0.01])
        intePlot3 = inteAxes.plot(inteFunc3, color=YELLOW, x_range=[-2, 0, 0.01])
        intePlot4 = inteAxes.plot(inteFunc4, color=YELLOW, x_range=[-1, 1, 0.01])
        intePlot5 = inteAxes.plot(inteFunc5, color=YELLOW, x_range=[0, 2, 0.01])
        intePlot6 = inteAxes.plot(inteFunc6, color=YELLOW, x_range=[1, 3, 0.01])
        intePlot7 = inteAxes.plot(inteFunc7, color=YELLOW, x_range=[2, 4, 0.01])

        # Segmented lines of basicSum - for smoother animation
        intePlotStraight1 = inteAxes.plot(basicSum, color=BLUE, x_range=[-4, -2, 0.01])
        intePlotStraight2 = inteAxes.plot(basicSum, color=BLUE, x_range=[-3, -1, 0.01])
        intePlotStraight3 = inteAxes.plot(basicSum, color=BLUE, x_range=[-2, 0, 0.01])
        intePlotStraight4 = inteAxes.plot(basicSum, color=BLUE, x_range=[-1, 1, 0.01])
        intePlotStraight5 = inteAxes.plot(basicSum, color=BLUE, x_range=[0, 2, 0.01])
        intePlotStraight6 = inteAxes.plot(basicSum, color=BLUE, x_range=[1, 3, 0.01])
        intePlotStraight7 = inteAxes.plot(basicSum, color=BLUE, x_range=[2, 4, 0.01])
        # Whole straight line of basicSum - to replace the segments
        intePlotStraightSum = inteAxes.plot(basicSum, color=BLUE, x_range=[-4, 4, 0.01])
        #Hide the whole line behind the rest to cover up the creation
        intePlotStraightSum.z_index = -1
        #Ensure our pyramids on the outer sides remain on top of our (blue) sum line
        intePlotStraight1.z_index = 1
        intePlotStraight7.z_index = 1

        # So I still suck at Manim and I don't know how to use transform, restore, and replacementtransform (and whatnot) without breaking everything
        # So here are some manual copies of our previous intePlotx functions
        intePlota1 = inteAxes.plot(inteFunc1, color=YELLOW, x_range=[-4, -2, 0.01])
        intePlota2 = inteAxes.plot(inteFunc2, color=YELLOW, x_range=[-3, -1, 0.01])
        intePlota3 = inteAxes.plot(inteFunc3, color=YELLOW, x_range=[-2, 0, 0.01])
        intePlota4 = inteAxes.plot(inteFunc4, color=YELLOW, x_range=[-1, 1, 0.01])
        intePlota5 = inteAxes.plot(inteFunc5, color=YELLOW, x_range=[0, 2, 0.01])
        intePlota6 = inteAxes.plot(inteFunc6, color=YELLOW, x_range=[1, 3, 0.01])
        intePlota7 = inteAxes.plot(inteFunc7, color=YELLOW, x_range=[2, 4, 0.01])

        # Straight line graph but for our other axes
        squaPlot1 = inteAxesSquared.plot(inteFunc1, color=YELLOW, x_range=[-4, -2, 0.01])
        squaPlot2 = inteAxesSquared.plot(inteFunc2, color=YELLOW, x_range=[-3, -1, 0.01])
        squaPlot3 = inteAxesSquared.plot(inteFunc3, color=YELLOW, x_range=[-2, 0, 0.01])
        squaPlot4 = inteAxesSquared.plot(inteFunc4, color=YELLOW, x_range=[-1, 1, 0.01])
        squaPlot5 = inteAxesSquared.plot(inteFunc5, color=YELLOW, x_range=[0, 2, 0.01])
        squaPlot6 = inteAxesSquared.plot(inteFunc6, color=YELLOW, x_range=[1, 3, 0.01])
        squaPlot7 = inteAxesSquared.plot(inteFunc7, color=YELLOW, x_range=[2, 4, 0.01])
        #Ensure our pyramids on the outer sides remain on top of our (blue) sum line
        squaPlot1.z_index = 1
        squaPlot7.z_index = 1

        # basicSum for our new axes
        squaPlotStraightSum = inteAxesSquared.plot(basicSum, color=BLUE, x_range=[-4, 4, 0.01])

        #
        # Pyramids to align with x^2 
        #

        # 3 and 5 aren't necessary as they're equal to our previous 3 and 5 function (respectively)
        # But to make it easier to keep track of the pyramids, I'll be adding it in anyway
        squaPlotSquared = inteAxesSquared.plot(inteFuncSquared, color=RED, x_range=[-3.08, 3.08, 0.01])
        squaPlotSquared1 = inteAxesSquared.plot(inteFuncSquared1, color=YELLOW, x_range=[-4, -2, 0.01])
        squaPlotSquared2 = inteAxesSquared.plot(inteFuncSquared2, color=YELLOW, x_range=[-3, -1, 0.01])
        squaPlotSquared3 = inteAxesSquared.plot(inteFuncSquared3, color=YELLOW, x_range=[-2, 0, 0.01])
        squaPlotSquared4 = inteAxesSquared.plot(inteFuncSquared4, color=YELLOW, x_range=[-1, 1, 0.01])
        squaPlotSquared5 = inteAxesSquared.plot(inteFuncSquared5, color=YELLOW, x_range=[0, 2, 0.01])
        squaPlotSquared6 = inteAxesSquared.plot(inteFuncSquared6, color=YELLOW, x_range=[1, 3, 0.01])
        squaPlotSquared7 = inteAxesSquared.plot(inteFuncSquared7, color=YELLOW, x_range=[2, 4, 0.01])
        # Ensure our pyramids on the outer sides remain on top of our (blue) sum line
        squaPlotSquared1.z_index = 1
        squaPlotSquared7.z_index = 1
        # Since we don't *need* this one, we can hide it a bit behind the x-axis, but it'll remain barely visible
        squaPlotSquared4.z_index = -1

        # Basic Approx. of x^2
        squaPlotSquaredSum = inteAxesSquared.plot(squareSum, color=BLUE, x_range=[-4, 4, 0.01])

        #--- Start of code added by ChatGPT --- (I don't understand like any of it)

        # Create a VMobject for the filled area
        xSquaredArea_fill = VMobject()
        xSquaredArea_fill.set_fill(PURPLE, opacity=0.5)  # Adjust opacity

        # Get points from the plotted blue line within the range [-3,3]
        purple_points = squaPlotSquaredSum.get_points_defining_boundary()  # Extract curve points
        purple_points = [p for p in purple_points if -3 <= inteAxesSquared.p2c(p)[0] <= 3]  # Keep only x ∈ [-3,3]

        # Manually ensure the boundary points exist
        left_top = inteAxesSquared.c2p(-3, squareSum(-3))  # Top-left
        right_top = inteAxesSquared.c2p(3, squareSum(3))  # Top-right
        left_bottom = inteAxesSquared.c2p(-3, 0)  # Bottom-left
        right_bottom = inteAxesSquared.c2p(3, 0)  # Bottom-right

        # Generate x-axis points at y=0
        x_axis_points = [inteAxesSquared.c2p(inteAxesSquared.p2c(p)[0], 0) for p in purple_points]

        # Reverse order for proper polygon closure
        x_axis_points.reverse()

        # Construct the filled shape (ensuring it starts & ends at the boundaries)
        xSquaredArea_fill.set_points_as_corners([left_top, *purple_points, right_top, right_bottom, *x_axis_points, left_bottom])

        # --- End of code added by ChatGPT ---
        # The code provided by ChatGPT didn't give us a white line from (-3, 0) to (-3, 9) but it made one at (3, 0) to (3, 9) so I'm manually adding one:
        left_boundary_line = Line(inteAxesSquared.c2p(-3, 0), inteAxesSquared.c2p(-3, squareSum(-3)), color=WHITE)

        #----------
        # Polygons
        #----------

        # We want to split up the pyramids and combine them into rectangles
        # First, we'll separate our pyramids, splitting the outer pyramids in half to keep the inner half blue
        # Then we'll spread them out to show the 6 pyramids separately
        # Then we can split the rest of the pyramids in half, and join them in a rectangular shape
        # Find the area of each rectangle, dividing the outer sides by 2
        # Take the sum of them all
        # Compare it to the actual value of integration
        # Left-side half-triangle (outline only)
        tri1 = Polygon(
            inteAxesSquared.c2p(-4, 0), 
            inteAxesSquared.c2p(-3, 9), 
            inteAxesSquared.c2p(-3, 0),
            color=YELLOW
        )

        # Left-side half-triangle (filled blue)
        tri2 = Polygon(
            inteAxesSquared.c2p(-3, 0), 
            inteAxesSquared.c2p(-3, 9), 
            inteAxesSquared.c2p(-2, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Middle full triangles (filled blue)
        tri3 = Polygon(
            inteAxesSquared.c2p(-3, 0), 
            inteAxesSquared.c2p(-2, 4), 
            inteAxesSquared.c2p(-1, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        tri4 = Polygon(
            inteAxesSquared.c2p(-2, 0), 
            inteAxesSquared.c2p(-1, 1), 
            inteAxesSquared.c2p(0, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Flat triangle (no height → just a yellow line)
        tri5 = Line(
            inteAxesSquared.c2p(-1, 0), 
            inteAxesSquared.c2p(1, 0), 
            color=YELLOW
        )

        tri6 = Polygon(
            inteAxesSquared.c2p(0, 0), 
            inteAxesSquared.c2p(1, 1), 
            inteAxesSquared.c2p(2, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        tri7 = Polygon(
            inteAxesSquared.c2p(1, 0), 
            inteAxesSquared.c2p(2, 4), 
            inteAxesSquared.c2p(3, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Right-side half-triangle (filled blue)
        tri8 = Polygon(
            inteAxesSquared.c2p(2, 0), 
            inteAxesSquared.c2p(3, 9), 
            inteAxesSquared.c2p(3, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Right-side half-triangle (outline only)
        tri9 = Polygon(
            inteAxesSquared.c2p(3, 0), 
            inteAxesSquared.c2p(3, 9), 
            inteAxesSquared.c2p(4, 0),
            color=YELLOW
        )
        
        # Manually shift the previous triangles into new positions by creating a copy of them, shifting them into place, then transforming
        # I think I could probably just use like
        # self.play(animate the shift 1, animate the shift 2...) but idk 
        tri1_transformed = tri1.copy().scale(0.75).shift(LEFT*1.5, DOWN*0.63)
        tri2_transformed = tri2.copy().scale(0.75).next_to(tri1_transformed, RIGHT*0.25)
        tri3_transformed = tri3.copy().scale(0.75).shift(LEFT*0.8, DOWN*0.2225)
        tri4_transformed = tri4.copy().scale(0.75).shift(LEFT*0)
        tri5_transformed = tri5.copy().scale(0.75).shift(UP*2)
        tri6_transformed = tri6.copy().scale(0.75).shift(RIGHT*0)
        tri7_transformed = tri7.copy().scale(0.75).shift(RIGHT*0.8, DOWN*0.2225)
        # 9 first so we can align 8 to the left-side of this
        tri9_transformed = tri9.copy().scale(0.75).shift(RIGHT*1.5, DOWN*0.63)
        tri8_transformed = tri8.copy().scale(0.75).next_to(tri9_transformed, LEFT*0.25)

        # Flip half of the left-side pyramid first
        tri2_flip = tri2_transformed.copy().flip(axis=RIGHT).move_to(tri1_transformed).shift(UP*0.125, RIGHT*0.005)
        # Show the size of the rectangle we're creating using curly brackets. tri1 needs no label as it creates a rectangle with tri2
        tri2_bracket = Brace(tri1_transformed, direction=RIGHT)
        # Manually increase the height of the bracket to better fit the triangle since we've been sorta doing this a bit messy
        tri2_bracket.set_height(tri2_bracket.get_height() + 0.15)
        # Manually shift it up a little since we now are underneath the area we want to represent
        tri2_bracket.shift(UP*0.075)
        # Set the text
        tri2_label = tri2_bracket.get_text(r"f(-3)").scale(0.7)
        # Create the bracket on top for the width of the rectangle
        tri2_top_bracket = Brace(tri1_transformed, direction=UP)  # Create an upward bracket
        # Create the label for the top bracket (labeling it "1")
        tri2_top_label = tri2_top_bracket.get_text("1").scale(0.7)

        tri2_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri1_transformed, UP*2).shift(LEFT*0.25)
        tri2_area_value = MathTex(r"\frac{f(-3)}{2}").scale(0.7).next_to(tri2_area_label, RIGHT*0.25)
        
        # Now split the rest of the pyramids and do the same
        
        # First, we create the triangles on the same axis points that the original triangles were on, then shift them the same way we shifted our other triangles previously
        # Split tri3 into two smaller triangles
        tri3a = Polygon(
            inteAxesSquared.c2p(-3, 0),  # Left base
            inteAxesSquared.c2p(-2, 4),  # Peak
            inteAxesSquared.c2p(-2, 0),  # Midpoint on x-axis
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        tri3b = Polygon(
            inteAxesSquared.c2p(-2, 0),  # Midpoint on x-axis
            inteAxesSquared.c2p(-2, 4),  # Peak
            inteAxesSquared.c2p(-1, 0),  # Right base
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Split tri4
        tri4a = Polygon(
            inteAxesSquared.c2p(-2, 0),
            inteAxesSquared.c2p(-1, 1),  # Midpoint peak
            inteAxesSquared.c2p(-1, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        tri4b = Polygon(
            inteAxesSquared.c2p(-1, 0),
            inteAxesSquared.c2p(-1, 1),  # Midpoint peak
            inteAxesSquared.c2p(0, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # tri5 stays as a line, but reduce it to half the size
        tri5a = Line(
            inteAxesSquared.c2p(-1, 0), 
            inteAxesSquared.c2p(0, 0), 
            color=YELLOW
        )

        tri6a = Polygon(
            inteAxesSquared.c2p(0, 0),
            inteAxesSquared.c2p(1, 1),  # Midpoint peak
            inteAxesSquared.c2p(1, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        tri6b = Polygon(
            inteAxesSquared.c2p(1, 0),
            inteAxesSquared.c2p(1, 1),  # Midpoint peak
            inteAxesSquared.c2p(2, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Split tri7
        tri7a = Polygon(
            inteAxesSquared.c2p(1, 0),
            inteAxesSquared.c2p(2, 4),
            inteAxesSquared.c2p(2, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        tri7b = Polygon(
            inteAxesSquared.c2p(2, 0),
            inteAxesSquared.c2p(2, 4),
            inteAxesSquared.c2p(3, 0),
            color=YELLOW, fill_color=PURPLE, fill_opacity=0.5
        )

        # Now we shift them the same way we did before, changing them slightly to spread out a bit better
        # Apply transformations to match their respective original triangles
        tri3a_transformed = tri3a.copy().scale(0.75).shift(LEFT*0.8, DOWN*0.2225)
        tri3b_transformed = tri3b.copy().scale(0.75).shift(LEFT, DOWN*0.2225)

        tri4a_transformed = tri4a.copy().scale(0.75).shift(RIGHT*0.1)
        tri4b_transformed = tri4b.copy().scale(0.75).shift(LEFT*0.1)

        # We don't *need* this, but I'll end up Fading this one in instead of the other so we can keep it all organized in the animation coding
        tri5a_transformed = tri5a.copy().scale(0.75).shift(UP*3) 

        tri6a_transformed = tri6a.copy().scale(0.75).shift(LEFT*0.1)
        tri6b_transformed = tri6b.copy().scale(0.75).shift(LEFT*0.4)

        tri7a_transformed = tri7a.copy().scale(0.75).shift(RIGHT*0.8, DOWN*0.2225)
        tri7b_transformed = tri7b.copy().scale(0.75).shift(RIGHT*0.6, DOWN*0.2225)

        # Now flip them all the same way we did before, adjusting the values slightly
        tri3b_flip = tri3b_transformed.copy().flip(axis=RIGHT).move_to(tri3a_transformed).shift(UP*0.08)
        tri4b_flip = tri4b_transformed.copy().flip(axis=RIGHT).move_to(tri4a_transformed).shift(LEFT*0.05)
        tri6b_flip = tri6b_transformed.copy().flip(axis=RIGHT).move_to(tri6a_transformed).shift(LEFT*0.05)
        tri7b_flip = tri7b_transformed.copy().flip(axis=RIGHT).move_to(tri7a_transformed).shift(UP*0.08)
        # Flip the last one too
        tri9_flip = tri9_transformed.copy().flip(axis=RIGHT).move_to(tri8_transformed).shift(UP*0.125)


        # Add all the curly brackets and labels

        tri3_bracket = Brace(tri3a_transformed, direction=RIGHT)
        tri3_label = tri3_bracket.get_text(r"f(-2)").scale(0.7).shift(LEFT*0.35)
        tri3_top_bracket = Brace(tri3a_transformed, direction=UP)
        tri3_top_label = tri3_top_bracket.get_text("1").scale(0.7)

        tri4_bracket = Brace(tri4a_transformed, direction=RIGHT)
        tri4_label = tri4_bracket.get_text(r"f(-1)").scale(0.7).shift(LEFT*0.35)
        tri4_top_bracket = Brace(tri4a_transformed, direction=UP)
        tri4_top_label = tri4_top_bracket.get_text("1").scale(0.7)

        #introduce 5 as we fade it in, showing that we don't need to add anything for this
        tri5_bracket = Brace(tri5a_transformed, direction=RIGHT)
        tri5_label = tri5_bracket.get_text(r"f(0)").scale(0.7).shift(LEFT*0.35)
        tri5_top_bracket = Brace(tri5a_transformed, direction=UP)
        tri5_top_label = tri5_top_bracket.get_text("1").scale(0.7)

        tri6_bracket = Brace(tri6a_transformed, direction=RIGHT)
        tri6_label = tri6_bracket.get_text(r"f(1)").scale(0.7).shift(LEFT*0.35)
        tri6_top_bracket = Brace(tri6a_transformed, direction=UP)
        tri6_top_label = tri6_top_bracket.get_text("1").scale(0.7)

        tri7_bracket = Brace(tri7a_transformed, direction=RIGHT)
        tri7_label = tri7_bracket.get_text(r"f(2)").scale(0.7).shift(LEFT*0.35)
        tri7_top_bracket = Brace(tri7a_transformed, direction=UP)
        tri7_top_label = tri7_top_bracket.get_text("1").scale(0.7)
        # Last set
        tri8_bracket = Brace(tri8_transformed, direction=RIGHT)
        tri8_label = tri8_bracket.get_text(r"f(3)").scale(0.7).shift(LEFT*0.35)
        tri8_top_bracket = Brace(tri8_transformed, direction=UP)
        tri8_top_label = tri8_top_bracket.get_text("1").scale(0.7)

        # Finally, convert them all to the areas

        tri3_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri3a_transformed, UP).shift(LEFT*0.25)
        tri3_area_value = MathTex(r"f(-2)").scale(0.7).next_to(tri3_area_label, RIGHT*0.25)

        tri4_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri4a_transformed, UP).shift(LEFT*0.25)
        tri4_area_value = MathTex(r"f(-1)").scale(0.7).next_to(tri4_area_label, RIGHT*0.25)
        
        tri5_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri5a_transformed, UP).shift(LEFT*0.25)
        tri5_area_value = MathTex(r"f(0)").scale(0.7).next_to(tri5_area_label, RIGHT*0.25)

        tri6_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri6a_transformed, UP).shift(LEFT*0.25)
        tri6_area_value = MathTex(r"f(1)").scale(0.7).next_to(tri6_area_label, RIGHT*0.25)

        tri7_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri7a_transformed, UP).shift(LEFT*0.25)
        tri7_area_value = MathTex(r"f(2)").scale(0.7).next_to(tri7_area_label, RIGHT*0.25)

        tri8_area_label = MathTex(r"\textcolor[HTML]{9A72AC}{A}=").scale(0.7).next_to(tri8_transformed, UP*2).shift(LEFT*0.25)
        tri8_area_value = MathTex(r"\frac{f(3)}{2}").scale(0.7).next_to(tri8_area_label, RIGHT*0.25)

        #---------- 
        # Formulas
        #----------

        # Formula 1 (vroom vroom)
        inteForm1 = MathTex(r"\frac{|x+1|+|x-1|-2|x|}{2}").shift(UP*3)
        inteForm1a = MathTex(f"f(x) = ").next_to(inteForm1, LEFT)

        # Formula 2 -> Multiple pyramids
        # 2a isn't necessary but adding it lets us keep track of the individual elements easier
        inteForm2 = MathTex(r"\frac{|(x-n)+1|+|(x-n)-1|-2|(x-n)|}{2}").shift(UP*3, LEFT).scale(0.825)
        inteForm2a = MathTex(r"f(x) = ").scale(0.825).next_to(inteForm2, LEFT)
        inteForm2b = MathTex(r"n \in \mathbb{Z}, -3 \leq n \leq 3").scale(0.825).next_to(inteForm2, RIGHT)

        # Formula 3 -> Sum of pyramids
        inteForm3 = MathTex(r"\frac{|(x-n)+1| + |(x-n)-1| - 2|(x-n)|}{2}").shift(UP*3).scale(0.9)
        inteForm3a = MathTex(r"\textcolor[HTML]{58C4DD}{\sum_{n=-3}^{3}}").next_to(inteForm3, LEFT).scale(0.9)

        # Formula 4 -> Simultaneously showing 2 and 3 in a single form
        inteForm4 = MathTex(r"\frac{|(x-n)+1|+|(x-n)-1|-2|(x-n)|}{2}").shift(UP*3, RIGHT*2.875).scale(0.8)
        inteForm4a = MathTex(r"\left( \textcolor{yellow}{f(n) = 1, -3 \leq n \leq 3} \quad \& \textcolor[HTML]{58C4DD}{\sum_{n=-3}^{3}} \right) ").scale(0.8).next_to(inteForm4, LEFT)

        # Formula 5 -> Same as Formula 4 but f(x) = x^2 instead of f(x) = 1
        # Set x^2 in "f(n) = x^2" to red, since we introduce a red line representing x^2
        inteForm5 = MathTex(r"\left( f(n) * \frac{|(x-n)+1|+|(x-n)-1|-2|(x-n)|}{2} \right)").shift(UP*3, RIGHT*2.8).scale(0.7)
        inteForm5a = MathTex(r"\left( \textcolor{yellow}{f(n) = \textcolor[HTML]{FC6255}{x^2}, -3 \leq n \leq 3} \quad \& \textcolor[HTML]{58C4DD}{\sum_{n=-3}^{3}} \right) ").scale(0.7).next_to(inteForm5, LEFT)

        inteForm6 = MathTex(r"\left( f(n) * \frac{|(x-n)+1|+|(x-n)-1|-2|(x-n)|}{2} \right)").shift(UP*3, RIGHT*0.5).scale(0.8)
        inteForm6a = MathTex(r"\textcolor[HTML]{58C4DD}{\sum_{n=-3}^{3}}").scale(0.8).next_to(inteForm6, LEFT)
        
        # Just use inteForm6a
        inteForm7 = MathTex(r"\textcolor[HTML]{9A72AC}{\int_{-3}^{3}}").scale(0.8).next_to(inteForm6a, LEFT)
        inteForm7a = MathTex(r"\textcolor[HTML]{9A72AC}{\, dx}").scale(0.8).next_to(inteForm6, RIGHT)
        
        # Now we're going to take all the values of our areas and combine them into a single summation.
        # I could probably set this all up easier but idk
        area_formula = tri2_area_label.copy().scale(1.42).shift(RIGHT*0.5)
        tri2_area_formula = tri2_area_value.copy().scale(1.2).next_to(area_formula, RIGHT)
        plusOne = MathTex(r"+").scale(0.75).next_to(tri2_area_formula, RIGHT)
        tri3_area_formula = tri3_area_value.copy().scale(1.2).next_to(plusOne, RIGHT)
        plusTwo = MathTex(r"+").scale(0.75).next_to(tri3_area_formula, RIGHT)
        tri4_area_formula = tri4_area_value.copy().scale(1.2).next_to(plusTwo, RIGHT)
        plusThree = MathTex(r"+").scale(0.75).next_to(tri4_area_formula, RIGHT)
        tri5_area_formula = tri5_area_value.copy().scale(1.2).next_to(plusThree, RIGHT)
        plusFour = MathTex(r"+").scale(0.75).next_to(tri5_area_formula, RIGHT)
        tri6_area_formula = tri6_area_value.copy().scale(1.2).next_to(plusFour, RIGHT)
        plusFive = MathTex(r"+").scale(0.75).next_to(tri6_area_formula, RIGHT)
        tri7_area_formula = tri7_area_value.copy().scale(1.2).next_to(plusFive, RIGHT)
        plusSix = MathTex(r"+").scale(0.75).next_to(tri7_area_formula, RIGHT)
        tri8_area_formula = tri8_area_value.copy().scale(1.2).next_to(plusSix, RIGHT)

        
        # Now we want to change our formulas into their actual values of the function x^2
        area_value_x2a = MathTex(r"\frac{9}{2}").move_to(tri2_area_formula).shift(DOWN*2)
        area_value_x3a = MathTex(r"4").move_to(tri3_area_formula).shift(DOWN*2)
        area_value_x4a = MathTex(r"1").move_to(tri4_area_formula).shift(DOWN*2)
        area_value_x5a = MathTex(r"0").move_to(tri5_area_formula).shift(DOWN*2)
        area_value_x6a = MathTex(r"1").move_to(tri6_area_formula).shift(DOWN*2)
        area_value_x7a = MathTex(r"4").move_to(tri7_area_formula).shift(DOWN*2)
        area_value_x8a = MathTex(r"\frac{9}{2}").move_to(tri8_area_formula).shift(DOWN*2)
        area_value_sum = MathTex(r"19").move_to(tri2_area_formula).shift(DOWN*2)


        #-------------------
        # Animate the scene
        #-------------------

        # Create axes
        self.play(Create(inteAxes))

        # Add central pyramid and write equation
        self.play(
            Create(intePlot4),
            Write(inteForm1),
            Write(inteForm1a)
        )      
        self.wait(1.5)

        # Now create the rest of the pyramids and update the equation
        self.play(
            Create(intePlot1),
            Create(intePlot2),
            Create(intePlot3),
            Create(intePlot5),
            Create(intePlot6),
            Create(intePlot7),
            ReplacementTransform(inteForm1, inteForm2),
            ReplacementTransform(inteForm1a, inteForm2a),
            Write(inteForm2b)
        )
        self.wait(1.5)

        # Change our function from singular pyramids to the segmented straight line
        self.play(
            ReplacementTransform(intePlot1, intePlotStraight1),
            ReplacementTransform(intePlot2, intePlotStraight2),
            ReplacementTransform(intePlot3, intePlotStraight3),
            ReplacementTransform(intePlot4, intePlotStraight4),
            ReplacementTransform(intePlot5, intePlotStraight5),
            ReplacementTransform(intePlot6, intePlotStraight6),
            ReplacementTransform(intePlot7, intePlotStraight7),
            ReplacementTransform(inteForm2, inteForm3),
            ReplacementTransform(inteForm2a, inteForm3a),
            FadeOut(inteForm2b)
        )
        self.wait(1.5)

        # Reintroduce a copy of the singular pyramids for visualizing them while we transform the graph
        # Hide the creation of the straight line of basicSum in this animation
        self.play(
            Create(intePlota1),
            Create(intePlota2),
            Create(intePlota3),
            Create(intePlota4),
            Create(intePlota5),
            Create(intePlota6),
            Create(intePlota7),
            Create(intePlotStraightSum),
            ReplacementTransform(inteForm3, inteForm4),
            ReplacementTransform(inteForm3a, inteForm4a)
        )
        self.wait(0.5)
        # Hide the segmented blue line 
        self.play(
            intePlotStraight1.animate.set_opacity(0),
            intePlotStraight2.animate.set_opacity(0),
            intePlotStraight3.animate.set_opacity(0),
            intePlotStraight4.animate.set_opacity(0),
            intePlotStraight5.animate.set_opacity(0),
            intePlotStraight6.animate.set_opacity(0),
            intePlotStraight7.animate.set_opacity(0),
        )
        self.wait(0.5)

        self.play(
            ReplacementTransform(inteAxes, inteAxesSquared),
            ReplacementTransform(intePlota1, squaPlot1),
            ReplacementTransform(intePlota2, squaPlot2),
            ReplacementTransform(intePlota3, squaPlot3),
            ReplacementTransform(intePlota4, squaPlot4),
            ReplacementTransform(intePlota5, squaPlot5),
            ReplacementTransform(intePlota6, squaPlot6),
            ReplacementTransform(intePlota7, squaPlot7),
            ReplacementTransform(intePlotStraightSum, squaPlotStraightSum),
            FadeIn(y_ticks, y_labels)
        )
        self.wait(1.5)

        self.play(
            Create(squaPlotSquared),
            ReplacementTransform(squaPlotStraightSum, squaPlotSquaredSum),
            ReplacementTransform(squaPlot1, squaPlotSquared1),
            ReplacementTransform(squaPlot2, squaPlotSquared2),
            ReplacementTransform(squaPlot3, squaPlotSquared3),
            ReplacementTransform(squaPlot4, squaPlotSquared4),
            ReplacementTransform(squaPlot5, squaPlotSquared5),
            ReplacementTransform(squaPlot6, squaPlotSquared6),
            ReplacementTransform(squaPlot7, squaPlotSquared7),
            ReplacementTransform(inteForm4, inteForm5),
            ReplacementTransform(inteForm4a, inteForm5a)
        )
        self.wait(1.5)
        self.play(
            FadeOut(squaPlotSquared1, squaPlotSquared2, squaPlotSquared3, squaPlotSquared4, squaPlotSquared5, squaPlotSquared6, squaPlotSquared7),
            ReplacementTransform(inteForm5, inteForm6),
            ReplacementTransform(inteForm5a, inteForm6a)      
        )
        self.wait(1.5)
        self.play(FadeIn(xSquaredArea_fill, left_boundary_line, inteForm7, inteForm7a))
        self.wait(1.5)
        self.play(
            FadeIn(tri1, tri2, tri3, tri4, tri5, tri6, tri7, tri8, tri9),
            FadeOut(xSquaredArea_fill, left_boundary_line)
        )
        self.wait(1.5)
        self.play(
            FadeOut(squaPlotSquaredSum, squaPlotSquared, inteAxesSquared, y_ticks, y_labels),
            ReplacementTransform(tri1, tri1_transformed),
            ReplacementTransform(tri2, tri2_transformed),
            ReplacementTransform(tri3, tri3_transformed),
            ReplacementTransform(tri4, tri4_transformed),
            ReplacementTransform(tri5, tri5_transformed),
            ReplacementTransform(tri6, tri6_transformed),
            ReplacementTransform(tri7, tri7_transformed),
            ReplacementTransform(tri8, tri8_transformed),
            ReplacementTransform(tri9, tri9_transformed)
        )
        self.wait(1.5)

        self.play(FadeOut(tri5_transformed))
        self.wait(1.5)
        
        self.play(ReplacementTransform(tri2_transformed, tri2_flip),
            Create(tri2_bracket),
            Create(tri2_label),
            Create(tri2_top_bracket),
            Create(tri2_top_label)
        )
        self.wait(1.5)
        self.play(
            FadeOut(tri2_bracket, tri2_top_bracket, tri2_top_label),
            FadeIn(tri2_area_label),
            ReplacementTransform(tri2_label, tri2_area_value)
        )
        self.wait(1.5)
        self.play(
            AnimationGroup(
                FadeIn(tri3a_transformed, tri3b_transformed, tri4a_transformed, tri4b_transformed, tri6a_transformed, tri6b_transformed, tri7a_transformed, tri7b_transformed),
                FadeOut(tri3_transformed, tri4_transformed, tri6_transformed, tri7_transformed)
            )
        )
        self.wait(1.5)
        self.play(
            ReplacementTransform(tri3b_transformed, tri3b_flip),
            ReplacementTransform(tri4b_transformed, tri4b_flip),
            ReplacementTransform(tri6b_transformed, tri6b_flip),
            ReplacementTransform(tri7b_transformed, tri7b_flip),
            ReplacementTransform(tri9_transformed, tri9_flip)
        )
        self.wait(1.5)
        self.play(
            FadeIn(tri3_bracket, tri3_label, tri3_top_bracket, tri3_top_label, tri4_bracket, tri4_label, tri4_top_bracket, tri4_top_label, tri5_bracket, tri5_label, tri5_top_bracket, tri5_top_label, tri6_bracket, tri6_label, tri6_top_bracket, tri6_top_label, tri7_bracket, tri7_label, tri7_top_bracket, tri7_top_label, tri8_bracket, tri8_label, tri8_top_bracket, tri8_top_label, tri5a_transformed),
        )
        self.wait(1.5)
        self.play(
            FadeOut(tri3_bracket, tri3_top_bracket, tri3_top_label, 
                    tri4_bracket, tri4_top_bracket, tri4_top_label, 
                    tri5_bracket, tri5_top_bracket, tri5_top_label, 
                    tri6_bracket, tri6_top_bracket, tri6_top_label, 
                    tri7_bracket, tri7_top_bracket, tri7_top_label, 
                    tri8_bracket, tri8_top_bracket, tri8_top_label),
            FadeIn(tri3_area_label, tri4_area_label, tri5_area_label, tri6_area_label, tri7_area_label, tri8_area_label),
            ReplacementTransform(tri3_label, tri3_area_value),
            ReplacementTransform(tri4_label, tri4_area_value),
            ReplacementTransform(tri5_label, tri5_area_value),
            ReplacementTransform(tri6_label, tri6_area_value),
            ReplacementTransform(tri7_label, tri7_area_value),
            ReplacementTransform(tri8_label, tri8_area_value),
        )
        self.wait(1.5)

        self.play(
            ReplacementTransform(tri2_area_label, area_formula),
            ReplacementTransform(tri2_area_value, tri2_area_formula),
            ReplacementTransform(tri3_area_value, tri3_area_formula),
            ReplacementTransform(tri4_area_value, tri4_area_formula),
            ReplacementTransform(tri5_area_value, tri5_area_formula),
            ReplacementTransform(tri6_area_value, tri6_area_formula),
            ReplacementTransform(tri7_area_value, tri7_area_formula),
            ReplacementTransform(tri8_area_value, tri8_area_formula),
            FadeIn(plusOne, plusTwo, plusThree, plusFour, plusFive, plusSix),
            FadeOut(
                tri1_transformed, tri2_flip, 
                tri3a_transformed, tri3b_flip, tri3_area_label,
                tri4a_transformed, tri4b_flip, tri4_area_label,
                tri5a_transformed, tri5_area_label,
                tri6a_transformed, tri6b_flip, tri6_area_label,
                tri7a_transformed, tri7b_flip, tri7_area_label,
                tri8_transformed, tri9_flip, tri8_area_label,
            )
        )
        self.wait(1.5)

        #Just create some copies here
        plus1 = plusOne.copy().shift(DOWN*2)
        plus2 = plusTwo.copy().shift(DOWN*2)
        plus3 = plusThree.copy().shift(DOWN*2)
        plus4 = plusFour.copy().shift(DOWN*2)
        plus5 = plusFive.copy().shift(DOWN*2)
        plus6 = plusSix.copy().shift(DOWN*2)
        equalsOne = MathTex(r"=").scale(0.75).next_to(tri2_area_formula, LEFT).shift(DOWN*2)
        
        self.play(
            AnimationGroup(
                ReplacementTransform(tri2_area_formula.copy(), area_value_x2a),
                ReplacementTransform(plusOne.copy(), plus1),
                ReplacementTransform(tri3_area_formula.copy(), area_value_x3a),
                ReplacementTransform(plusTwo.copy(), plus2),
                ReplacementTransform(tri4_area_formula.copy(), area_value_x4a),
                ReplacementTransform(plusThree.copy(), plus3),
                ReplacementTransform(tri5_area_formula.copy(), area_value_x5a),
                ReplacementTransform(plusFour.copy(), plus4),
                ReplacementTransform(tri6_area_formula.copy(), area_value_x6a),
                ReplacementTransform(plusFive.copy(), plus5),
                ReplacementTransform(tri7_area_formula.copy(), area_value_x7a),
                ReplacementTransform(plusSix.copy(), plus6),
                ReplacementTransform(tri8_area_formula.copy(), area_value_x8a),
                FadeIn(equalsOne),
                lag_ratio=0
            )
        )
        self.wait(1.5)
        self.play(
            AnimationGroup(
                ReplacementTransform(area_value_x2a, area_value_sum),
                plus1.animate.move_to(area_value_x2a).set_opacity(0),
                area_value_x3a.animate.move_to(area_value_x2a).set_opacity(0),
                plus2.animate.move_to(area_value_x2a).set_opacity(0),
                area_value_x4a.animate.move_to(area_value_x2a).set_opacity(0),
                plus3.animate.move_to(area_value_x2a).set_opacity(0),
                area_value_x5a.animate.move_to(area_value_x2a).set_opacity(0),
                plus4.animate.move_to(area_value_x2a).set_opacity(0),
                area_value_x6a.animate.move_to(area_value_x2a).set_opacity(0),
                plus5.animate.move_to(area_value_x2a).set_opacity(0),
                area_value_x7a.animate.move_to(area_value_x2a).set_opacity(0),
                plus6.animate.move_to(area_value_x2a).set_opacity(0),
                area_value_x8a.animate.move_to(area_value_x2a).set_opacity(0),
            )
        )
        self.wait(1.5)

        equalsTwo = MathTex(r"=").next_to(tri8_area_formula, RIGHT)
        formula_value_sum = area_value_sum.copy().next_to(equalsTwo, RIGHT)
        self.play(
            AnimationGroup(
                ReplacementTransform(area_value_sum.copy(), formula_value_sum),
                ReplacementTransform(equalsOne.copy(), equalsTwo),
                inteForm6.animate.shift(LEFT*0.8),
                inteForm6a.animate.shift(LEFT*0.8),
                inteForm7.animate.shift(LEFT*0.8),
                inteForm7a.animate.shift(LEFT*0.8),
                equalsOne.animate.move_to(inteForm7a),
                area_value_sum.animate.next_to(inteForm7a, RIGHT*1.25),
                FadeOut(area_formula)
            )
        )
        self.wait(1.5)

        # Okay now combine the f(n) values into a formula
        approx_formula = MathTex(r"\textcolor[HTML]{9A72AC}{\sum_{n=-2}^{2}(}\textcolor[HTML]{FC6255}{f(n)}\textcolor[HTML]{9A72AC}{)} + \frac{\textcolor[HTML]{FC6255}{f(-3)}+\textcolor[HTML]{FC6255}{f(3)}}{\textcolor[HTML]{9A72AC}{2}}}").move_to(tri2_area_formula).shift(RIGHT*4.5)
        equalsThree = MathTex(r"=").next_to(approx_formula, RIGHT)
        approx_formula_value = formula_value_sum.copy().next_to(equalsThree, RIGHT)

        self.play(
            AnimationGroup(
                ReplacementTransform(tri2_area_formula, approx_formula),
                ReplacementTransform(equalsTwo, equalsThree),
                ReplacementTransform(formula_value_sum, approx_formula_value),
                plusOne.animate.move_to(tri5_area_formula).set_opacity(0),
                tri3_area_formula.animate.move_to(tri5_area_formula).set_opacity(0),
                plusTwo.animate.move_to(tri5_area_formula).set_opacity(0),
                tri4_area_formula.animate.move_to(tri5_area_formula).set_opacity(0),
                plusThree.animate.move_to(tri5_area_formula).set_opacity(0),
                tri5_area_formula.animate.move_to(tri5_area_formula).set_opacity(0),
                plusFour.animate.move_to(tri5_area_formula).set_opacity(0),
                tri6_area_formula.animate.move_to(tri5_area_formula).set_opacity(0),
                plusFive.animate.move_to(tri5_area_formula).set_opacity(0),
                tri7_area_formula.animate.move_to(tri5_area_formula).set_opacity(0),
                plusSix.animate.move_to(tri5_area_formula).set_opacity(0),
                tri8_area_formula.animate.move_to(tri5_area_formula).set_opacity(0),
                lag_ratio=0
            )
        )
        self.wait(1.5)
        # Create a few more things here.
        inteFormulaApprox = MathTex(r"\approx").next_to(approx_formula, LEFT)
        inteFormula_dx = MathTex(r"\textcolor[HTML]{F7A1A3}{\, dx}").next_to(inteFormulaApprox,LEFT)
        inteFormulaFunc = MathTex(r"\textcolor[HTML]{FC6255}{f(n)}").next_to(inteFormula_dx, LEFT)
        inteFormulaInt = MathTex(r"\textcolor[HTML]{F7A1A3}{\int_{-3}^{3}}").next_to(inteFormulaFunc, LEFT)
        self.play(
            FadeIn(inteFormulaApprox, inteFormulaFunc, inteFormulaInt, inteFormula_dx),
            FadeOut(inteForm6, inteForm6a, inteForm7, inteForm7a, equalsOne, area_value_sum)
        )
        self.wait(1.5)
        self.play(
            AnimationGroup(
                inteFormulaApprox.animate.shift(UP*1.75, RIGHT*0.5),
                inteFormulaFunc.animate.shift(UP*1.75, RIGHT*0.5),
                inteFormulaInt.animate.shift(UP*1.75, RIGHT*0.5),
                inteFormula_dx.animate.shift(UP*1.75, RIGHT*0.5),
                approx_formula.animate.shift(UP*1.75, RIGHT*0.5),
                approx_formula_value.animate.shift(UP*1.75, RIGHT*0.5),
                equalsThree.animate.shift(UP*1.75, RIGHT*0.5),
                FadeIn(inteAxesSquared, y_labels, y_ticks, squaPlotSquared)
            )
        )
        self.wait(1.5)
        area_underxSquared = inteAxesSquared.get_area(squaPlotSquared, x_range=[-3, 3], color=RED_A, opacity=0.5)
        self.play(
            FadeIn(area_underxSquared)
        )
        integrationValue = MathTex(r"18").next_to(inteFormulaApprox, LEFT).shift(RIGHT)
        equalsFour = MathTex(r"=").next_to(integrationValue, LEFT)
        self.wait(1.5)
        self.play(
            AnimationGroup(
                ReplacementTransform(area_underxSquared, integrationValue),
                inteFormulaFunc.animate.shift(LEFT*0.4),
                inteFormulaInt.animate.shift(LEFT*0.4),
                inteFormula_dx.animate.shift(LEFT*0.4),
                approx_formula.animate.shift(RIGHT),
                inteFormulaApprox.animate.shift(RIGHT),
                equalsThree.animate.shift(RIGHT),
                approx_formula_value.animate.shift(RIGHT),
                FadeIn(equalsFour)
            )
        )
        self.play(
            FadeIn(xSquaredArea_fill)
        )
        self.wait(1.5)
        self.play(
            ReplacementTransform(xSquaredArea_fill, approx_formula)
        )
        self.wait(1.5)
        self.play(
            FadeOut(y_labels, y_ticks, inteAxesSquared, squaPlotSquared)
        )

        self.wait(1.5)
        general_int = MathTex(r"\textcolor[HTML]{F7A1A3}{\int_{a}^{b}}").scale(1.2).move_to(inteFormulaInt).shift(DOWN*2.6, RIGHT)
        # General Funk
        general_func = MathTex(r"\textcolor[HTML]{FC6255}{f(n)}").scale(1.2).next_to(general_int, RIGHT)
        general_dx = inteFormula_dx.copy().scale(1.2).next_to(general_func, RIGHT)
        general_approx = inteFormulaApprox.copy().scale(1.2).next_to(general_dx, RIGHT)
        general_formula = MathTex(r"\textcolor[HTML]{9A72AC}{\sum_{n=a+1}^{b-1}(}\textcolor[HTML]{FC6255}{f(n)}\textcolor[HTML]{9A72AC}{)} + \frac{\textcolor[HTML]{FC6255}{f(a)}+\textcolor[HTML]{FC6255}{f(b)}}{\textcolor[HTML]{9A72AC}{2}}}").scale(1.2).next_to(general_approx, RIGHT)
        self.play(
            ReplacementTransform(inteFormulaInt.copy(), general_int),
            ReplacementTransform(inteFormulaFunc.copy(), general_func),
            ReplacementTransform(inteFormula_dx.copy(), general_dx),
            ReplacementTransform(inteFormulaApprox.copy(), general_approx),
            ReplacementTransform(approx_formula.copy(), general_formula),
        )
        self.wait(3)