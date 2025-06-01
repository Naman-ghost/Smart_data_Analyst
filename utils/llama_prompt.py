import requests
import os

TOGETHER_API_KEY = "dd1cb80c775bba39d38043bb1053ce6ce75a940874d32bdcd7f0b6e6918c23e1"

headers = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"

def ask_llm(prompt):
    url = "https://api.together.xyz/inference"
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop": ["User:", "Agent:"]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            print("❌ API Error:", response.status_code)
            print("🔴 Response:", response.text[:500])
            return "[API Error]"

        result = response.json()
        # Extract output from "choices" array
        if "choices" in result and len(result["choices"]) > 0:
            output = result["choices"][0].get("text", "").strip()
            if output:
                return output
            else:
                return "[No output text]"
        else:
            print("⚠️ Unexpected response format:", result)
            return "[No output]"
    except Exception as e:
        return f"[Error] {str(e)}"
