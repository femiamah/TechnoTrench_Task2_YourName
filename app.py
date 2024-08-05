from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)
    
    score = 0
    suggestions = []
    
    if length >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")
    
    if has_upper:
        score += 1
    else:
        suggestions.append("Password should include at least one uppercase letter.")
    
    if has_lower:
        score += 1
    else:
        suggestions.append("Password should include at least one lowercase letter.")
    
    if has_digit:
        score += 1
    else:
        suggestions.append("Password should include at least one digit.")
    
    if has_special:
        score += 1
    else:
        suggestions.append("Password should include at least one special character.")
    
    strength = "Weak"
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    
    return strength, suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    strength, suggestions = check_password_strength(password)
    return render_template('result.html', password=password, strength=strength, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
