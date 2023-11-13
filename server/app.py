#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

# base URL
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# print the string in the terminal and display it in the web browser
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

# display all numbers in the range of parameter on separate lines
@app.route("/count/<int:parameter>")
def count(parameter):
    # range(start, stop[, step])
    output = "\n".join([f"{x}" for x in range(parameter)]) + "\n"
    return output

# perform the appropriate operation on the two numbers
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    # can try match, case ?
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return "Invalid operation"

if __name__ == "__main__":
    app.run(port=5555, debug=True)