! pip install pydantic

from pydantic import BaseModel, Field
from typing import List

class DocumentStructure(BaseModel):
    """Định nghĩa cấu trúc đầu ra của DocumentAgent"""
    title: str = Field(..., description="Tên hoặc tiêu đề tài liệu")
    headings: List[str] = Field(default_factory=list, description="Danh sách các heading")
    paragraphs: List[str] = Field(default_factory=list, description="Danh sách các đoạn văn")