import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

AUDIT_SYSTEM_PROMPT = """
You are a Strict Compliance Auditor.
Your task is to analyze the given text file and determine whether it contains any critical policy violations or security risks (such as credit card numbers, sensitive passwords, plain-text personal data leaks, or unauthorized actions).

Output Format Rules:
1. If the file contains any sensitive data (such as credit card numbers, phone numbers, email addresses, or passwords), clearly describe the detected violation in English.
2. If everything is safe, only write: "No Violation Found".

Do not include unnecessary explanations. Provide only the audit report.
"""

def audit_document_with_gemma(file_name, content):
    """Send the document to Gemma 3:1b for compliance auditing."""

    #Limit the content length for smaller models if the file is very large.
    truncated_content = content[:3000]

    prompt = f"""
    {AUDIT_SYSTEM_PROMPT}

    Document Name: {file_name}
    Document Content:
    \"\"\"{truncated_content}\"\"\"

    Audit Report:
    """

    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        return response.json()['response']
    except Exception as e:
        return f"Error connecting to local Gemma model: {e}"