from flask import Flask, render_template, request, redirect, url_for
from collections import deque

app = Flask(__name__)


history = deque(maxlen=5)

def analyze_password(password):
    
    stack_sim = "".join(list(password)[::-1])

    result = {
        "password": password,
        "length": len(password) >= 8,
        "digit": any(c.isdigit() for c in password),
        "upper": any(c.isupper() for c in password),
        "lower": any(c.islower() for c in password),
        "special": any(c in "!@#$%^&*()-_+=[]{};:'\",.<>/?\\|`~" for c in password),
        "stack": stack_sim
    }

    score = sum([result["length"], result["digit"], result["upper"], result["lower"], result["special"]])
    if score == 5:
        result["strength"] = "Strong"
    elif score >= 3:
        result["strength"] = "Moderate"
    else:
        result["strength"] = "Weak"

    return result

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=None, history=list(history))

@app.route("/analyze", methods=["POST"])
def analyze_route():
    pwd = request.form.get("password", "").strip()
    if not pwd:
        return redirect(url_for("index"))
    res = analyze_password(pwd)
    # store in queue (history)
    history.appendleft({"password": pwd, "strength": res["strength"]})
    return render_template("index.html", result=res, history=list(history))

if __name__ == "__main__":
    app.run(debug=True)
