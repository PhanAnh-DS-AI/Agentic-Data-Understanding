import fitz  # PyMuPDF

def parse_pdf(path: str) -> str:
    """Trích xuất toàn bộ text thô từ file PDF.
    
    Args:
        path (str): Đường dẫn đến file PDF.
    
    Returns:
        str: Văn bản thô được trích xuất từ tất cả các trang của PDF, cách nhau bởi ký tự xuống dòng.
    
    Raises:
        FileNotFoundError: Nếu file không tồn tại tại đường dẫn được cung cấp.
        Exception: Nếu có lỗi xảy ra trong quá trình xử lý file PDF (ví dụ: file bị hỏng).
    """
    try:
        # Mở file PDF bằng PyMuPDF
        doc = fitz.open(path)
        # Trích xuất văn bản từ từng trang và lưu vào danh sách
        pages = [page.get_text("text") for page in doc]
        # Kết hợp văn bản từ tất cả các trang, cách nhau bởi ký tự xuống dòng
        return "\n".join(pages)
    except FileNotFoundError:
        raise FileNotFoundError(f"File PDF không tồn tại: {path}")
    except Exception as e:
        raise Exception(f"Lỗi khi xử lý PDF: {str(e)}")