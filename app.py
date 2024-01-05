from flask import Flask, request

app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    if request.method == 'POST':
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
