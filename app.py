from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/run_command', methods=['GET', 'POST', 'HEAD'])
def run_command():
    if request.method == 'POST' or request.method == 'GET' or request.method == 'HEAD':
        # Add security checks here if needed
        # For simplicity, no security checks are included in this example
        command_result = execute_command('python3 main.py')
        return command_result

def execute_command(command):
    import subprocess
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return f"Command Output: {result.stdout}\nCommand Error: {result.stderr}\n"
    except Exception as e:
        return f"Error: {str(e)}\n"

if __name__ == '__main__':
    app.run(debug=True)
    while True:
        subprocess.run('timeout 100 python3 main.py', capture_output=True, text=True)
