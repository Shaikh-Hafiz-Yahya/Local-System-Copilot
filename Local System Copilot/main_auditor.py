import os
from data_processor import load_local_documents
from audit_engine import audit_document_with_gemma

def run_compliance_audit():
    # Folder jahan hospital ke sensitive records rakhay hain
    # Aap check karne ke liye ek 'records' naam ka folder bana kar usme test txt/pdf rakh sakte hain
    records_folder = "./secure_records" 
    
    if not os.path.exists(records_folder):
        os.makedirs(records_folder)
        print(f"⚠️ '{records_folder}' folder bana diya hai. Isme apni test files rakhein aur dobara run karein.")
        return

    print("🔍 Scanning local secure drive...")
    docs = load_local_documents(records_folder)
    
    if not docs:
        print("❌ Folder mein koi text ya PDF files nahi mili.")
        return
        
    print(f"📋 Total {len(docs)} files mili hain. Auditing started with Gemma 3:1b...\n")
    print("="*50)
    
    for doc in docs:
        print(f"📄 Auditing File: {doc['file_name']}")
        print("-" * 30)
        
        # Running local AI audit
        report = audit_document_with_gemma(doc['file_name'], doc['content'])
        
        print(f"[Gemma 3:1b Audit Result]:\n{report}")
        print("="*50)

if __name__ == "__main__":
    run_compliance_audit()