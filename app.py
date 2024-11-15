from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    # Initialize feedback
    feedback = []
    # Length check
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        feedback.append("Length is good.")

    # Character diversity check
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    if not re.search(r'[\W_]', password):  # \W matches any non-alphanumeric character
        feedback.append("Password should contain at least one special character.")

    # Common pattern check (e.g., "password123")
    common_patterns = ["password", "1234", "qwerty"]
    for pattern in common_patterns:
        if pattern.lower() in password.lower():
            feedback.append(f"Password contains a common pattern: {pattern}. Try to avoid it.")

    # Suggest stronger password if feedback is present
    if len(feedback) == 1:
        feedback.append("Your password is strong.")
    return feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = []
    if request.method == 'POST':
        password = request.form['password']
        feedback = check_password_strength(password)
    return render_template('index.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
