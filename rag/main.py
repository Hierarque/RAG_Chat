import os
import upload

def main(url):
    doc_name = upload.get_doc_from_url(url)
    try:
        if doc_name.endswith(".pdf"):
            upload.convert_pdf_to_text(doc_name)
        else:
            print("File type not supported")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    if os.getenv("PDF_URL"):
        main(os.environ["PDF_URL"])