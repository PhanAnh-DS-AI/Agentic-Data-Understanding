import pytest
from src.agents.document_agent import DocumentAgent
from src.models.document_structure import DocumentStructure

@pytest.mark.parametrize("file_path", [
    "src/tools/document_tools/pdf_parser.py",
    "src/tools/document_tools/docx_parser.py",
    "src/tools/document_tools/pptx_parser.py"
])
def test_document_agent(file_path):
    """
    Kiểm tra chức năng của DocumentAgent với các loại file khác nhau.
    
    Args:
        file_path (str): Đường dẫn đến file cần kiểm tra
    """
    # Khởi tạo DocumentAgent
    agent = DocumentAgent()
    
    # Chạy agent và lấy kết quả
    result = agent.run(file_path)
    
    # Kiểm tra kiểu dữ liệu của kết quả
    assert isinstance(result, DocumentStructure), "Kết quả phải là một instance của DocumentStructure"
    assert isinstance(result.title, str), "Tiêu đề phải là một chuỗi"
    assert isinstance(result.headings, list), "Danh sách tiêu đề phụ phải là một list"
    assert isinstance(result.paragraphs, list), "Danh sách đoạn văn phải là một list"
    
    # Kiểm tra xem các thuộc tính không rỗng (tùy thuộc vào nội dung file mẫu)
    assert len(result.title) > 0, "Tiêu đề không được rỗng"
    assert len(result.paragraphs) > 0, "Phải có ít nhất một đoạn văn"

def test_unsupported_file_format():
    """Kiểm tra xử lý lỗi khi file không được hỗ trợ"""
    agent = DocumentAgent()
    with pytest.raises(ValueError):
        agent.extract_raw_text("data/sample.txt")