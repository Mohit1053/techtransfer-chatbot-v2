# 🔬 TechTransfer IP Analysis Chatbot

> AI-powered intellectual property analysis tool for research papers and patents

[![CI](https://github.com/Mohit1053/techtransfer-chatbot/actions/workflows/ci.yml/badge.svg)](https://github.com/Mohit1053/techtransfer-chatbot/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**TechTransfer IP Analysis Chatbot** is an AI-powered tool designed to analyze research papers and patents for intellectual property (IP) potential. It uses Google's Gemini AI to extract key information, assess commercial viability, and generate comprehensive IP reports.

### Key Capabilities

| Feature | Description |
|---------|-------------|
| **PDF Processing** | Extract text and images from research papers |
| **AI Analysis** | Multi-question IP assessment using Gemini |
| **Batch Processing** | Analyze multiple papers concurrently |
| **Interactive Chat** | Conversational interface for follow-up questions |
| **Report Generation** | Professional HTML/PDF IP analysis reports |

---

## ✨ Features

### Core Functionality
- 📄 **PDF Text Extraction** - Robust extraction using PyMuPDF
- 🖼️ **Image Extraction** - Extract figures and diagrams
- 🤖 **AI-Powered Analysis** - Google Gemini integration
- 💬 **Interactive Chat** - Follow-up questions and clarifications
- 📊 **Concurrent Processing** - Multi-threaded batch analysis

### Analysis Categories
- **Technology Overview** - Core innovation description
- **Commercial Potential** - Market viability assessment
- **IP Strength** - Patent landscape analysis
- **Competition Analysis** - Existing solutions comparison
- **Development Stage** - TRL (Technology Readiness Level)

### Output Formats
- 🌐 HTML Reports - Interactive web-based reports
- 📄 PDF Export - Professional document output
- 📊 JSON Data - Machine-readable analysis

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- Google Gemini API key(s)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mohit1053/techtransfer-chatbot.git
   cd techtransfer-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

5. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your Google API keys
   ```

---

## 💻 Usage

### Streamlit Web Interface

```bash
streamlit run main.py
```

Then open http://localhost:8501 in your browser.

### Batch Processing

```bash
python batch_paper_analyzer.py --input papers/ --output reports/
```

### API Server

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Command Line

```bash
python process_dataset_folder.py --folder ./papers --output ./results
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Google API Keys (comma-separated for multiple)
GOOGLE_API_KEYS=your-key-1,your-key-2,your-key-3

# Rate limiting
RATE_LIMIT_RPM=60
COOLDOWN_SECONDS=60

# Application settings
LOG_LEVEL=INFO
MAX_QA_WORKERS=8
```

### API Key Management

The system supports multiple API keys with automatic rotation and rate limiting:

- Keys are used in round-robin fashion
- Automatic cooldown on rate limit errors
- Graceful degradation if keys are exhausted

---

## 📁 Project Structure

```
techtransfer-chatbot/
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   ├── ISSUE_TEMPLATE.md
│   └── PULL_REQUEST_TEMPLATE.md
├── main.py                 # Streamlit web application
├── chatbot.py              # AI chat and Q&A logic
├── config.py               # Configuration management
├── pdf_utils.py            # PDF processing utilities
├── api.py                  # FastAPI REST interface
├── batch_paper_analyzer.py # Batch processing script
├── process_dataset_folder.py # Folder processing
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
├── CHANGELOG.md           # Version history
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE                # MIT License
└── README.md              # This file
```

---

## 🔌 API Reference

### REST Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/analyze` | Analyze a PDF document |
| `POST` | `/chat` | Send a chat message |
| `GET` | `/health` | Health check |

### Example Request

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@paper.pdf"
```

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

### Quick Start

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'feat: add feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Security Notice

**IMPORTANT**: Never commit API keys or credentials!

- Use `.env` file for local development
- Add all config files with secrets to `.gitignore`
- Use environment variables in production

---

## 👤 Author

**TechTransfer Chatbot**

- GitHub: [@Mohit1053](https://github.com/Mohit1053)

---

<p align="center">
  Made with ❤️ for technology transfer professionals
</p>


