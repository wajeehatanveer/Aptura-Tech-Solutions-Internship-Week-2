
# 📊 API Data Processing Script

A Python-based API Data Processing project that fetches JSON data from a public API, processes and cleans the data, calculates summary statistics, and exports the processed results to a CSV file.

The project also includes a **Streamlit frontend** to provide an interactive way to fetch, view, analyze, and download the processed data.

---

## 🎯 Objective

The objective of this project is to develop a Python script that can:

- Fetch data from a public JSON API
- Extract relevant fields from the API response
- Clean and process the retrieved data
- Calculate useful summary statistics
- Export processed data to CSV
- Handle API and data-related errors
- Present the processed results through an interactive interface

---

## ✨ Features

### 🔹 API Data Fetching
- Connects to a public JSON API
- Retrieves JSON data using HTTP requests
- Handles connection, timeout, HTTP, and JSON errors

### 🔹 Data Processing
- Extracts selected fields:
  - ID
  - User ID
  - Title
  - Body
- Removes unnecessary whitespace
- Validates required fields
- Skips incomplete records

### 🔹 Summary Statistics
The application calculates:

- Total number of records
- Number of unique users
- Average title length
- Average body length

### 🔹 CSV Export
Processed data can be exported as:`

The Streamlit interface also provides a download button for the processed CSV file.

### 🔹 Streamlit Dashboard

The frontend provides:

* API data fetching
* Summary statistics
* Processed data table
* CSV download functionality
* Success and error messages

---

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **Pandas**
* **Streamlit**
* **JSON**
* **CSV**

---

## 📁 Project Structure

```text
Task 2 - API Data Processing/
│
├── api_processor.py
├── app.py
├── output.csv
├── README.md
└── screenshots/
    ├── 01_dashboard.png
    ├── 02_processed_data.png
    ├── 03_export_data.png
    └── 04_terminal_output.png
```

---

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install requests pandas streamlit
```

---

## ▶️ Running the Python Script

Run the API processing script using:

```bash
python api_processor.py
```

The script will:

1. Fetch data from the API
2. Process valid records
3. Calculate statistics
4. Display the results
5. Export the processed data to `output.csv`

---

## 🌐 Running the Streamlit App

Launch the interactive dashboard using:

```bash
streamlit run app.py
```

T
## 📊 Output

The project successfully processes **100 API records** and calculates summary statistics including:

* Total Records
* Unique Users
* Average Title Length
* Average Body Length

The processed records are displayed in a structured table and can be exported as a CSV file.

---


## 📚 What I Learned

Through this project, I learned how to:

* Work with public APIs
* Send HTTP requests using Python
* Handle JSON responses
* Clean and validate data
* Calculate basic statistics
* Export data to CSV
* Handle API errors and exceptions
* Build an interactive Streamlit interface
* Connect data processing logic with a frontend

---

## 👩‍💻 Internship Task

**Aptura Tech Solutions — Python Internship**

**Week 2 — Task 2: API Data Processing Script**

````
