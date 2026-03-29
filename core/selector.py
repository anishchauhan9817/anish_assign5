from pptx import Presentation
import os

def analyze_template(path):
    prs = Presentation(path)
    score = 0

    for layout in prs.slide_layouts:
        name = layout.name.lower()

        if "title" in name and "content" in name:
            score += 5
        if "two" in name:
            score += 2

    return score


def select_best_template(folder):
    best_score = -1
    best_template = None

    for file in os.listdir(folder):
        if file.endswith(".pptx"):
            path = os.path.join(folder, file)
            score = analyze_template(path)

            if score > best_score:
                best_score = score
                best_template = file

    # Save result (VERY IMPORTANT FOR ASSIGNMENT)
    with open("output/selected_template.txt", "w") as f:
        f.write(best_template)

    return best_template, best_score