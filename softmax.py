from manim import *


class SoftmaxScene(Scene):
    def construct(self):
        # Title
        title = Text("Softmax Function").scale(1.5).to_edge(UP)
        self.play(Write(title))

        # Classification problem
        classification_problem = Text("Classification Problem").scale(1.2).to_edge(LEFT)
        self.play(Write(classification_problem))

        # Neural network diagram
        neural_network = self.get_neural_network_diagram().to_edge(RIGHT)
        self.play(FadeIn(neural_network))

        # Explanation of raw scores
        raw_scores = Text("Raw Scores (Logits)").next_to(neural_network, DOWN).scale(0.8)
        self.play(Write(raw_scores))

        # Softmax function
        softmax_text = Text("Softmax Function").next_to(classification_problem, DOWN)
        self.play(Write(softmax_text))

        # Softmax formula
        softmax_formula = MathTex("p_i = \\frac{e^{z_i}}{\\sum_{j} e^{z_j}}").next_to(softmax_text, DOWN).scale(0.8)
        self.play(Write(softmax_formula))

        # Explanation of softmax
        softmax_explanation = Text("Converts logits into probabilities").next_to(softmax_formula, DOWN).scale(0.8)
        self.play(Write(softmax_explanation))

        # Explanation of need for softmax
        need_softmax = Text("Raw scores may not be interpretable as probabilities").next_to(softmax_explanation, DOWN).scale(0.8)
        self.play(Write(need_softmax))

        # Conclusion
        conclusion = Text("Softmax is crucial for interpreting classification model outputs").to_edge(DOWN)
        self.play(Write(conclusion))

        self.wait()

    def get_neural_network_diagram(self):
        input_layer = Rectangle(width=2, height=1.5, color=BLUE)
        hidden_layer = Rectangle(width=2, height=1.5, color=BLUE).shift(DOWN * 1.5)
        output_layer = Rectangle(width=2, height=1.5, color=BLUE).shift(DOWN * 3)

        arrow1 = Arrow(input_layer.get_bottom(), hidden_layer.get_top(), color=WHITE)
        arrow2 = Arrow(hidden_layer.get_bottom(), output_layer.get_top(), color=WHITE)

        neural_network = VGroup(input_layer, hidden_layer, output_layer, arrow1, arrow2)

        return neural_network


# Example usage
softmax_scene = SoftmaxScene()
softmax_scene.render()
