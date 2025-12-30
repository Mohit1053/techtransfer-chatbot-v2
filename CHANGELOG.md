# Changelog

All notable changes to the TechTransfer Chatbot will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Docker containerization
- Additional AI model support (OpenAI, Anthropic)
- Enhanced report templates
- Database integration for analysis history

## [1.0.0] - 2025-12-30

### Added
- Initial release of TechTransfer IP Analysis Chatbot
- Streamlit web interface (`main.py`)
- AI-powered Q&A analysis (`chatbot.py`)
- PDF text and image extraction (`pdf_utils.py`)
- REST API interface (`api.py`)
- Batch processing capability (`batch_paper_analyzer.py`)
- Dataset folder processing (`process_dataset_folder.py`)
- Multi-key API management with rate limiting
- Interactive chat for follow-up questions
- HTML report generation

### Security
- API key management via environment variables
- Comprehensive .gitignore for secrets
- Rate limiting and cooldown handling
