import os
from data_processor import load_local_documents
from audit_engine import audit_document_with_gemma


def run_compliance_audit():
    # Folder containing sensitive hospital records.
    # Create a folder named 'secure_records' and place your test TXT/PDF files inside it.
    records_folder = "./secure_records"

    if not os.path.exists(records_folder):
        os.makedirs(records_folder)
        print(f"'{records_folder}' folder has been created. Place your test files inside it and run the program again.")
        return

    print("Scanning local secure drive...")
    docs = load_local_documents(records_folder)

    if not docs:
        print("No text or PDF files were found in the folder.")
        return

    print(f"Found {len(docs)} file(s). Starting compliance audit using Gemma 3:1b...\n")
    print("=" * 50)

    for doc in docs:
        print(f"Auditing File: {doc['file_name']}")
        print("-" * 30)

        # Run the local AI-powered compliance audit
        report = audit_document_with_gemma(doc['file_name'], doc['content'])

        print(f"[Gemma 3:1b Audit Result]:\n{report}")
        print("=" * 50)


if __name__ == "__main__":
    run_compliance_audit()