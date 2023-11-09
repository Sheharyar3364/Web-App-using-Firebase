from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message('New Contact Form Submission',
                      recipients=['dummy@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f"Error: {str(e)}", 'danger')

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)