from flask import Flask, render_template, request

app = Flask(__name__)

# Define the routes and their functions

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error_message = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            # Perform the calculation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error_message = "Cannot divide by zero"
            else:
                error_message = "Invalid operation"
        except ValueError:
            error_message = "Invalid input. Please enter valid numbers."
    
    return render_template('index.html', result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

