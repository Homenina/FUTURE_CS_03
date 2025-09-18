# 🔐 Secure File Sharing System (Flask + AES)

## 📌 Introduction  
This project is a **Secure File Sharing System** built with **Python Flask** as the backend framework and **AES encryption** for data protection.  

The system allows users to:  
- **Upload files** → automatically encrypted before storage  
- **Download files** → decrypted before delivery  

It simulates a real-world solution for secure data sharing in industries such as **healthcare, law, and corporate organizations**.

---

## 🛠 Tools and Technologies  

- **Python Flask** – backend web application framework  
- **PyCryptodome (AES)** – encryption and decryption of files  
- **HTML / CSS** – simple user interface  
- **Virtual Environment (venv)** – project isolation  
- **Web Browser (localhost)** – for testing and usage  

---

## ⚙️ Implementation  

### 1️⃣ Environment Setup  
- Installed Flask and PyCryptodome.  
- Created project folders:  
  - `templates/`  
  - `uploads/`  
- Generated a secure AES key and stored it as an **environment variable**.  

### 2️⃣ Application Development  
- Implemented `app.py` with Flask routes for:  
  - Uploading & encrypting files  
  - Listing available files  
  - Downloading & decrypting files  
- Designed the user interface with `index.html` in `templates/`.  

### 3️⃣ Running the App  
- Activate virtual environment:  
  ```bash
  venv\Scripts\activate   # Windows  
  source venv/bin/activate # Mac/Linux
