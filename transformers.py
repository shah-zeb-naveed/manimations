# Import necessary modules from Manim
from manim import *

class EmbeddingScene(Scene):
    def construct(self):
        # Create a matrix representing the embedding matrix
        embedding_matrix = Matrix([[1, 0.5, 0], [0.2, 0.8, 0.3], [0, 0.4, 1]])
        embedding_matrix.scale(0.8)
        self.play(Create(embedding_matrix))

        # Create arrows to represent the transformation process
        arrow_query = Arrow(embedding_matrix.get_center(), embedding_matrix.get_center() + RIGHT)
        arrow_key = Arrow(embedding_matrix.get_center(), embedding_matrix.get_center() + UP)
        arrow_value = Arrow(embedding_matrix.get_center(), embedding_matrix.get_center() + DOWN)

        self.play(Create(arrow_query), Create(arrow_key), Create(arrow_value))

        # Add labels for Query, Key, and Value
        label_query = Text("Query").next_to(arrow_query, RIGHT)
        label_key = Text("Key").next_to(arrow_key, UP)
        label_value = Text("Value").next_to(arrow_value, DOWN)

        self.play(Create(label_query), Create(label_key), Create(label_value))

        # Show the attention mechanism (optional)
        attention_arrow = Arrow(arrow_query.get_end(), arrow_key.get_start())
        self.play(Create(attention_arrow))

        # Show the final embedding
        final_embedding = Circle(color=BLUE).next_to(embedding_matrix, RIGHT)
        self.play(TransformFromCopy(embedding_matrix, final_embedding))

        # Fade out everything
        self.play(FadeOut(embedding_matrix), FadeOut(arrow_query), FadeOut(arrow_key),
                  FadeOut(arrow_value), FadeOut(label_query), FadeOut(label_key),
                  FadeOut(label_value), FadeOut(attention_arrow))

        self.wait(1)  # Pause for a moment

# Run the scene
if __name__ == "__main__":
    scene = EmbeddingScene()
    scene.render()
