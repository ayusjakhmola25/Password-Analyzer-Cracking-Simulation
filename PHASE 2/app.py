from flask import Flask, render_template, request
from collections import deque
import time
import re
import os
import math # <--- ADDED: math is now needed for log2

app = Flask(__name__)

# --- Data & History ---
PASSWORD_LIST = ["12345678", "password123", "qwerty", "admin", "test1", "user", "abc123", "111111", "000000", "p@ssw0rd",
    "qazwsx", "asdfgh", "12341234", "myname", "Secret", "master", "dragon", "hello", "laptop", "access",
    "login", "changeit", "rootuser", "guest1", "welcome", "Abcdef", "Test", "UserPass", "admin01", "password",
    "123456", "PassWord", "User123", "Tester", "System", "dummy", "sample", "demo", "Demo123", "Secure",
    "MyPass", "Pass1", "Pass2", "Pass3", "Pass4", "Pass5", "Pass6", "Pass7", "Pass8", "Pass9",
    "1a2b3c", "3c4d5e", "5e6f7g", "7g8h9i", "9i0j1k", "k1j0i9", "i9h8g7", "g7f6e5", "e5d4c3", "c3b2a1",
    "password!", "admin@", "test#", "user$", "abc%", "123^", "qwerty&", "asdf*", "zxcvbn(", "mnbvcxz)",
    "apple", "banana", "orange", "grape", "melon", "cherry", "mango", "kiwi", "lime", "peach",
    "Python", "Flask", "Django", "Coder", "Script", "WebDev", "Data", "Cloud", "Linux", "Windows",
    "Home", "Work", "Office", "School", "Street", "House", "Car", "Bike", "Bus", "Train"]

# History for Search Simulation (Newest to the left/top)
search_history = deque(maxlen=5)
# History for Strength Analyzer (Changed to appendleft for newest to the top)
analyze_history = deque(maxlen=5)

CRITERIA = {
    'length': lambda p: len(p) >= 8,
    'digit': lambda p: bool(re.search(r'\d', p)),
    'upper': lambda p: bool(re.search(r'[A-Z]', p)),
    'lower': lambda p: bool(re.search(r'[a-z]', p)),
    'special': lambda p: bool(re.search(r'[!@#$%^&*()_+=\-{}[\]:;"\'<,>.?/`~]', p))
}

# --- Search Simulation Functions (Unchanged) ---

def linear_search(target, password_list, delay=0.2):
    attempts = []
    start = time.time()
    for p in password_list:
        attempts.append({"tried": p, "match": p == target})
        time.sleep(delay)
        if p == target:
            break
    end = time.time()
    found = any(a["match"] for a in attempts)
    return attempts, found, len(attempts), end - start

def binary_search(target, password_list, delay=0.2):
    arr = sorted(password_list) 
    attempts = []
    low, high = 0, len(arr) - 1
    start = time.time()
    while low <= high:
        mid = (low + high) // 2
        tried = arr[mid]
        attempts.append({"tried": tried, "match": tried == target})
        time.sleep(delay)
        if tried == target:
            break
        if target < tried: 
            high = mid - 1
        else:
            low = mid + 1
    end = time.time()
    found = any(a["match"] for a in attempts)
    return arr, attempts, found, len(attempts), end - start

# --- New/Modified Strength Analyzer Functions ---

def calculate_entropy(password):
    """Calculates password entropy in bits."""
    length = len(password)
    if length == 0:
        return 0.0

    # Determine character set size (N)
    N = 0
    if re.search(r'[a-z]', password):
        N += 26  # Lowercase
    if re.search(r'[A-Z]', password):
        N += 26  # Uppercase
    if re.search(r'\d', password):
        N += 10  # Digits
    # Using a common special character set size for simplicity (approximate)
    if re.search(r'[!@#$%^&*()_+=\-{}[\]:;"\'<,>.?/`~]', password):
        N += 32  # Special characters (approx. 32 common ones)

    if N == 0:
        return 0.0
    
    # Entropy formula: H = L * log2(N)
    entropy_bits = length * math.log2(N)
    return entropy_bits

