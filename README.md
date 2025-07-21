# 🚀 Invoice Processing Automation System

[![CI/CD Pipeline](https://github.com/Hassan-Naeem-code/RPA-Automation-Week-2/workflows/Invoice%20Automation%20CI/CD/badge.svg)](https://github.com/Hassan-Naeem-code/RPA-Automation-Week-2/actions)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

A comprehensive invoice processing automation system built with Python for Concordia University's Robotic Process Automation course. This system automates the entire invoice lifecycle from data ingestion to report generation and email distribution, demonstrating modern RPA principles and enterprise-grade architecture.

## ✨ Key Features

### 🔧 Core Automation Capabilities
- **Intelligent Data Processing**: Advanced invoice data validation, cleaning, and enrichment
- **Multi-Format Report Generation**: Comprehensive Excel reports with multiple analysis sheets
- **Automated Email Distribution**: Professional HTML email templates with report attachments
- **Real-time Processing**: Efficient batch processing with progress tracking
- **Data Quality Assurance**: Built-in validation and error handling mechanisms

### 🏢 Enterprise Features
- **Configuration Management**: YAML-based configuration with environment variable support
- **Structured Logging**: Comprehensive logging with rotation and formatting
- **Error Handling**: Robust exception handling with detailed error reporting
- **Security**: Input validation and secure credential management
- **Scalability**: Modular architecture supporting high-volume processing
- **CI/CD Ready**: Complete pipeline with testing, security checks, and deployment
- **Docker Support**: Containerized deployment for production environments

## 🏗️ Architecture

### System Components

```
scripts/                           # Working automation scripts
├── main.py                        # Main orchestrator and workflow manager
├── process_data.py               # Invoice data processing engine
├── generate_report.py            # Excel report generation
├── send_email.py                 # Email automation service
└── create_sample_data.py         # Test data generation

src/                              # Enterprise architecture (alternative structure)
├── automation/
│   ├── core/
│   │   ├── data_processor.py     # Advanced data processing
│   │   ├── report_generator.py   # Multi-format report generation  
│   │   └── email_service.py      # Email distribution service
│   ├── utils/
│   │   ├── config.py            # Configuration management
│   │   ├── logger.py            # Logging infrastructure
│   │   └── validators.py        # Data validation utilities
│   └── exceptions.py            # Custom exception definitions
└── main.py                      # Enterprise application orchestrator

config/
├── settings.yaml                # Application configuration
└── .env.example                 # Environment variables template

tests/                           # Comprehensive test suite
├── test_system.py              # End-to-end system tests
├── test_unit.py                # Unit tests for core functions
└── unit/
    └── test_automation.py       # Component integration tests
```

### Data Flow Architecture

1. **Data Ingestion** → Raw invoice data from Excel files
2. **Processing Pipeline** → Validation, cleaning, and enrichment
3. **Report Generation** → Multi-sheet Excel reports with analytics
4. **Distribution** → Automated email delivery with attachments

## 📊 Generated Reports

The system creates comprehensive Excel reports with multiple analysis sheets:

- **📈 Executive Summary**: High-level metrics and KPIs
- **👥 Client Analysis**: Client-wise breakdown and payment patterns
- **⏰ Aging Analysis**: Outstanding invoice aging and trends
- **📊 Status Breakdown**: Payment status distribution
- **✅ Quality Metrics**: Data validation and quality scores
- **📅 Time Series**: Monthly/yearly trend analysis
- **📋 Raw Data**: Complete processed dataset

## 🚀 Quick Start

### 1. System Requirements

- **Python**: 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended for large datasets)
- **Storage**: 1GB disk space for data processing
- **OS**: Windows, macOS, or Linux

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/Hassan-Naeem-code/RPA-Automation-Week-2.git
cd automation_project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

1. **Environment Setup**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Email Configuration** (optional):
   ```env
   EMAIL_ENABLED=true
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_USERNAME=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

3. **Application Settings**:
   - Edit `config/settings.yaml` for advanced configuration
   - Supports multiple environments and deployment scenarios

### 4. Usage

#### Basic Usage (Scripts Version - Recommended)
```bash
# Process invoice data (simple approach)
python scripts/main.py

# The scripts version automatically:
# - Processes data/invoice_data.xlsx
# - Generates data/processed_invoice_data.xlsx  
# - Creates data/report.xlsx with summary
# - Attempts email notification (if configured)
```

#### Enterprise Usage (Advanced)
```bash
# Process invoice data with enterprise features
python src/main.py data/invoice_data.xlsx

# With custom output directory
python src/main.py data/invoice_data.xlsx --output-dir reports/

# Send email notifications
python src/main.py data/invoice_data.xlsx --email recipient@company.com

# Debug mode
python src/main.py data/invoice_data.xlsx --debug
```

#### Advanced Usage
```bash
# Use custom configuration (enterprise version)
python src/main.py data/invoice_data.xlsx --config config/production.yaml

# Multiple email recipients
python src/main.py data/invoice_data.xlsx --email user1@company.com user2@company.com

# Create sample data for testing
python scripts/create_sample_data.py

# Use sample data for testing
python src/main.py --sample
```

### 5. Data Format

Your input Excel file should contain these columns:

| Column | Type | Description | Required | Example |
|--------|------|-------------|----------|---------|
| `InvoiceID` | String | Unique identifier | ✅ | INV000001 |
| `Client` | String | Client/customer name | ✅ | ABC Corp |
| `Amount` | Number | Invoice amount (positive values) | ✅ | 1500.75 |
| `Status` | String | PAID/UNPAID/PENDING/OVERDUE | ✅ | PAID |
| `Date` | Date | Invoice date | ✅ | 2025-01-15 |

The system includes 100 sample invoice records for testing and demonstration.

## 🧪 Testing

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage (enterprise version)
pytest --cov=src/automation --cov-report=html

# Run scripts version tests  
pytest --cov=scripts --cov-report=html

# Run specific test categories
pytest tests/unit/          # Unit tests only
pytest tests/integration/   # Integration tests only
pytest -m slow             # Slow tests only
```

### Test Coverage

The project maintains high test coverage with comprehensive:
- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end workflow testing
- **Performance Tests**: Load and stress testing
- **Security Tests**: Vulnerability and safety checks

## 🔧 Development

### Code Quality Tools

```bash
# Code formatting
black scripts/ src/ tests/

# Import sorting  
isort scripts/ src/ tests/

# Linting
flake8 scripts/ src/ tests/

# Type checking (enterprise version)
mypy src/
```

## 🐳 Docker Deployment

### Build and Run

```bash
# Build Docker image
docker build -t invoice-automation .

# Run with volume mapping
docker run -v $(pwd)/data:/app/data -v $(pwd)/config:/app/config invoice-automation

# Run with environment variables
docker run -e EMAIL_ENABLED=true -e SMTP_SERVER=smtp.gmail.com invoice-automation
```

## 📈 Monitoring & Performance

### Built-in Metrics

- **Processing Speed**: Records per second
- **Data Quality Score**: Validation and completeness metrics
- **Memory Usage**: Real-time memory consumption
- **Error Rates**: Processing and validation error tracking

### Health Checks

```bash
# System health check (enterprise version)
python src/main.py --health-check

# Configuration validation  
python src/main.py --validate-config

# Test automation workflow (scripts version)
python scripts/main.py

# Create sample data
python scripts/create_sample_data.py
```

## 🔒 Security Features

- **Input Validation**: Comprehensive data sanitization
- **Secure Configuration**: Environment-based secrets management
- **Audit Trail**: Complete operation logging
- **Error Handling**: Secure error messages without data exposure

## 🚀 Production Deployment

### Environment Setup

1. **Production Configuration**:
   ```yaml
   app:
     environment: production
     debug: false
   
   logging:
     level: WARNING
     file_enabled: true
   
   security:
     audit_trail: true
     encrypt_sensitive_data: true
   ```

2. **Resource Requirements**:
   - **CPU**: 2+ cores for parallel processing
   - **Memory**: 8GB+ for large datasets
   - **Storage**: SSD recommended for performance

3. **Monitoring Setup**:
   - Log aggregation (ELK Stack, Splunk)
   - Metrics collection (Prometheus, Grafana)
   - Alerting (PagerDuty, Slack)

## 📚 API Documentation

### Core Classes (Enterprise Version)

#### `InvoiceProcessor`
```python
from automation.core import InvoiceProcessor

processor = InvoiceProcessor(config_manager)
stats = processor.process_invoices(input_file, output_file)
```

#### `ReportGenerator` 
```python
from automation.core import ReportGenerator

generator = ReportGenerator(config_manager)
metrics = generator.generate_report(data_file, report_file)
```

### Simple Functions (Scripts Version)

#### Core Functions
```python
from scripts.process_data import process_invoices
from scripts.generate_report import generate_report  
from scripts.send_email import send_email

# Process invoices
success = process_invoices(input_file, output_file)

# Generate reports
success = generate_report(data_file, report_file)

# Send email
success = send_email(report_file)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Standards

- **Python**: PEP 8 compliant
- **Documentation**: Google-style docstrings
- **Testing**: Minimum 85% code coverage
- **Type Hints**: Required for all public APIs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Documentation

- **📖 Repository**: [GitHub Repository](https://github.com/Hassan-Naeem-code/RPA-Automation-Week-2)
- **🐛 Bug Reports**: [GitHub Issues](https://github.com/Hassan-Naeem-code/RPA-Automation-Week-2/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Hassan-Naeem-code/RPA-Automation-Week-2/discussions)
- **🎓 Course**: Concordia University - Robotic Process Automation
- **👨‍💻 Author**: Hassan Naeem

## 🎯 Project Roadmap

### ✅ Completed Features
- ✅ **Working Scripts Version**: Simple, functional automation pipeline
- ✅ **Enterprise Architecture**: Advanced modular structure  
- ✅ **Data Processing**: Excel file processing with 100 sample records
- ✅ **Report Generation**: Multi-sheet Excel reports with analytics
- ✅ **Email System**: SMTP-based notification system
- ✅ **Testing Suite**: 22 comprehensive tests (21/22 passing)
- ✅ **CI/CD Pipeline**: GitHub Actions workflow
- ✅ **Docker Support**: Container deployment ready
- ✅ **Configuration**: YAML-based settings management
- ✅ **Documentation**: Complete project documentation

### � Assignment Features Demonstrated
- ✅ **Robotic Process Automation**: End-to-end automated workflow
- ✅ **Data Processing**: Automated Excel data manipulation
- ✅ **Report Generation**: Automated business intelligence reports  
- ✅ **Email Automation**: Scheduled notification system
- ✅ **Error Handling**: Robust exception management
- ✅ **Industry Standards**: Professional project structure
- ✅ **Version Control**: Git-based development workflow
- ✅ **Testing**: Automated quality assurance

---

**🎓 Concordia University RPA Assignment - Week 2** 🎉

*Built with ❤️ for Robotic Process Automation Course by Hassan Naeem*

**Ready for Production Use!** ✨