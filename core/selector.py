import os
from core.template_analyzer import analyze_template

def select_best_template(input_slides, template_folder="templates_ppt"):
    best_score = -1
    best_template = None

    for file in os.listdir(template_folder):
        if file.endswith(".pptx"):
            path = os.path.join(template_folder, file)
            analysis = analyze_template(path)

            # simple scoring
            score = analysis["layout_count"]

            if score > best_score:
                best_score = score
                best_template = path

    # save selected template
    with open("output/selected_template.txt", "w") as f:
        f.write(best_template)

    return best_template