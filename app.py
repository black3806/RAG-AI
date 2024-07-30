from flask import Flask, request, render_template
import subprocess
import re
import shlex

app = Flask(__name__)

def sanitize_input(user_input):
    """
    Sanitize the input to prevent command injection and other potential issues.
    """
    # Basic sanitization: remove or escape dangerous characters
    # For a more comprehensive approach, you might need to adapt based on your input expectations.
    sanitized_input = re.sub(r'[^\w\s]', '', user_input)  # Remove all non-alphanumeric characters except spaces
    return sanitized_input

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ''
    error_message = ''
    
    if request.method == 'POST':
        question = request.form['question']
        
        if len(question) > 500:
            error_message = 'Input is too long. Please limit your question to 300 characters.'
        else:
            sanitized_question = sanitize_input(question)
            
            # Safely build the command line
            cmd = ['python3', 'query_data.py', shlex.quote(sanitized_question)]
            
            # Call the external script with the sanitized question
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            answer = result.stdout  # Get the output from the script

    return render_template('index.html', answer=answer, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
