# Import các hàm parser
from src.tools.document_tools.pdf_parser import parse_pdf
from src.tools.document_tools.docx_parser import parse_docx
from src.tools.document_tools.pptx_parser import parse_pptx

# Ví dụ sử dụng
try:
    # Trích xuất văn bản từ PDF
    pdf_text = parse_pdf("c:/Users/Admin/Downloads/Deep-Learning-with-Python.pdf")
    print("Nội dung PDF:")
    print(pdf_text)

    # Trích xuất văn bản từ DOCX
    docx_text = parse_docx("c:/Users/Admin/Downloads/Date-2025-07-10_Time-18-57_IELTS-Writing-Task-2_Score-6.0-LexiBot.docx")
    print("\nNội dung DOCX:")
    print(docx_text)

    # Trích xuất văn bản từ PPTX
    pptx_text = parse_pptx("c:/Users/Admin/Downloads/NST.pptx")
    print("\nNội dung PPTX:")
    print(pptx_text)
except Exception as e:
    print(f"Lỗi: {e}")

    c:\Users\Admin\Downloads\Agentic-Data-Understanding 