# Phase 1: Password Strength Analyzer (Flask App)

This is a simple web application built with **Flask** that allows users to analyze the strength of a password based on several common security criteria. The application provides immediate feedback and keeps a short history of the last few attempts.

---

## Features

The application classifies password strength based on five criteria.

* **Password Strength Analysis:** Evaluates passwords for:
    * Minimum **length** of 8 characters.
    * Inclusion of at least one **digit**.
    * Inclusion of at least one **uppercase** letter.
    * Inclusion of at least one **lowercase** letter.
    * Inclusion of at least one **special character** (`!@#$%^&*()-_+=...`).
* **Strength Classification:** Assigns a strength level based on the number of passed criteria:
    * **Strong:** Meets all 5 criteria.
    * **Moderate:** Meets 3 or 4 criteria.
    * **Weak:** Meets 0, 1, or 2 criteria.
* **Attempt History (Queue):** Maintains a queue (`collections.deque` with `maxlen=5`) of the last 5 analyzed passwords and their strength scores.
* **"Stack Simulation":** Displays the analyzed password in **reversed order** to demonstrate a simple data structure manipulation (stack pop simulation).

---

## Project Structure

The project follows a standard Flask structure:
