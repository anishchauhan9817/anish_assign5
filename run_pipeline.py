from core.extractor import extract_ppt_content, save_json
from core.selector import select_best_template
from core.generator import generate_presentation
import os

# Input file
input_file = "uploads/sample.pptx"

# Step 1: Extract content
data = extract_ppt_content(input_file)

# Save extracted JSON (IMPORTANT for assignment)
os.makedirs("output", exist_ok=True)
save_json(data, "output/extracted.json")

# Step 2: Select best template
template_name, score = select_best_template("templates_ppt")

print(f"✅ Selected Template: {template_name} (Score: {score})")

# Step 3: Generate final presentation
template_path = f"templates_ppt/{template_name}"

output_path = generate_presentation(data, template_path)

print(f"✅ Final presentation generated at: {output_path}")