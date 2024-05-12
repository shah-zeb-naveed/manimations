from manim import *

class MatrixScene(Scene):
    def construct(self):
        # Create the feature matrix
        feature_matrix = IntegerMatrix([[1 for _ in range(5)] for _ in range(5)], bracket_h_buff=SMALL_BUFF)
        feature_matrix.scale(0.7)
        self.play(Write(feature_matrix))

        # Create the label matrix
        label_matrix = IntegerMatrix([[1] for _ in range(5)], bracket_h_buff=SMALL_BUFF)
        label_matrix.scale(0.7)
        label_matrix.next_to(feature_matrix, RIGHT, buff=LARGE_BUFF)
        self.play(Write(label_matrix))

        # Create the rectangle
        rectangle = SurroundingRectangle(feature_matrix.get_columns()[0])
        self.play(Create(rectangle))

        # Animate the rectangle to move across the columns of the feature matrix
        for i in range(1, 5):
            self.play(rectangle.animate.become(SurroundingRectangle(feature_matrix.get_columns()[i])))

        # Animate the rectangle to move to the label matrix
        self.play(rectangle.animate.become(SurroundingRectangle(label_matrix)))

        self.wait()
