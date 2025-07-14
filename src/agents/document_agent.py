from transformers import pipeline
from langchain import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from src.models.document_structure import DocumentStructure
from src.tools.document_tools.pdf_parser import parse_pdf
from src.tools.document_tools.docx_parser import parse_docx
from src.tools.document_tools.pptx_parser import parse_pptx

# Khởi tạo parser schema để phân tích đầu ra theo cấu trúc DocumentStructure
parser = PydanticOutputParser(pydantic_object=DocumentStructure)

# Tạo PromptTemplate với hướng dẫn định dạng
prompt = PromptTemplate(
    template=(
        "Bạn là DocumentAgent, một trợ lý thông minh chuyên phân tích tài liệu. "
        "Nhiệm vụ của bạn là trích xuất cấu trúc tài liệu (tiêu đề, tiêu đề phụ, đoạn văn) "
        "từ văn bản thô và trả về dưới dạng JSON theo định dạng sau:\n"
        "{format_instructions}\n\n"
        "Dưới đây là nội dung văn bản cần phân tích:\n"
        "{text}\n\n"
        "Hãy trả về kết quả dưới dạng JSON chính xác và đầy đủ."
    ),
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Khởi tạo pipeline LLM từ Hugging Face
hf_pipe = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    device=0,
    max_new_tokens=512,
    temperature=0.1
)

# Tích hợp pipeline vào LangChain
llm = HuggingFacePipeline(pipeline=hf_pipe)

class DocumentAgent:
    """Agent thông minh để trích xuất và cấu trúc văn bản từ tài liệu"""
    def __init__(self):
        """Khởi tạo DocumentAgent với LLM, prompt và parser"""
        self.llm = llm
        self.prompt = prompt
        self.parser = parser

    def extract_raw_text(self, file_path: str) -> str:
        """
        Trích xuất văn bản thô từ file dựa trên phần mở rộng.
        
        Args:
            file_path (str): Đường dẫn đến file tài liệu
        
        Returns:
            str: Văn bản thô trích xuất từ file
            
        Raises:
            ValueError: Nếu định dạng file không được hỗ trợ
        """
        ext = file_path.lower().split('.')[-1]
        if ext == 'pdf':
            return parse_pdf(file_path)
        elif ext == 'docx':
            return parse_docx(file_path)
        elif ext == 'pptx':
            return parse_pptx(file_path)
        else:
            raise ValueError(f"Định dạng file không được hỗ trợ: {ext}")

    def run(self, file_path: str) -> DocumentStructure:
        """
        Chạy DocumentAgent để trích xuất cấu trúc từ file tài liệu.
        
        Args:
            file_path (str): Đường dẫn đến file tài liệu
        
        Returns:
            DocumentStructure: Cấu trúc tài liệu được phân tích
        
        Raises:
            ValueError: Nếu trích xuất văn bản thất bại
            Exception: Nếu LLM hoặc parser gặp lỗi
        """
        # 1) Trích xuất văn bản thô từ file
        raw_text = self.extract_raw_text(file_path)
        
        # 2) Định dạng prompt với văn bản thô
        formatted_prompt = self.prompt.format(text=raw_text)
        
        # 3) Gọi LLM để xử lý prompt và lấy kết quả
        llm_output = self.llm(formatted_prompt)[0]['generated_text']
        
        # 4) Phân tích đầu ra của LLM thành cấu trúc DocumentStructure
        structured_output = self.parser.parse(llm_output)
        
        return structured_output