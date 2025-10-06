# 🔒 Phase 1: Flask Password Strength Analyzer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

This project, **Phase 1 of the Password Strength Analyzer**, is a sleek and functional web application built with **Python and Flask**. It provides immediate, criteria-based feedback on password security and demonstrates fundamental data structures (Queue/Stack) in a practical setting.

➡️ **Ready to test your password?** Get started below!

---

## ✨ Features That Shine

We analyze your password using a comprehensive scoring system to categorize its strength:

| Criteria (Pass/Fail) | Description |
| :--- | :--- |
| **Length** | Must be 8 characters or longer. |
| **Digit** | Must contain at least one number (0-9). |
| **Uppercase** | Must contain at least one capital letter (A-Z). |
| **Lowercase** | Must contain at least one small letter (a-z). |
| **Special Char** | Must contain at least one special character (e.g., `!@#$%^&*`). |

### 🏆 Strength Tiers

* 🟢 **Strong:** Meets **all 5** criteria. Your password is secure!
* 🟠 **Moderate:** Meets **3 or 4** criteria. Good, but could be stronger.
* 🔴 **Weak:** Meets **0, 1, or 2** criteria. Time to update your password!

### 📊 Data Structure Showcase

1.  **History Queue (FIFO):** We use a **`collections.deque`** (a highly optimized double-ended queue) to store and display the last **5** analyzed password attempts, keeping your recent history tidy.
2.  **Stack Simulation:** For demonstration, the result includes a **"Stack Simulation"** which simply displays your entered password in **reversed order**—mimicking the output of popping all elements off a stack!.

---

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | **Python** | The core programming language. |
| **Web Framework** | **Flask** | Lightweight and powerful micro-framework for the web server and routing. |
| **Data Structure** | **`collections.deque`** | Efficiently manages the history queue. |
| **Frontend** | **HTML5/CSS3** | Structured template and custom styling (`style.css`) for a clean UI. |

---

## 🚀 Getting Started

Follow these simple steps to get the application running on your local machine.

### Prerequisites

You need **Python 3.x** installed on your system.

### 1. Setup

If you have cloned the repository, ensure your files are structured correctly:
