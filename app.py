from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None  # To store the result of the calculation
    error_message = None  # To store any error messages

    # Check if the request method is POST (i.e., form was submitted)
    if request.method == 'POST':
        try:
            # Attempt to get and convert the input values to floats
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            # Perform the calculation based on the selected operation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2  # Division
                else:
                    # Error message for division by zero
                    error_message = "Cannot divide by zero."
            else:
                # Error message for invalid operation
                error_message = "Invalid operation selected. Please try again."
        
        except ValueError:
            # Error message for invalid number input
            error_message = "Invalid input. Please enter valid numbers."

    # Return the rendered HTML page with the result and any error message
    return render_template('index.html', result=result, error_message=error_message)

# Ensure the app runs only if this script is executed directly (not when imported)
if __name__ == '__main__':
    app.run(debug=True)

