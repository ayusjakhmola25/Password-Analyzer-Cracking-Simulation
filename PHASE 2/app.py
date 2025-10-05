from flask import Flask, render_template, request
from collections import deque
import time
import os

app = Flask(__name__)

# Dummy password list
PASSWORD_LIST = ["123", "abc", "Abc123!", "P@ssw0rd"]

# Queue to store last 5 attempts
history = deque(maxlen=5)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    context = {"password_list": PASSWORD_LIST}
    if request.method == 'POST':
        password = request.form.get('password', '').strip()
        # optional: custom delay from form
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

        history.appendleft({"password": password,
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
            "history": list(history),
            "delay": delay
        })

    return render_template('index.html', **context)

if __name__ == '__main__':
    # ensure Flask can find static/templates when run
    app.run(debug=True)
