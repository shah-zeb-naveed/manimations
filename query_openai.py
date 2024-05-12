from openai import OpenAI

client = OpenAI()

# Set your OpenAI API key

def query_gpt(prompt, model="gpt-4-turbo"):
    try:
        response = client.completions.create(engine=model,
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"])
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error:", e)
        return None


prompt = """
Need to create an animation for an explanation video on how curve fitting works in ML. 

# Visualization Concept
1. A set of dots roughly scattered like a sine curve on a graph (not a pure sine curve but with some noise)
2. then another solid curve (depicting the curve defined by an ML model) appears. It starts as a straight line but then as the training progresses, the straight line fits into the set of dots and ultimately transforms into a sine curve.
3. Then create similar scenes for 2 additional curves

# Instructions
1. Be creative to add animations as needed and as possible in the Manim python library.
2. First, create a proper plan of action to think what exactly will you be visualizing (graphic elements, formulas, etc.) to explain what concepts.
3. Then translate that action plan to a python script.
4. Do not add any full sentences on the screen. You can however use labels as text if needed.
5. Make sure to not use Manim functionality that is deprecated.
"""

response = query_gpt(prompt)
print("Response:", response)
