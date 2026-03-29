from core.extractor import extract_ppt_content, save_json
from core.selector import select_best_template
from core.generator import generate_presentation

input_file = "uploads/sample.pptx"
# Step 1: Extract
slides = extract_ppt_content(input_file)
save_json(slides)

# Step 2: Select template
template = select_best_template(slides)

# Step 3: Generate new PPT
generate_presentation(template, slides)

print("✅ Final presentation generated!")
