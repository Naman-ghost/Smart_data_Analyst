import os
import io
import base64
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.file_parser import parse_file
from utils.llama_prompt import ask_llm
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
CORS(app) 
DATA_CONTEXT = {
    "is_dataframe": False,
    "content_text": "",
    "dataframe": None
}

def get_data_summary(df: pd.DataFrame) -> str:
    schema = ", ".join([f"{col} ({str(dtype)})" for col, dtype in df.dtypes.items()])
    sample = df.head(30).to_csv(index=False)
    return f"Columns: {schema}\n\nSample Data:\n{sample}"

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filename = file.filename
    file_path = os.path.join("temp_files", filename)
    os.makedirs("temp_files", exist_ok=True)
    file.save(file_path)

    parsed = parse_file(file_path)
    if isinstance(parsed, pd.DataFrame):
        DATA_CONTEXT["is_dataframe"] = True
        DATA_CONTEXT["dataframe"] = parsed
        DATA_CONTEXT["content_text"] = get_data_summary(parsed)
    else:
        DATA_CONTEXT["is_dataframe"] = False
        DATA_CONTEXT["dataframe"] = None
        DATA_CONTEXT["content_text"] = parsed

    os.remove(file_path)
    return jsonify({"message": f"File '{filename}' uploaded and parsed successfully."})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided"}), 400

    if not DATA_CONTEXT["content_text"]:
        return jsonify({"error": "No data uploaded yet"}), 400

    prompt = f"""
You are a data analyst expert in data interpretation, visualization, and insightful business analytics.

Given the data context below, answer the user's question thoroughly, with actionable insights and clarity.

Data Context:
{DATA_CONTEXT['content_text']}

User Question:
{question}

Please provide your answer in a clear and structured manner.
"""

    response = ask_llm(prompt)
    return jsonify({"response": response})

@app.route("/visualize", methods=["POST"])
def visualize():
    if not DATA_CONTEXT["is_dataframe"] or DATA_CONTEXT["dataframe"] is None:
        return jsonify({"error": "No tabular data available for visualization"}), 400
    
    data = request.get_json()
    x_col = data.get("x_col")
    y_col = data.get("y_col")
    if not x_col or not y_col:
        return jsonify({"error": "Please provide 'x_col' and 'y_col' in request body"}), 400

    df = DATA_CONTEXT["dataframe"]
    if x_col not in df.columns or y_col not in df.columns:
        return jsonify({"error": "Provided columns not found in data"}), 400

    # Create plot
    plt.figure(figsize=(10,6))
    sns.barplot(x=x_col, y=y_col, data=df.groupby(x_col)[y_col].sum().reset_index().sort_values(by=y_col, ascending=False).head(10))
    plt.title(f"Top {x_col} by {y_col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return jsonify({"image_base64": img_base64})

if __name__ == "__main__":
    app.run(debug=True)
