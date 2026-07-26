import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

AUDIT_SYSTEM_PROMPT = """
Aap ek Strict Compliance Auditor hain.
Aapka kaam di gayi text file ko analyze karna hai aur check karna hai ke kya isme koi critical policy violation ya security risk hai (jaise credit card numbers, sensitive passwords, plain text personal data leak, ya unauthorized actions).

Output Format Rules:
1. Agar file mein koi sensitive data (jaise credit card number, phone, email ya password) leaks ho raha hai, toh clear Urdu/English mein likhein ke kya violation mili hai.
2. Agar sab kuch safe hai, sirf tabhi likhein: "No Violation Found".

Faltu baatein mat likhein, direct report dein.
"""

def audit_document_with_gemma(file_name, content):
    """Gemma 3:1b ko document bhej kar audit karwana"""
    
    # Chote model ke liye content ko limit karna zaroori hai agar file bohot bari ho
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