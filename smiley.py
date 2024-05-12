from manim import *

class SmileyFace(Scene):
    def construct(self):
        # Create smiley face
        face = Circle(color=BLUE, radius=1)
        left_eye = Circle(color=WHITE, radius=0.1).move_to(0.5*UP + 0.5*LEFT)
        right_eye = Circle(color=WHITE, radius=0.1).move_to(0.5*UP + 0.5*RIGHT)
        nose = Polygon(ORIGIN, 0.2*LEFT, 0.2*RIGHT, color=WHITE).next_to(face, DOWN, buff=SMALL_BUFF)
        mouth = Arc(radius=0.6, start_angle=PI/6, angle=-PI/3, color=WHITE).next_to(nose, DOWN, buff=0.05)

        smiley_face = VGroup(face, left_eye, right_eye, nose, mouth)

        # Create data points
        data_points = VGroup(*[Dot(point, color=RED) for point in self.generate_data()])
        
        # Add smiley face and data points to scene
        self.play(Create(smiley_face))
        self.wait(1)
        self.play(Create(data_points))
        self.wait(1)

        # Fit curve
        fitted_curve = self.fit_curve(data_points)

        # Animation of the fitted curve
        self.play(Create(fitted_curve))
        self.wait()

    def generate_data(self):
        # Generate random data points
        np.random.seed(0)
        x = np.linspace(0, 4, 10)
        y = 0.5 * x**2 + np.random.normal(size=x.shape)
        return [(x_val, y_val, 0) for x_val, y_val in zip(x, y)]

    def fit_curve(self, data_points):
        # Fit a curve to the data points
        x, y, _ = zip(*[point.get_center() for point in data_points])
        coefficients = np.polyfit(x, y, 2)  # Quadratic fit
        x_fit = np.linspace(0, 4, 100)
        y_fit = np.polyval(coefficients, x_fit)
        fitted_curve = VMobject()
        fitted_curve.set_points_smoothly([*zip(x_fit, y_fit, [0]*len(x_fit))])
        return fitted_curve
