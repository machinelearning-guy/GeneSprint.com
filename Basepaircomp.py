from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/reverse', methods=['POST'])
def reverse():
    input_text = request.form['input_text']
    # Reverse the string
    reversed_text = input_text[::-1]
    return render_template('index.html', original=input_text, reversed=reversed_text)

if __name__ == '__main__':
    app.run(debug=True)

