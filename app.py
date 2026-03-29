import uuid
import os
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from markitdown import MarkItDown

app = Flask(__name__)

# =========================
# CONFIG
# =========================
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# Limit file size (optional but recommended: 10MB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# =========================
# HOME ROUTE
# =========================
@app.route("/")
def index():
    return render_template("index.html")

# =========================
# ENHANCE ROUTE
# =========================
@app.route("/enhance", methods=["POST"])
def enhance():
    try:
        file = request.files.get("pptx_file")

        # ❌ Validation
        if not file:
            return jsonify({"success": False, "error": "No file uploaded"}), 400

        if not file.filename.lower().endswith(".pptx"):
            return jsonify({"success": False, "error": "Upload only .pptx file"}), 400

        # =========================
        # SAVE FILE
        # =========================
        file_path = UPLOAD_DIR / f"{uuid.uuid4().hex}.pptx"
        file.save(file_path)

        # =========================
        # EXTRACT TEXT
        # =========================
        try:
            md = MarkItDown()
            result = md.convert(str(file_path))
            ppt_text = result.text_content.strip()
        except Exception as e:
            return jsonify({"success": False, "error": f"Error reading PPT: {str(e)}"}), 500

        if not ppt_text:
            return jsonify({"success": False, "error": "No content found in PPT"}), 400

        # =========================
        # ANALYSIS
        # =========================
        slides = ppt_text.split("\n\n")
        slide_count = len(slides)
        text_length = len(ppt_text)

        analysis = f"""
📊 PPT ANALYSIS

• Estimated Slides: {slide_count}
• Content Length: {text_length} characters

💡 Suggestions:
- Reduce text
- Add visuals/icons
- Keep 1 idea per slide
- Use better headings
"""

        # =========================
        # PREVIEW
        # =========================
        preview_text = "\n\n".join(slides[:3])

        # =========================
        # REDIRECT LINKS
        # =========================
        links = [
            {"name": "🎨 Canva (Best Design)", "url": "https://www.canva.com/templates/presentations/"},
            {"name": "📊 Slidesgo Templates", "url": "https://slidesgo.com/"},
            {"name": "🤖 Gamma AI (Auto Redesign)", "url": "https://gamma.app/"},
            {"name": "📎 Google Slides", "url": "https://docs.google.com/presentation/"}
        ]

        return jsonify({
            "success": True,
            "analysis": analysis.strip(),
            "preview": preview_text.strip(),
            "links": links
        })

    except Exception as e:
        return jsonify({"success": False, "error": f"Server Error: {str(e)}"}), 500


# =========================
# RUN APP (RENDER READY)
# =========================
if __name__ == "__main__":
    print("\n🚀 PPT Enhancer running...\n")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)