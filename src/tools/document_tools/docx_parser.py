from docx import Document

def parse_docx(path: str) -> str:
    """Trích xuất toàn bộ text thô từ file Word (.docx).
    
    Args:
        path (str): Đường dẫn đến file DOCX.
    
    Returns:
        str: Văn bản thô được trích xuất từ tất cả các đoạn văn của DOCX, cách nhau bởi ký tự xuống dòng.
    
    Raises:
        FileNotFoundError: Nếu file không tồn tại tại đường dẫn được cung cấp.
        Exception: Nếu có lỗi xảy ra trong quá trình xử lý file DOCX (ví dụ: file không hợp lệ).
    """
    try:
        # Mở file DOCX bằng python-docx
        doc = Document(path)
        # Trích xuất văn bản từ từng đoạn văn, loại bỏ đoạn rỗng hoặc chỉ chứa khoảng trắng
        paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        # Kết hợp các đoạn văn thành một chuỗi, cách nhau bởi ký tự xuống dòng
        return "\n".join(paras)
    except FileNotFoundError:
        raise FileNotFoundError(f"File DOCX không tồn tại: {path}")
    except Exception as e:
        raise Exception(f"Lỗi khi xử lý DOCX: {str(e)}")