# 📊 PPTX Content Extraction & Template-Based Presentation Generation

## 🔍 Overview

This project is an automated system that processes PowerPoint (PPTX) files to:

1. Extract structured content from a source presentation
2. Analyze multiple PPTX templates
3. Select the most suitable template using a scoring mechanism
4. Generate a new presentation using the selected template

The system is built using Python and follows an end-to-end automated workflow.

---

## 🚀 Live Demo

👉 https://ppt-enhancer.onrender.com

---

## 📂 GitHub Repository

👉 https://github.com/anishchauhan9817/anish_assign5

---

## ⚙️ Features

* ✅ Extracts structured content from PPTX files
* ✅ Supports titles, body text, and bullet points
* ✅ Analyzes multiple presentation templates
* ✅ Uses scoring logic to select the best template
* ✅ Automatically generates a new PPTX using the selected template
* ✅ End-to-end automation

---

## 🧠 Approach

The system is modularized into extractor, analyzer, selector, and generator components, ensuring scalability and maintainability.

### 1. Content Extraction

The system reads the input PPTX file and extracts:

* Slide titles
* Body text
* Bullet points
* Slide structure information

The extracted data is converted into a structured JSON format, which is later used for rebuilding the presentation.

---

### 2. Template Analysis

Each available template is analyzed to understand:

* Available slide layouts
* Placeholder types (title, content, etc.)
* Supported content structures

This helps determine how well a template can accommodate the extracted content.

---

### 3. Template Selection (Scoring Logic)

A scoring-based approach is used to select the best template.

Each template is evaluated based on:

* ✔️ Support for title + content layouts
* ✔️ Compatibility with bullet points
* ✔️ Number of usable layouts
* ✔️ Flexibility of placeholders

#### Example Scoring Logic:

* Title + Content layout → +5
* Bullet support → +3
* Multiple layouts → +2

The template with the highest score is selected.

The selected template name is saved for reference.

---

### 4. Final Presentation Generation

Using the selected template:

* Slides are recreated
* Titles are mapped to title placeholders
* Body content is inserted correctly
* Bullet points are preserved

Final output is generated as:

```
output/final_presentation.pptx
```

---

## 🛠️ Tech Stack & Libraries

* Python
* python-pptx
* Flask (for web interface)
* JSON (for structured data handling)

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/anishchauhan9817/anish_assign5.git
cd anish_assign5
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the application (Web)

```bash
python app.py
```

---

### 4. Run pipeline directly (CLI)

```bash
python3 run_pipeline.py
```

---

### 5. Open in browser

```
http://localhost:5000
```

---

## 📁 Project Structure

```
├── app.py
├── core/
├── templates/
├── templates_ppt/
├── output/
│   └── final_presentation.pptx
├── requirements.txt
├── run_pipeline.py
└── README.md
```

---

## 📈 Evaluation Criteria Coverage

| Requirement              | Status        |
| ------------------------ | ------------- |
| Content Extraction       | ✅ Implemented |
| Template Analysis        | ✅ Implemented |
| Template Selection Logic | ✅ Implemented |
| PPT Generation           | ✅ Implemented |
| Documentation            | ✅ Completed   |

---

## 💡 Future Improvements

* Advanced AI-based template matching
* Better layout adaptation
* Table and image extraction support
* Design similarity scoring

---

## 👨‍💻 Author

**Anish Chauhan**

---

## ✅ Conclusion

This project successfully demonstrates an automated pipeline for transforming PPTX presentations using intelligent template selection and structured content extraction.
