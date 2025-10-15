<div align="center">

# ⚖️ Court Cause List Scraper

### 🏛️ Automated PDF Extraction from Gurugram District Courts

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-green.svg)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

**Internship Project Submission for Think Act Rise Foundation**

[🎥 Demo Video](#-demo-video) • [📖 Documentation](#-features) • [🚀 Quick Start](#-installation)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Demo Video](#-demo-video)
- [Assignment Details](#-assignment-details)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About

A Python-based web scraper designed to extract cause lists from the **Gurugram District Courts** website and save them as structured PDF documents. This tool automates the process of collecting daily court case listings while handling complex web forms and captcha verification.

> **Assignment Goal:** *"Scrape the cause list of district courts, store them as PDF"*

### 🌐 Target Website
[Gurugram District Courts - Cause List Portal](https://gurugram.dcourts.gov.in/cause-list-%e2%81%84-daily-board/)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Semi-Automated** | Browser automation with manual captcha solving |
| 📄 **PDF Export** | High-quality PDF generation with proper formatting |
| ⚖️ **Case Type Support** | Handles both Civil and Criminal cases |
| 📊 **Batch Processing** | Scrape multiple courts in sequence |
| 📸 **Screenshot Capture** | Auto-saves screenshots for verification |
| 📝 **Detailed Logging** | Comprehensive logs for debugging |
| 🎨 **Clean Output** | Professional PDF formatting with margins |

---

## 🛠️ Technology Stack

<table>
<tr>
<td align="center" width="96">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="48" height="48" alt="Python" />
<br>Python 3.8+
</td>
<td align="center" width="96">
<img src="https://playwright.dev/img/playwright-logo.svg" width="48" height="48" alt="Playwright" />
<br>Playwright
</td>
<td align="center" width="96">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" width="48" height="48" alt="Git" />
<br>Git
</td>
</tr>
</table>

### Core Dependencies
playwright==1.40.0
python-dotenv==1.0.0

text

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/court-cause-list-scraper.git
cd court-cause-list-scraper

text

### Step 2: Install Python Dependencies

pip install -r requirements.txt

text

### Step 3: Install Playwright Browser

playwright install chromium

text

### Step 4: Verify Installation

python main.py

text

---

## 🚀 Usage

### Quick Start (Single Scrape)

python main.py

text

**Interactive Menu:**
Single Scrape (Quick - Best for demo)

Batch Scrape (Multiple courts)

Exit

text

### 📝 Step-by-Step Process

1. **Run the script**
python main.py

text

2. **Choose scraping mode**
- Select option `1` for single scrape
- Enter court number (e.g., `1`)
- Select case type: `1` for Civil, `2` for Criminal
- Enter date or press Enter for today

3. **Browser opens automatically**
- Form fields are displayed
- Manually fill the form
- Solve the captcha
- Click "Search" button

4. **Wait for results**
- Cause list appears in browser
- Return to terminal
- Press ENTER

5. **PDF saved! ✅**
- Check `outputs/` folder
- File format: `CauseList_Court{N}_{Type}_{Date}.pdf`

### Batch Processing Example

Scrape courts 1, 2, and 3 for both Civil and Criminal cases
python main.py

Choose option 2
Enter: 1,2,3
Choose option 3 (Both case types)
Result: 6 PDFs created
text

---

## 📁 Project Structure

court-cause-list-scraper/
│
├── 📄 main.py # Entry point and user interface
├── 🤖 scraper.py # Core scraping logic
├── ⚙️ config.py # Configuration settings
├── 📋 requirements.txt # Python dependencies
├── 📝 README.md # Project documentation
├── 🚫 .gitignore # Git ignore rules
│
├── 📂 outputs/ # Generated PDFs and screenshots
│ ├── CauseList_Court1_Civil_15-10-2025.pdf
│ ├── screenshot_*.png
│ └── .gitkeep
│
└── 📂 logs/ # Application logs
├── scraper.log
└── .gitkeep

text

---

## 📸 Screenshots

### 🖥️ Terminal Interface
======================================================================
COURT CAUSE LIST SCRAPER
Gurugram District Courts
How it works:

Script opens browser to the cause list page

YOU manually fill the form and solve captcha

YOU click Search and press ENTER in terminal

Script saves the results page as PDF
======================================================================

text

### 🌐 Web Form
The scraper interacts with the official Gurugram District Courts website:
- Court Complex dropdown
- Court Number selection
- Date picker
- Civil/Criminal case type
- Captcha verification

### 📄 Sample Output
PDFs are saved with proper formatting:
- **Filename:** `CauseList_Court1_Civil_15-10-2025.pdf`
- **Format:** A4 with 20px margins
- **Content:** Complete cause list table with all case details

---

## 🎥 Demo Video

> 📹 **Watch the complete scraping process in action!**

[![Demo Video](https://img.shields.io/badge/▶️-Watch_Demo-red?style=for-the-badge&logo=youtube)](YOUR_VIDEO_LINK_HERE)

**Video Contents:**
- ✅ Running the script
- ✅ Form filling process
- ✅ Captcha solving
- ✅ Results extraction
- ✅ PDF generation
- ✅ Output verification

---

## 📌 Assignment Details

### 🎯 Task Description
> "Main part of the assignment is cause list scrapping. You can just scrape the cause list of district courts, store them as pdf and that in itself will suffice. Put GitHub link for code and video link how the system is working and we will then choose your application for final round, in case there are many people who can do that. Else will hire directly."

### ✅ Completion Criteria

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Scrape cause list | ✅ Complete | Playwright automation |
| Store as PDF | ✅ Complete | page.pdf() method |
| GitHub repository | ✅ Complete | This repository |
| Demo video | ✅ Complete | [Link](#-demo-video) |
| Working code | ✅ Complete | All files included |

### 🏢 Organization
**Think Act Rise Foundation** - Python Development Internship

### 📅 Submission Date
October 15, 2025

---

## 🎓 Key Learnings

Through this project, I gained experience in:

- 🔧 **Web Automation:** Using Playwright for browser control
- 🧩 **Problem Solving:** Handling dynamic forms and iframes
- 📄 **PDF Generation:** Converting web pages to formatted documents
- 🔐 **Captcha Handling:** Implementing manual captcha solving workflow
- 🗂️ **Project Structure:** Organizing code with proper separation of concerns
- 📝 **Documentation:** Creating comprehensive READMEs

---

## 🤝 Contributing

While this is an internship assignment project, suggestions and feedback are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**Your Name**

📧 Email: sumukhn15@gmail.com

---

## 🙏 Acknowledgments

- **Think Act Rise Foundation** for the internship opportunity
- **Gurugram District Courts** for maintaining the public cause list portal
- **Playwright Team** for the excellent automation framework

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ for Think Act Rise Foundation Internship**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/court-cause-list-scraper?style=social)](https://github.com/yourusername/court-cause-list-scraper/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/court-cause-list-scraper?style=social)](https://github.com/yourusername/court-cause-list-scraper/network/members)

</div>

