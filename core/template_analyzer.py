from pptx import Presentation

def analyze_template(template_path):
    prs = Presentation(template_path)

    layouts = []

    for layout in prs.slide_layouts:
        layouts.append(layout.name)

    return {
        "template": template_path,
        "layouts": layouts,
        "layout_count": len(layouts)
    }