# Save this code in a file called calculator_app.py

import streamlit as st

# Title and instructions
st.title("Simple Calculator")
st.write("Choose an operation and enter two numbers.")

# Select operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Input numbers
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero is undefined.")

    # Display result
    if result is not None:
        st.write(f"The result of {operation} is: {result}")
