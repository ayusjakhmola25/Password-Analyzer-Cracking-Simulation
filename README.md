
🔑 Password Cracking & Analyzer Tool
This project is an advanced, educational web utility built with Flask that provides a hands-on environment for understanding password security mechanics. It combines a Cracking Simulation to visualize attack efficiency with a comprehensive Strength Analyzer to evaluate password robustness.

The application features a sleek, professional dark-themed interface to visually compare search algorithms and provide detailed password scores.

✨ Key Features
The utility is divided into two core functionalities accessible via distinct tabs:

🔬 Strength Analyzer & Security Assessment
This component provides immediate, criteria-based feedback on password security using a comprehensive scoring system.

Criteria-Based Scoring: Passwords are scored based on 5 essential criteria (Length ≥8, Uppercase, Lowercase, Digit, Special Character) to determine its strength rating.

Strength Tiers: Categorizes passwords as Weak, Moderate, or Strong based on the number of criteria met.

⏳ Estimated Crack Time: Calculates the theoretical Entropy of a password and estimates the time required for a brute-force attack using modern hardware assumptions.

📚 Dynamic Dictionary Integration: Any password analyzed here is automatically saved to the internal dictionary file (password.txt), making the Cracking Simulation instantly more relevant and interactive.

📊 Data Structure Showcase: Demonstrates practical data structures:

History Queue (FIFO): Uses a collections.deque to store and display the last 5 analyzed password attempts.

Stack Simulation: Displays the entered password in reversed order, mimicking the output of popping elements off a stack.

⚡ Cracking Simulation
This tab visually compares the efficiency of different search algorithms on a pre-defined or dynamically updated dictionary list.

Algorithm Comparison: Visually compare Linear Search (Brute-Force) against Binary Search (Optimized) on the dictionary list.

Performance Visualization: Clearly illustrates the performance difference between O(n) and O(logn) time complexity in a practical context.

Metrics Display: Observe the difference in Number of Attempts and Time Taken between the two algorithms to find the target password.

🛠️ Technology Stack
Component	Technology	Role
Backend Logic	Python 3.8+	Core application logic, algorithms, and strength calculation.
Web Framework	Flask	Lightweight framework for routing and serving the web application.
Data Structures	collections.deque	Efficiently manages the real-time history logs (Queue).
Frontend	HTML5, CSS3	Custom dark theme for a sleek, technical UI/UX.

Export to Sheets
🚀 Setup and Installation
Follow these steps to get the Password Cracking & Analyzer Tool running locally.

Prerequisites
Python 3.x installed on your system.

1. Clone the repository
Bash

git clone [https://github.com/your-username/password-security-lab.git](https://github.com/your-username/password-security-lab.git)
cd password-security-lab
2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

Bash

python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows (Command Prompt)
.\venv\Scripts\activate
3. Install Dependencies
This project only requires the Flask web framework.

Bash

pip install Flask
4. Run the Application
Start the Flask server from the project root directory:

Bash

python app.py
The application will now be accessible in your web browser at: http://127.0.0.1:5001/.

🎯 Usage
Tab 1: Strength Analyzer
Navigate to the Strength Analyzer tab.

Enter any password you wish to evaluate.

Click Analyze Password.

Review the detailed Strength Rating, Estimated Brute-Force Crack Time, and the History Queue update.

Tab 2: Cracking Simulation
Navigate to the Cracking Simulation tab.

Enter a password. (For best results, use a password known to be in password.txt—either a default one or one you recently analyzed).

Click Start Simulation to watch the linear and binary searches run side-by-side.

Observe the significant performance difference in the displayed metrics.

🤝 Contributing
Contributions are greatly appreciated. They are what make the open-source community an amazing place to learn and inspire.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📜 License
Distributed under the MIT License. See LICENSE for more information.

<p align="center">Built with 💙 for Cybersecurity Education</p>
