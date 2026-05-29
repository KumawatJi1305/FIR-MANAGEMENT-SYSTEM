# 🚔 FIR Management System

A simple and efficient **FIR (First Information Report) Management System** built using **Python Flask**, **MySQL**, **HTML/CSS**, and **Bootstrap**.  
This project allows users to file FIR complaints online and enables administrators to manage, update, and monitor all FIR records through a secure dashboard.

---

# 📌 Features

- 📝 File FIR complaints online
- 🔐 Admin Login Authentication
- 📋 View all FIR records
- ✏️ Edit and update FIR details
- 📅 Automatic FIR date storage
- 📊 FIR status management (Pending/Resolved)
- 💾 MySQL Database Integration
- 🌐 User-friendly web interface

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Flask | Web Framework |
| MySQL | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| Bootstrap | Responsive UI |
| Jinja2 | Template Rendering |

---

# 📂 Project Structure

```bash
FIR-Management-System/
│
├── app.py
├── db_config.py
├── workbench1.sql
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── file_fir.html
│   ├── view_fir.html
│   └── edit.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/FIR-Management-System.git
```

---

## 2️⃣ Move into Project Folder

```bash
cd FIR-Management-System
```

---

## 3️⃣ Install Required Packages

```bash
pip install flask mysql-connector-python
```

---

## 4️⃣ Setup MySQL Database

1. Open **MySQL Workbench**
2. Create a new database:

```sql
CREATE DATABASE fir_hns;
```

3. Import the provided SQL file:

```bash
workbench1.sql
```

---

# 🔧 Database Configuration

Update your MySQL credentials inside `app.py` or `db_config.py`:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="fir_hns"
)
```

---

# ▶️ Run the Project

```bash
python app.py
```

The application will run on:

```bash
http://127.0.0.1:5000/
```

---

# 🔑 Admin Login Credentials

```text
Username : HiKe CodeX
Password : 1326
```

> You can modify these credentials inside `app.py`

---

# 📸 Main Modules

## 🏠 Home Page
- Landing page of the system
- Navigation to FIR filing and admin login

## 📝 File FIR
- Users can submit FIR details
- Complaint gets stored in MySQL database

## 🔐 Admin Login
- Secure login system for admin access

## 📋 View FIR
- Admin can view all submitted FIR records

## ✏️ Edit FIR
- Update FIR details and status

---

# 🗄️ Database Table Structure

## `all_firs`

| Column | Type |
|--------|------|
| id | INT (Primary Key) |
| name | VARCHAR |
| phone | VARCHAR |
| address | TEXT |
| complaint | TEXT |
| status | VARCHAR |
| date | DATE |

---

# 🚀 Future Improvements

- 📧 Email notifications
- 📱 Mobile responsive dashboard
- 🔍 FIR search functionality
- 📄 PDF report generation
- 👮 Multi-admin system
- 🔒 Password encryption
- ☁️ Cloud deployment

---

# 🌍 Deployment Platforms

You can deploy this project on:

- Render
- Railway
- PythonAnywhere
- Heroku
- AWS EC2

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

# 📄 License

This project is created for educational and internship purposes.

---

# 👨‍💻 Developer

Developed by **HiKe CodeX**

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---
