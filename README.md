# 📊 Smart Data Analyst

> Your intelligent assistant for analyzing sales and business data with LLM + Python visualizations.

![LLM + Data](https://img.shields.io/badge/AI-Powered-green?style=flat&logo=OpenAI) ![Flask](https://img.shields.io/badge/Backend-Flask-blue) ![HTML](https://img.shields.io/badge/Frontend-HTML/CSS-yellow) ![Notebook](https://img.shields.io/badge/Notebook-Jupyter-orange)

---

## 🚀 Overview

Smart Data Analyst enables business users and analysts to:
- Upload structured data files (CSV, Excel) or text-based reports.
- Ask questions using natural language (LLM-powered).
- View intelligent insights and automatic visualizations (bar charts).
- Use a simple frontend (no React) or Jupyter Notebook for direct interaction.

---

## 🗂️ Project Structure

```
Smart_data_Analyst/
├── app.py                       # Flask backend for API routes
├── frontend/
│   └── index.html               # HTML + JS UI for file upload, query, visualization
├── smart_data_analyst.ipynb     # Jupyter notebook for testing LLM + data
├── sample_files/
│   ├── sample.csv               # Rich sample with 40+ columns
│   ├── sample.xlsx              # Excel version
│   └── sales_summary.txt        # Text summary file (40+ lines)
├── utils/
│   ├── file_parser.py           # Parses .csv, .xlsx, .txt files
│   └── llama_prompt.py          # Calls Together.ai LLM API
├── requirements.txt             # Dependencies list
└── README.md                    # This file
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Naman-ghost/Smart_data_Analyst.git
cd Smart_data_Analyst
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Together API Key

In `utils/llama_prompt.py`, set:

```python
TOGETHER_API_KEY = "your-api-key-here"
```

Get one from https://app.together.ai/

---

## ▶️ Run the Web App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📒 Use via Jupyter Notebook

Open:

```
notebook/smart_data_analyst.ipynb
```

It supports:
- File loading and preview
- LLM-powered analysis
- Basic barplot visualization

---

## 📤 Uploadable File Types

Supported formats:
- `.csv`
- `.xlsx`
- `.txt`

See sample files inside `/sample_files`.

---

## 🌐 API Endpoints

| Route          | Method | Description                                |
|----------------|--------|--------------------------------------------|
| `/upload`      | POST   | Upload a CSV/XLSX/TXT file                 |
| `/ask`         | POST   | Ask a question about the uploaded data     |
| `/visualize`   | POST   | Generate bar plot with `x_col`, `y_col`    |

Use Postman or the provided HTML form.

---

## 🖼️ Frontend Preview

Minimal, clean UI to:
- Upload files
- Ask questions
- View intelligent insights and visual plots

All built using plain **HTML + CSS**.

---

## ✅ Example Questions

- What are the top 5 most sold products?
- Compare sales across regions.
- What’s the trend in weekly revenue?
- Visualize quantity vs category.

---

## ✨ Credits

- LLM Model: [Together.ai - LLaMA-4 Maverick 17B](https://www.together.ai/)
- Built by: [@Naman-ghost](https://github.com/Naman-ghost)
- UI built with love in plain HTML + CSS

---

## 📌 To Do

- [ ] Add Excel multi-sheet support
- [ ] Add pie chart/line chart options
- [ ] Save uploaded files in DB or session

---

## 📜 License

MIT
