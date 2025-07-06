# Agentic Data Understand

An intelligent document processing system that uses multi-agent AI to understand and analyze various document types including PDFs, Word documents, PowerPoint presentations, and Markdown files.

## 🎯 Project Overview

Agentic Data Understand is a sophisticated document analysis platform that leverages multiple AI agents to comprehensively process and understand documents. The system can extract text, images, tables, perform OCR on scanned documents, and provide intelligent summaries and insights.

### Key Features

- **Multi-Agent Architecture**: Specialized agents for different document elements (text, images, tables)
- **Tool-Calling System**: Agents can call specific tools for specialized tasks
- **Multi-Format Support**: PDF, Word (.docx), PowerPoint (.pptx), Markdown files
- **Advanced OCR**: Extract text from scanned documents and images
- **Image Analysis**: Understand and describe images within documents
- **Table Detection & Analysis**: Extract and analyze tabular data
- **Intelligent Summarization**: Generate comprehensive document summaries
- **Workflow Orchestration**: Automated processing pipelines

## 🏗️ Architecture

The system uses a multi-agent approach where different specialized agents coordinate to process documents:

1. **Orchestrator Agent**: Coordinates the entire workflow
2. **Document Agent**: Handles document parsing and text extraction
3. **Image Agent**: Analyzes images and performs OCR
4. **Table Agent**: Detects and analyzes tabular data
5. **Summary Agent**: Generates final comprehensive summaries

## 📁 Project Structure

```
Agent-Data-Understand/
├── src/
│   ├── agents/                    # Agent orchestration and coordination
│   │   ├── orchestrator_agent.py  # Main coordinator agent
│   │   ├── document_agent.py      # Document understanding agent
│   │   ├── image_agent.py         # Image analysis agent
│   │   ├── table_agent.py         # Table analysis agent
│   │   └── summary_agent.py       # Final summarization agent
│   │
│   ├── tools/                     # Tool implementations
│   │   ├── document_tools/        # Document parsing tools
│   │   ├── vision_tools/          # OCR, image extraction, table detection
│   │   ├── analysis_tools/        # Text analysis, summarization
│   │   └── utility_tools/         # File handling, data formatting
│   │
│   ├── models/                    # Data models and schemas
│   ├── workflows/                 # Predefined workflow patterns
│   ├── utils/                     # Utility functions
│   └── api/                       # API layer (optional)
│
├── tests/                         # Unit and integration tests
├── data/                          # Data storage (input, processed, output)
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Agent-Data-Understand.git
cd Agent-Data-Understand
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

```python
from src.main import DocumentProcessor

# Initialize the processor
processor = DocumentProcessor()

# Process a document
result = processor.process_document("path/to/your/document.pdf")

# Get the summary
print(result.summary)

# Get extracted tables
print(result.tables)

# Get image descriptions
print(result.image_analyses)
```

### Command Line Interface

```bash
python src/main.py --input document.pdf --output results.json
```

## 🔧 Configuration

Create a `config.py` file or set environment variables for:

- AI model API keys
- Processing parameters
- Output formats
- Storage paths

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern AI/ML libraries
- Inspired by multi-agent systems research
- Community contributions welcome

## 📞 Support

For questions and support, please open an issue on GitHub or contact the maintainers.

---

**Note**: This project is under active development. Features and APIs may change as the system evolves.