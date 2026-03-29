from pptx import Presentation
import json

def extract_ppt_content(file_path):
    prs = Presentation(file_path)

    slides_data = []

    for slide in prs.slides:
        slide_info = {
            "title": "",
            "content": [],
            "layout": slide.slide_layout.name
        }

        for shape in slide.shapes:
            if shape.has_text_frame:
                text = shape.text.strip()

                if shape == slide.shapes.title:
                    slide_info["title"] = text
                else:
                    slide_info["content"].append(text)

        slides_data.append(slide_info)

    return slides_data


def save_json(data, path="data/extracted.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)