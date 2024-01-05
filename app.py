from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/neon', methods=['GET'])
def admin():
    return "Hello Komiljon!"

@app.route('/run<int:run_number>', methods=['HEAD'])
def run_command(run_number):
    if request.method == 'HEAD':
        command_result = execute_command(f'python3 main.py for run{run_number}')
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
