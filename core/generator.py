from pptx import Presentation

def generate_presentation(template_path, slides_data):
    prs = Presentation(template_path)

    for slide_data in slides_data:
        layout = prs.slide_layouts[1]  # basic layout
        slide = prs.slides.add_slide(layout)

        # Title
        slide.shapes.title.text = slide_data["title"]

        # Content
        if len(slide.placeholders) > 1:
            content = "\n".join(slide_data["content"])
            slide.placeholders[1].text = content

    prs.save("output/final_presentation.pptx")
    