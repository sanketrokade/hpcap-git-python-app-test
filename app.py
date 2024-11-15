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
            # Get the input values from the form, with default empty string in case no input
            num1 = request.form.get('num1', '').strip()  # Remove any leading/trailing spaces
            num2 = request.form.get('num2', '').strip()  # Remove any leading/trailing spaces
            operation = request.form.get('operation', '')  # Get selected operation

            # Ensure that both numbers are provided, else show an error
            if not num1 or not num2:
                error_message = "Both numbers are required. Please enter valid numbers."
            
            # Proceed only if both numbers are provided
            else:
                # Attempt to convert input values to floats
                try:
                    num1 = float(num1)  # Convert num1 to float
                    num2 = float(num2)  # Convert num2 to float
                except ValueError:
                    # Handle the case where the user enters non-numeric values
                    error_message = "Invalid input. Please enter valid numeric values."

                # Perform the calculation if inputs are valid
                if not error_message:  # Proceed only if there is no error in inputs
                    if operation == 'add':
                        result = num1 + num2
                    elif operation == 'subtract':
                        result = num1 - num2
                    elif operation == 'multiply':
                        result = num1 * num2
                    elif operation == 'divide':
                        if num2 != 0:
                            result = num1 / num2  # Perform division
                        else:
                            # Show error if division by zero is attempted
                            error_message = "Cannot divide by zero."
                    else:
                        # Error message for invalid operation (if the operation is not recognized)
                        error_message = "Invalid operation selected. Please try again."

    # Return the rendered HTML page with the result and any error message
    return render_template('index.html', result=result, error_message=error_message, num1=num1, num2=num2, operation=operation)

# Ensure the app runs only if this script is executed directly (not when imported)
if __name__ == '__main__':
    app.run(debug=True)

