# 🧹 Data Cleaner Pro

## ✨ Overview

**Data Cleaner Pro** is a powerful Streamlit-based tool that allows users to upload, clean, transform, and convert data files (CSV, XLSX, Markdown, HTML). It applies various cleaning operations and provides file conversion options for better usability.

## 🚀 Features

- **Multiple File Uploads:** Supports CSV, Excel, Markdown, and HTML files.
- **Data Cleaning:**
  - Remove duplicates
  - Fill missing numeric values with the column mean
  - Select specific columns to retain
- **Data Visualization:** Displays bar charts for numerical columns.
- **File Conversion:** Converts the cleaned data into CSV, Excel, Markdown, or HTML formats for easy download.

## 🔧 Installation & Setup

### 1️⃣ Prerequisites

Ensure you have Python installed. Recommended version: **Python 3.8+**

### 2️⃣ Install Dependencies
```bash
poetry add streamlit pandas openpyxl
```

## 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 🛠 Known Issues & Areas of Improvement

### Handling Multiple File Merging Efficiently

- **Issue:** If files have different structures (columns missing or in different orders), merging may cause misalignment.
- **Possible Fix:** Implement a schema-matching mechanism to handle varying column structures intelligently.

### Enhanced Data Cleaning Options

- Additional cleaning features such as:
  - Handling outliers
  - Standardizing text format
  - More advanced missing value imputation methods




**Made with ❤️ using Python & Streamlit**

