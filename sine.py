from manim import *
import numpy as np

class CurveFittingAnimation(Scene):
    def construct(self):
        # Set up the scene
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False},
            tips=False,
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.add(axes, labels)

        # Generate the data points
        x_values = np.linspace(-4, 4, 30)
        y_true = np.sin(x_values) + 0.2 * np.random.randn(len(x_values))
        data_points = [Dot(axes.coords_to_point(x, y), radius=0.05) for x, y in zip(x_values, y_true)]
        self.play(AnimationGroup(*[Create(dot) for dot in data_points], lag_ratio=0.1))

        # Visualize the initial straight line
        line = always_redraw(lambda: axes.plot(
            lambda x: np.polyval(np.polyfit(x_values, y_true, 1), x),
            x_range=[-4, 4],
            stroke_width=3,
        ))
        self.play(Create(line))
        self.wait()

        # Animate the curve fitting process
        curve = always_redraw(lambda: axes.plot(
            lambda x: np.polyval(np.polyfit(x_values, y_true, 6), x),
            x_range=[-4, 4],
            stroke_width=3,
        ))
        self.play(ReplacementTransform(line, curve), run_time=5)
        self.wait()

        # Add explanatory text and annotations
        text = Text("Curve fitting with a polynomial function")
        self.play(Write(text))
        self.wait()

        arrow = Arrow(start=axes.coords_to_point(-3, 1), end=axes.coords_to_point(-1, -1), buff=0)
        self.play(Create(arrow))
        self.wait()

        circle = Circle(radius=0.5, color=YELLOW).move_to(axes.coords_to_point(2, -1))
        self.play(Create(circle))
        self.wait()

        self.play(FadeOut(text), FadeOut(arrow), FadeOut(circle))

# Run the animation
scene = CurveFittingAnimation()
scene.render()