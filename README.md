# Automated File Organizer CLI Tool

**Domain:** Python Developer  
**Internship Program:** SoftNexis Internship  

---

## 📌 Project Overview
This Python command-line tool scans a designated directory, identifies files by their extensions, and automatically groups them into categorized folders (e.g., `Documents`, `Images`, `Python_Code`).

---

## 🛠️ Features & Key Implementations
- **Directory Traversal:** Leveraged Python's `pathlib` module to scan files and directories safely.
- **Categorization Engine:** Maps file extensions (`.py`, `.txt`, `.jpg`, `.pdf`, etc.) to specific category folders.
- **Conflict Handling:** Prevents file overwrites by appending numerical suffixes (e.g., `report_copy1.txt`) if a duplicate exists.
- **Dry-Run Preview (`--dry-run`):** Allows users to preview organizational moves before making permanent changes.
- **Logging & Auditing:** Automatically logs execution details, timestamps, and potential errors to `organizer.log`.

---

## 🚀 How to Run
1. **Preview Changes (Dry Run):**
   ```bash
   python organizer.py test_folder --dry-run
