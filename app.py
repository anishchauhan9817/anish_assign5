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

        if not file:
            return jsonify({"success": False, "error": "No file uploaded"}), 400

        if not file.filename.lower().endswith(".pptx"):
            return jsonify({"success": False, "error": "Upload only .pptx file"}), 400

        # SAVE FILE
        file_path = UPLOAD_DIR / f"{uuid.uuid4().hex}.pptx"
        file.save(file_path)

        # EXTRACT TEXT
        try:
            md = MarkItDown()
            result = md.convert(str(file_path))
            ppt_text = result.text_content.strip()
        except Exception as e:
            return jsonify({"success": False, "error": f"Error reading PPT: {str(e)}"}), 500

        if not ppt_text:
            return jsonify({"success": False, "error": "No content found in PPT"}), 400

        # =========================
        # SMART ANALYSIS
        # =========================
        slides = ppt_text.split("\n\n")
        slide_count = len(slides)
        text_length = len(ppt_text)

        avg_words = text_length // slide_count if slide_count else 0

        suggestions = []

        if slide_count > 50:
            suggestions.append("Too many slides, consider reducing")

        if text_length > 5000:
            suggestions.append("Content is too dense, simplify text")

        if avg_words > 100:
            suggestions.append("Too much text per slide")

        if slide_count < 10:
            suggestions.append("Add more content slides")

        if not suggestions:
            suggestions = [
                "Good structure overall",
                "Consider adding visuals/icons",
                "Improve slide headings"
            ]

        # SCORE SYSTEM
        score = 100

        if slide_count > 50:
            score -= 20

        if text_length > 5000:
            score -= 20

        if avg_words > 100:
            score -= 20

        # ANALYSIS TEXT
        analysis = f"""
📊 PPT ANALYSIS

• Estimated Slides: {slide_count}
• Content Length: {text_length} characters
• Avg Words/Slide: {avg_words}

⭐ Score: {score}/100
"""

        # PREVIEW
        preview_text = "\n\n".join(slides[:3])

        # LINKS
        links = [
            {"name": "🎨 Canva (Best Design)", "url": "https://www.canva.com/templates/presentations/"},
            {"name": "📊 Slidesgo Templates", "url": "https://slidesgo.com/"},
            {"name": "🤖 Gamma AI (Auto Redesign)", "url": "https://gamma.app/"},
            {"name": "📎 Google Slides", "url": "https://docs.google.com/presentation/"}
        ]

        return jsonify({
            "success": True,
            "analysis": analysis.strip(),
            "suggestions": suggestions,
            "score": score,
            "preview": preview_text.strip(),
            "links": links
        })

    except Exception as e:
        return jsonify({"success": False, "error": f"Server Error: {str(e)}"}), 500


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    print("\n🚀 PPT Enhancer running...\n")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)