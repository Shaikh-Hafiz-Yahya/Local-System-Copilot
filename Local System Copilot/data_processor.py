import os
from pypdf import PdfReader

def load_local_documents(folder_path):
    """Folder se saari text aur PDF files ka data read karne ke liye"""
    documents = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Agar PDF file hai
        if filename.endswith('.pdf'):
            try:
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                documents.append({"file_name": filename, "content": text})
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
        #Agar normal Text file hai
        elif filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                documents.append({"file_name": filename, "content": f.read()})
                
    return documents