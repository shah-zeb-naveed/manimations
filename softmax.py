from manim import *


class SineWaveGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3 * np.pi, 3 * np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        )

        # Create the axes
        self.add(axes)

        # Animate the sine wave
        sine_graph = self.get_sine_wave_graph(axes)
        self.play(Write(sine_graph), run_time=3)

        self.wait(3)

    def get_sine_wave_graph(self, axes):
        return FunctionGraph(lambda x: np.sin(x), x_range=[-3 * np.pi, 3 * np.pi], color=WHITE)


# Example usage
sine_wave_scene = SineWaveGraph()
sine_wave_scene.render()