def format_crack_time(seconds):
    """Formats a large number of seconds into human-readable time."""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    if seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f} minutes"
    if seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.1f} hours"
    if seconds < 31536000:
        days = seconds / 86400
        return f"{days:.1f} days"
    
    years = seconds / 31536000
    return f"{years:.1f} years"

def analyze_password_strength(password, crack_speed=10**9):
    """Analyzes strength, calculates entropy, and estimates crack time."""
    results = {
        name: check(password)
        for name, check in CRITERIA.items()
    }
    
    passed_count = sum(results.values())
    
    if passed_count == 5:
        strength = "Strong"
    elif passed_count >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    entropy_bits = calculate_entropy(password)
    
    # Calculate total possible combinations (2^Entropy)
    total_combinations = 2**entropy_bits
    
    # Estimate time to crack (seconds)
    # Assumes a constant crack speed (e.g., 1 billion guesses per second)
    if crack_speed > 0:
        # Time = Combinations / Crack_Speed
        time_seconds = total_combinations / crack_speed
        crack_time_readable = format_crack_time(time_seconds)
    else:
        crack_time_readable = "N/A"

    stack_sim = "".join(reversed(password))
    
    results['strength'] = strength
    results['stack'] = stack_sim
    results['entropy_bits'] = round(entropy_bits, 2)
    results['crack_time'] = crack_time_readable
    results['crack_speed_gph'] = f"{crack_speed/10**9} Billion / second" # For display
    
    return results

# --- Flask Route (Handles both GET and POST for both features) ---

@app.route('/', methods=['GET', 'POST'])
def index():
    context = {
        'list_size': len(PASSWORD_LIST),
        'search_history': list(search_history),
        'analyze_history': list(analyze_history),
        'active_tab': 'search' # Default tab on GET
    }

    if request.method == 'POST':
        form_type = request.form.get('form_type')
        
        if form_type == 'search_simulation':
            context['active_tab'] = 'search'
            password = request.form.get('password', '').strip()
            
            try:
                delay = float(request.form.get('delay', '0.2'))
                if delay < 0: delay = 0.2
            except:
                delay = 0.2

            linear_attempts, linear_found, linear_count, linear_time = linear_search(password, PASSWORD_LIST, delay=delay)
            sorted_list, binary_attempts, binary_found, binary_count, binary_time = binary_search(password, PASSWORD_LIST, delay=delay)

            linear_message = (f"Password found in {linear_count} attempts using Linear Search." if linear_found
                              else f"Password NOT found after {linear_count} attempts using Linear Search.")
            binary_message = (f"Password found in {binary_count} attempts using Binary Search." if binary_found
                              else f"Password NOT found after {binary_count} attempts using Binary Search.")

            search_history.appendleft({"password": password,
                                "linear": f"{linear_count} attempts ({'found' if linear_found else 'not found'})",
                                "binary": f"{binary_count} attempts ({'found' if binary_found else 'not found'})"})

            context.update({
                "linear_attempts": linear_attempts,
                "binary_attempts": binary_attempts,
                "linear_message": linear_message,
                "binary_message": binary_message,
                "linear_time": linear_time,
                "binary_time": binary_time,
                "sorted_list": sorted_list,
                "delay": delay
            })
            context['search_history'] = list(search_history)

        elif form_type == 'strength_analyzer':
            context['active_tab'] = 'analyze'
            password = request.form.get('analyze_password', '')
            
            # Using default crack speed of 10^9
            result = analyze_password_strength(password) 
            
            history_item = {
                'password': password,
                'strength': result['strength']
            }
            analyze_history.appendleft(history_item)
            
            context['analyze_result'] = result
            context['analyze_history'] = list(analyze_history)

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5001)