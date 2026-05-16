# Rule-Based Career Path Recommendation Expert System for IT Job Seekers

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![CLIPS](https://img.shields.io/badge/Expert_System-CLIPS-orange.svg)
![EasyGUI](https://img.shields.io/badge/GUI-EasyGUI-green.svg)

## 📌 Project Overview

This project is a **rule-based expert system** built using the CLIPS inference engine via Python. The system is designed to help IT-related job seekers identify the most suitable career paths based on their personal and professional profiles, including:

* 🎓 **Education level** (Diploma, Degree, Master)
* 💼 **Years of experience**
* 💻 **Programming interest**
* 🧠 **Personality traits** (e.g., Detail-Oriented, Problem-Solving, Leadership)
* 🛠️ **Technical skills** (e.g., Python, AWS, LINUX, Machine Learning)

The system applies a comprehensive set of predefined **IF-THEN rules** to assert facts and fire rules, ultimately recommending the most suitable IT careers.

---

## 👨‍💻 Project Members

* **242UT2449P** See Chwan Kai
* **242UT2449Z** Kho Wei Cong
* **242UT244B2** Tee Kian Hao
* **1221302254** ALGHANEM, HUSSAIN SALEH A

---

## 🎯 Key Features

* **Rule-Based Inference:** Powered by CLIPS environment to evaluate complex career matching rules.
* **Interactive GUI:** Easy-to-use graphical interface powered by `easygui`.
* **Dynamic Feedback System:** Allows users to leave feedback, stored locally in `feedback.txt`.
* **Email Result Sharing:** Integrates with Gmail SMTP to send career suggestions directly to the user's inbox.
* **Job Search Redirection:** Automatically opens JobStreet in the user's browser tailored to their recommended career.
* **Input Validation:** Robust error handling and Regex validation for user inputs.

---

## 🧠 Supported Career Recommendations

The expert system contains rules to recommend **20 distinct IT career roles**, including:

| Software & Web | Data & AI | Infrastructure & Security | Management & Others |
|---|---|---|---|
| Junior Software Developer | Data Scientist | Network Administrator | UI/UX Designer |
| Senior Software Developer | Machine Learning Engineer | Cybersecurity Analyst | IT Project Manager |
| Web Developer | Artificial Intelligence Engineer| Cloud Engineer | Business Analyst |
| Mobile App Developer | | System Administrator | QA Engineer |
| Game Developer | | Database Administrator | IT Department Leader |
| | | IT Support Specialist | |

---

## 🛠️ Technologies Used

* **Python 3**: Core programming language.
* **CLIPS**: Expert System Engine (via `clips` / `clipspy` bindings).
* **EasyGUI**: For building the graphical user interface.
* **smtplib & email**: For sending results via email.
* **webbrowser**: For opening relevant job search links.
* **logging & re**: For environment logging and input validation.

---

## ⚙️ How It Works

1. **User Profile Collection**: The user enters personal details and completes a questionnaire via the GUI.
2. **Fact Assertion**: The system collects data (Programming interest, Education, Experience, Personality, Skills) and asserts them as facts into the CLIPS environment.
3. **Rule Firing**: CLIPS evaluates the asserted facts against its predefined rule base.
4. **Recommendation Generation**: Based on matching conditions, specific career rules fire and generate recommendations.
5. **Post-Evaluation Actions**: The user can choose to:
   * 📧 Email the results to a specified address.
   * 🌐 Search for relevant job openings online (JobStreet).
   * 🔄 Retake the test or provide feedback.

---

## 📧 Email Feature Setup

The system can send career results via email using the Gmail SMTP server.
> **Note:** An App Password is required for Gmail authentication to use this feature. The sender email configuration is located within the `send_email` function in the source code.

---

## 🚀 How to Run

### 1. Install dependencies

Ensure you have Python installed, then run the following command to install the required libraries:

```bash
pip install clips easygui
```
*(Note: If `clips` does not install the correct bindings, try `pip install clipspy`)*

### 2. Run the program

Execute the main script using Python:

```bash
python "TES6313_GroupKST_Source Code.py"
```

---

## ⚠️ Notes

* Requires the **CLIPS Python binding** installed.
* An active **internet connection** is needed for the email and job search redirection features.
* The Gmail app password must be configured within the source code to enable the email sending capability.
* User feedback is collected and stored locally in a file named `feedback.txt`.

---

## 📊 System Type

✔ **Rule-Based Expert System**  
✔ **Decision Support System**
