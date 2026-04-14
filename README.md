# Rule-based Career Path Recommendation Expert System for IT-related Job Seekers

## 📌 Project Overview

This project is a **rule-based expert system** built using the CLIPS inference engine in Python. The system helps IT-related job seekers identify suitable career paths based on their:

* Education level
* Years of experience
* Programming interest
* Personality traits
* Technical skills

The system applies a set of predefined **IF-THEN rules** to recommend the most suitable IT career.

---


## 👨‍💻 Project Members

* 242UT2449P See Chwan Kai
* 242UT2449Z Kho Wei Cong
* 242UT244B2 Tee Kian Hao
* 1221302254 ALGHANEM, HUSSAIN SALEH A

---

## 🎯 Features

* Rule-based inference using CLIPS
* Career recommendations based on user profile
* GUI-based user interaction using EasyGUI
* Feedback collection system
* Email result sharing (SMTP Gmail integration)
* Job search redirection via JobStreet

---

## 🧠 Career Rules Included

The system supports recommendations for 20 IT career roles, including:

* Junior Software Developer
* Senior Software Developer
* Data Scientist
* Network Administrator
* Cybersecurity Analyst
* Web Developer
* DevOps Engineer
* Cloud Engineer
* Artificial Intelligence Engineer
* Mobile App Developer
* UI/UX Designer
* IT Project Manager
* Game Developer
* Business Analyst
* System Administrator
* QA Engineer
* Machine Learning Engineer
* Database Administrator
* IT Department Leader

---

## 🛠️ Technologies Used

* Python 3
* CLIPS (Expert System Engine)
* EasyGUI (User Interface)
* smtplib (Email Service)
* webbrowser (Job search redirection)
* logging
* regex (input validation)

---

## ⚙️ How It Works

1. User enters personal details via GUI
2. System collects:

   * Programming interest
   * Education level
   * Years of experience
   * Personality traits
   * Skills
3. Facts are asserted into CLIPS environment
4. Rules are fired based on matching conditions
5. Career recommendation(s) are generated
6. User can:

   * Email results
   * Search jobs online
   * Retake the test

---

## 📧 Email Feature

The system can send career results via email using Gmail SMTP.

> Note: App password is required for Gmail authentication.

---

## 💬 Feedback Feature

User feedback is stored locally in:

```
feedback.txt
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install clips easygui
```

### 2. Run the program

```bash
python main.py
```

---

## ⚠️ Notes

* Requires CLIPS Python binding installed
* Internet connection needed for email and job search features
* Gmail app password must be configured for email sending

---

## 📊 System Type

✔ Rule-Based Expert System
✔ Decision Support System
